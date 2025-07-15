import time
import requests

from configuration.configuration_params import Parameters
from utilities.update_booking import book_seat_parking, get_booking_details, show_notification_windows
from utilities.send_email import EmailSender


def process_exist_available_internal_parking_slots_response(response):
    """Process the JSON response to extract the required data."""
    parking_types = response[0]["parkingTypeList"]

    # Find capacity for type "Internal"
    internal_capacity = next(
        (p.get("capacity", 0) for p in parking_types if p.get("type") == "Internal"),
        0
    )

    print("Internal capacity:", internal_capacity)
    return internal_capacity

def get_exist_available_internal_parking_slots_request(date):
    """Make a GET request for a specific date to check available internal slots."""
    url = Parameters.available_parking_slots_url
    headers = Parameters.get_headers
    params = {
        "dates": date,
        "facilityId": "64a41c5241d4b80382ab638b",
        "facilitySectorName": "MAROUSSI"
    }
    # print("Request URL:",  f"{url}?{params}")
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        response_data = response.json()
        return process_exist_available_internal_parking_slots_response(response_data)
    else:
        print(f"Request failed for {date} with status code {response.status_code}")
        return None


def process_my_bookings(response):
    # Return a list of all booking dicts
    return response.get("deskBookings", [])


def get_my_bookings():
    response_future = requests.get(Parameters.my_booked_desks_url, headers=Parameters.get_headers)
    if response_future.status_code == 200:
        response_data_future = response_future.json()
        return process_my_bookings(response_data_future)
    return []



def parking_avalilability():
    days = Parameters.parking_dates
    while True:
        try:
            my_bookings = get_my_bookings()  # <-- Now a list of bookings
            for date in days:
                print(f"Processing for {date} ...")
                exist_available_internal_parking_slots = get_exist_available_internal_parking_slots_request(date)

                if exist_available_internal_parking_slots is not None and exist_available_internal_parking_slots > 0 :
                    print(f"Found internal parking slot for {date}")
                    show_notification_windows("Internal Parking Found !!!", f"Found internal parking slot for {date}")
                    # Get the booking for the current date
                    booking = next((b for b in my_bookings if b.get("date") == date), None)

                    if (booking and
                            booking['sectorName']== "MAROUSSI" and
                            booking.get("parkingStatus") != "REQUESTED" and
                            book_seat_parking(booking['code'], date, True)) :

                        result = get_booking_details(booking)
                        EmailSender.send_email(f"Parking Slot {result.get("parkingNumber")} Booked" ,
                                               f"Parking Slot {result.get("parkingNumber")} Booked. \n \n {Parameters.planner_url}")
                    else:
                        print(f"No Valid Booking for Parking Assignment found for date {date}")
                        print(f"id: {booking['id']}")
                        print(f"parkingStatus: {booking['parkingStatus']} \n")

                else:
                    print(f"No Available parking slots for {date} ")

            # Wait before checking again
            print("Waiting for the next check...\n ---")
            time.sleep(Parameters.sleep_in_parking_availability)
        except Exception as e:
            print(f"Connection refused by the server..")
            print(f"Original cause: {e}\n")
            print("Let me sleep for 5 seconds")
            time.sleep(5)
            print(f"Was a nice sleep, now let me continue...\n")
            continue

