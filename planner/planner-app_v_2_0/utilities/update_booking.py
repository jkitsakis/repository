import requests
import json

from plyer import notification

from configuration.configuration_params import Parameters

def read_json_and_create_dict():
    try:
        with open(Parameters.seats_dir, 'r') as file:
            data = json.load(file)

        # Create a dictionary with 'code' as the key
        code_dict = {item["code"]: item for item in data}
        return code_dict

    except FileNotFoundError:
        print(f"Error: File not found at {Parameters.seats_dir}")
    except KeyError:
        print("Error: 'code' field is missing in the JSON data.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please check the file format.")
    return None

# Function to send a PUT request
def send_put(desk_booking_id, put_data):
    # Additional headers to append
    additional_headers = {
        "Referer": f"https://myplanner.netcompany-intrasoft.com/booking/{desk_booking_id}/edit"
    }
    Parameters.put_headers.update(additional_headers)
    headers = Parameters.put_headers
    # Make the PUT request
    response = requests.put(Parameters.put_url.substitute(deskbookingid=desk_booking_id),
                            headers=headers,
                            data=put_data)
    put_response= {
        "status_code": response.status_code,
        "data": put_data,
        "text": response.text
    }
    return put_response

def find_seat_details(availale_seat_code):
    seats_db =read_json_and_create_dict()
    if availale_seat_code in seats_db:
       return seats_db[availale_seat_code]
    else:
        print("Code not found in the dictionary.")

def get_my_booking_id(date):
    data = requests.get(Parameters.find_desk_booking_id_url, headers=Parameters.get_headers,
                        params={"fromDate": date, "toDate": date}).json()
    if data:
        return data[0].get("deskBookingId")
    else:
        return None

def get_booking_details(booking):
    fields = [
        "id", "date", "city", "sectorName", "floor", "code", "duringDrawPeriod",
        "parkingStatus", "parkingNumber", "parkingSupported",
        "externalParkingSupported", "parkingType", "plateNumber"
    ]
    return {field: booking.get(field) for field in fields}

def show_notification_windows(title, message):
    """Display a system notification on Windows."""
    notification.notify(
        title=title,
        message=message,
        app_name="Data Alert",
        timeout=60  # Duration of the notification in seconds
    )


def book_seat_parking(available_seat_code, date, parking_book=False):
    seat_details = find_seat_details(available_seat_code)
    if seat_details:
        # Prepare the base payload
        parameters_to_send = {
            "date": date,
            "code": seat_details['code'],
            "positionId": seat_details['positionId'],
            "facilityId": seat_details['facilityId'],
            "x": seat_details['x'],
            "y": seat_details['y'],
            "parkingRequested": 'true' if Parameters.book_parking_slot else 'false',
            "plateNumber": "ZNK3510" if Parameters.book_parking_slot else "",
            "type": "Internal" if (Parameters.book_parking_slot and parking_book) else "All"
        }
        data_to_send = Parameters.put_template_parking.substitute(**parameters_to_send)

        booking_id = get_my_booking_id(date)
        if booking_id:
            put_response = send_put(booking_id, data_to_send)
            if (put_response['status_code'] != 200 or
                    any(keyword in put_response['text'].lower() for keyword in ['rejected', 'unauthorized'])):
                show_notification_windows(f"Update Failed (Status: {put_response['status_code']})", f"Error: {put_response['text']} ")
                print(f"Error: {put_response['status_code']} - {put_response['text']}")
                return False
            else:
                print(f"Planner book: {seat_details['code']}")
                show_notification_windows("Planner book: !!!",
                                          f"Success: {put_response['text']} (Status: {put_response['status_code']})")
                print(f"Success: {put_response['status_code']} - {put_response['text']}")
                return True
        else:
            print(f"No booking_id Found for {date}")
            return False
    else:
        print(f"No seat_details Found for {date}")
        return False

