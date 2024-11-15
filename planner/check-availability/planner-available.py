import time
import requests
import datetime
import ctypes
import webbrowser
from plyer import notification

from send_email import EmailSender
from book_desk import BookDesk

from configuration_params import Parameters

def get_days_for_week():
    """Returns the list of dates from tomorrow until Friday."""
    today = datetime.datetime.now()
    days = []
    # Get dates from tomorrow till Friday (5 days in total)
    for i in range(1, 9):
        day = today + datetime.timedelta(days=i)
        # Only include weekdays (Monday = 0, Sunday = 6)
        if day.weekday() < 5:
            days.append(day.strftime('%Y-%m-%d'))
    return days


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
    response = requests.get(Parameters.available_seats_url, headers=Parameters.headers, params={"dates": date, "sectorName": "AMALIAS"})

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

def make_my_booked_desks_request():
    """Make a GET request for a specific date."""
    response_future = requests.get(Parameters.my_booked_desks_url, headers=Parameters.headers)

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

def main():
    my_booked_desks = make_my_booked_desks_request()
    days = get_days_for_week()
    while True:
        data_found = False
        for date in days:
            print(f"Processing data for {date}")
            data = make_get_request(date)

            if data:
                print(f"Found data for {date}:")
                desk_item = {'code': data['code'], 'date': date}

                if (desk_item not in my_booked_desks):
                    message_title = "Desk available ..."
                    message_txt = f" Date {date}\n Floor {data['floor']}\n Desk {data['code']}\n "
                    email_txt = message_txt + f"\n \n {Parameters.planner_url}"
                    print(message_txt)

                    # --- when away from screen for all desks in amalias
                    # EmailSender.send_email(message_title, email_txt)
                    # show_notification_windows(message_title, message_txt)

                    # --- when on screen for all desks in amalias
                    show_notification_interacted(message_title, message_txt)
                    webbrowser.open_new(Parameters.planner_url)
                    EmailSender.send_email(message_title, email_txt)

                    # --- Specific Floor
                    #if (data['floor'] == "1st Floor"  or data['floor'] =="Mezzazine"):
                        # webbrowser.open_new(planner_url)
                        # EmailSender.send_email(message_title, email_txt)
                        # show_notification(message_title, message_txt)

                        # We are ok ... remove date not search again
                        # days.remove(date)

                    if BookDesk.post_seat(data['code'], date):
                        print(f"Desk {data['code']} booked for Date {date}  \n")
                        EmailSender.send_email("Booked", f"Desk {data['code']} booked for Date {date}  \n")

                else:
                    #already booked. no search again
                    print(f"Already booked for {date} will be removed from dates array \n")
                    days.remove(date)
            else:
                print(f"No data found for {date}\n ")

        if not days:
            print("All days processed with available data found.")
            break  # Exit the loop if all days have been processed successfully


        # Wait before checking again (e.g., 1 hour)
        print("Waiting for the next check...\n ---\n")
        time.sleep(5)  # Delay in seconds (3600 seconds = 1 hour)

if __name__ == "__main__":
    main()
