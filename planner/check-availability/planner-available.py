import time
import requests
import datetime
import ctypes
import webbrowser
from plyer import notification

from send_email import EmailSender
from book_desk import BookDesk

planner_url = "https://myplanner.netcompany-intrasoft.com"
available_seats_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/facility/facilities/available/map"
my_booked_desks_url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking/future?page=0&size=15"

# Define the headers for the GET request
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'Path=/; Path=/; Path=/; _ga=GA1.1.2086248922.1725605193; _ga_PV0JVKBGJ5=GS1.1.1728549146.3.1.1728549241.0.0.0; TS00000000076=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4109d0002c414daca58a0b699f46146bcbde638c98ad92ed06571e023144e38b763b9466c6b7bf992381b930f3125a803c7b3e4e3bda2704b04d7c23c1bf8fbb57c98046742f4ddb9b2e79b8514879e75568ac15d179109caeaebf3e0a82af0718e8372c5870af9f96c815662ae274527f65aa5e977b4fd7820b34da5938db370b9138f90138be50d7c51564be260b2d32c0e4ddf82d17a7bef6a7fd0ca61788d469ad71428bf9c346073af2a64d77d44810d7005e3f11a26b0480f6b76c05f82fc5a4bfb36cb5f3ee07a899697550a1a8ae6d59; TSPD_101_DID=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4106380090e31c1c8fd8def8622a1c50a3e582f0eafd739bc15ef7424e7b0df059e5eb21ab4ad20ffe6c716dfc942ac32212737c2234ecd3605f0866; JSESSIONID=0CBC02C4AC845EF525F3C49A21115865; TS010ee64b=01eb1053a06986da9e0e299f176fb51d0d3fc4fad35e9ab976fed1310a7ecf37f62d83669e83d769e5d5f394a4c0dd80c371bd8adbccee5dace37b32f56d07ed635c7d2bc6397070303a2c9fc3679d0ac153c518de; TSf455e12a027=0804a8c53bab20002ae5fbe5591bf95371d77f48129a874f2aa422741c69a9788870759c631c3e4d08e768a11b113000d2d44fb1c9ad9663e86ff21ea4194585c1d55f0573642a7db52c5b7dcb66cb38b144590eecb391d6eddfd6847478251a'

}

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
    response = requests.get(available_seats_url, headers=headers, params={"dates": date, "sectorName": "AMALIAS"})

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
    response_future = requests.get(my_booked_desks_url, headers=headers)

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
                    email_txt = message_txt + f"\n \n {planner_url}"
                    print(message_txt)

                    # --- when away from screen for all desks in amalias
                    # EmailSender.send_email(message_title, email_txt)
                    # show_notification_windows(message_title, message_txt)

                    # --- when on screen for all desks in amalias
                    show_notification_interacted(message_title, message_txt)
                    webbrowser.open_new(planner_url)
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
