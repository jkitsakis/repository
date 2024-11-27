import time
from datetime import datetime, timedelta

import requests
import ctypes
import webbrowser
from plyer import notification

from send_email import EmailSender
from update_desk import UpdateDesk

from configuration_params import Parameters

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
    response = requests.get(Parameters.available_seats_url, headers=Parameters.put_headers, params={"dates": date, "sectorName": "AMALIAS"})

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
    response_future = requests.get(Parameters.my_booked_desks_url, headers=Parameters.put_headers)

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
    today = datetime.now().strftime('%Y-%m-%d')
    # today = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    print(f"Processing data for {today}")

    while True:
        available_desk = make_get_request(today)
        print(f"There is desk  {available_desk['code']}")

        # if available_desk and (available_desk['floor'] == '1st Floor' or available_desk['floor'] == 'Mezzazine'):
        if available_desk and available_desk['floor'] == 'Mezzazine':
            print(f"Found data for {today}:")

            message_title = Parameters.message_title_template.substitute(date=today, floor=available_desk['floor'])
            message_txt = Parameters.message_txt_template.substitute(date=today, floor=available_desk['floor'],
                                                                     code=available_desk['code'])
            email_txt = message_txt + f"\n \n {Parameters.planner_url}"

            show_notification_windows(message_title, message_txt)
            # EmailSender.send_email(message_title, email_txt)
            if UpdateDesk.book_seat(available_desk['code'], today):
                message_success = Parameters.mail_success_template.substitute(date=today,
                                                                              floor=available_desk['floor'], code=available_desk['code'])
                print(message_success)
                EmailSender.send_email("Booked", message_success)
            break

        print("Waiting for the next check...\n ---\n")
        time.sleep(5)  # Delay in seconds (3600 seconds = 1 hour)





if __name__ == "__main__":
    #Get my booked desks
    #For each day :
        #Step 1. find available desks by day. Get response
        #Step 2. process response to find desk pameters ids etc ...
        #Step 3. Desk FOUND
            #Step 3.1. if the desk is already booked by me
                #Step 3.1.1. Check if is located in 2nd or 3rd floor
                    #Step 3.1.2 Yes -> LOOP
                    #Step 3.1.3 No -> On screen notification, email , post , remove the day from the days to search
            #Step 3.2 remove the day from the days to search - Desk located on 1st floor or mezzazine
        #Step 4. Desk Not Found. Continue to next day

    main()
