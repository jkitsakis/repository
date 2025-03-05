import time
import requests
import ctypes
import webbrowser
from plyer import notification

from configuration.configuration_params import Parameters
from utilities.send_email import EmailSender
from utilities.update_desk import UpdateDesk


def process_response(response):
    """Process the JSON response to extract the required data."""
    if "AMALIAS" in response:
        for floor in response["AMALIAS"]:
            if floor.get("positionDtoList"):
                floorInResposnse = floor.get("floor")
                position = floor["positionDtoList"][0]  # Get first element in positionDtoList
                # Extract required data if available
                if "floor" in floor and "id" in position and "x" in position and "y" in position and "code" in position and "available" in position:
                    return {
                        "floor": floorInResposnse,
                        "id": position["id"],
                        "x": position["x"],
                        "y": position["y"],
                        "code": position["code"],
                        "available": position["available"]
                    }
    return None

def make_get_request(date):
    """Make a GET request for a specific date."""
    response = requests.get(Parameters.available_seats_url, headers=Parameters.get_headers, params={"dates": date, "sectorName": "AMALIAS"})
    if response.status_code == 200:
        response_data = response.json()
        return process_response(response_data)
    else:
        print(f"Request failed for {date} with status code {response.status_code}")
        return None




def process_response_future(response):
    data_list = []
    """Process the JSON response to extract the required data."""
    if "deskBookings" in response:
        for deskBooking in response["deskBookings"]:
            extracted_data = {
                "date": deskBooking.get("date"),
                "code": deskBooking.get("code")
            }
            data_list.append(extracted_data)

    return data_list

def get_my_booked_desks():
    """Make a GET request for a specific date."""
    response_future = requests.get(Parameters.my_booked_desks_url, headers=Parameters.get_headers)

    if response_future.status_code == 200:
        response_data_future = response_future.json()
        return process_response_future(response_data_future)


def show_notification_interacted(title, message):
    # popup window
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)

def show_notification_windows(title, message):
    """Display a system notification on Windows."""
    notification.notify(
        title=title,
        message=message,
        app_name="Data Alert",
        timeout=60  # Duration of the notification in seconds
    )

def main_avalilability():
    days = Parameters.dates
    while True:
        try:
            my_booked_desks = get_my_booked_desks()

            for date in days:
                print(f"Processing for {date} ...")
                available_future_desk = make_get_request(date)

                if available_future_desk:
                    print(f"Found desk for {date}:")
                    available_desk = {'code': available_future_desk['code'], 'date': date}

                    if available_desk not in my_booked_desks :
                        message_title = Parameters.message_title_template.substitute(date=date, floor=available_future_desk['floor'])
                        message_txt = Parameters.message_txt_template.substitute(date=date, floor=available_future_desk['floor'], code=available_future_desk['code'])
                        print(f"{message_txt}\n")

                        # webbrowser.open_new(referer_url)
                        # referer_url = Parameters.referer_url.substitute(
                        # deskbookingid=UpdateDesk.get_my_booking_id(date))
                        # email_txt = message_txt + f"\n \n {referer_url}"
                        # EmailSender.send_email(message_title, email_txt)
                        show_notification_windows(message_title, message_txt)

                        if UpdateDesk.book_seat(available_future_desk['code'], date):
                            message_success = Parameters.mail_success_template.substitute(date=date, floor=available_future_desk['floor'], code=available_future_desk['code'])
                            print(f"{message_success}\n")
                            EmailSender.send_email("Planner, Desk Booked", message_success + f"\n \n {Parameters.planner_url}")

                        # --- Specific Floor
                        if available_future_desk['floor'] == 'Mezzazine':
                            days.remove(date)

                    # elif available_desk in my_booked_desks and (available_future_desk['floor'] == '2nd Floor' or available_future_desk['floor'] == '3rd Floor'):
                    elif available_desk in my_booked_desks and available_future_desk['floor'] != 'Mezzazine':
                        print(f"Desk {available_desk['code']} on {available_future_desk['floor']} is already booked. Search again ...")
                    else:
                        #already booked. no search again
                        print(f"Already booked for {date} will be removed from dates array ")
                        days.remove(date)
                else:
                    print(f"No data found for {date} ")

            if not days:
                print("All days processed with available data found.")
                break  # Exit the loop if all days have been processed successfully


            # Wait before checking again (e.g., 1 hour)
            print("Waiting for the next check...\n ---")
            time.sleep(Parameters.sleep_in_availability)  # Delay in seconds (3600 seconds = 1 hour)
        except Exception as e:
            print(f"Connection refused by the server..")
            print(f"Original cause: {e}\n")
            print("Let me sleep for 5 seconds")
            time.sleep(5)
            print(f"Was a nice sleep, now let me continue...\n")
            continue
