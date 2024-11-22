import requests
import json

from plyer import notification

from configuration_params import Parameters



def read_json_and_create_dict():
    json_file_path = "seats.json"
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        # Create a dictionary with 'code' as the key
        code_dict = {item["code"]: item for item in data}
        return code_dict

    except FileNotFoundError:
        print(f"Error: File not found at {json_file_path}")
    except KeyError:
        print("Error: 'code' field is missing in the JSON data.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please check the file format.")
    return None

# Function to send a PUT request
def send_put(desk_booking_id, put_data):
    # Additional headers to append
    additional_headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "text/plain;charset=UTF-8",
        "Referer": f"https://myplanner.netcompany-intrasoft.com/booking/{desk_booking_id}/edit",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }

    Parameters.headers.update(additional_headers)


    # Make the PUT request
    put_response = requests.put(Parameters.put_url.substitute(deskbookingid=desk_booking_id),
                                headers=Parameters.headers,
                                data=put_data)
    print(f"PUT Result :{put_response.text}")

    if (put_response.status_code not in [200, 204] or
            any(keyword in put_response.text.lower() for keyword in ['rejected', 'unauthorized'])):
        notification.notify(
            title="Update Failed",
            message=f"{put_response.text}",
            app_name="Data Alert",
            timeout=60  # Duration of the notification in seconds
        )
        return None
        # raise Exception(f"PUT request failed with status code {put_response.status_code}")

    notification.notify(
        title="Update Success !!!",
        message=f"{put_response.text} \n {put_response.text}",
        app_name="Data Alert",
        timeout=60  # Duration of the notification in seconds
    )
    return put_response

def book_seat(found_seat):
    seats_db =read_json_and_create_dict()
    if found_seat in seats_db:
       return seats_db[found_seat]
    else:
        print("Code not found in the dictionary.")

def get_my_booking_id(date):
    """Find desk_booking_id"""
    print(f"URL desk_booking_id: {Parameters.find_desk_booking_id_url}?fromDate={date}&toDate={date}")
    data = requests.get(Parameters.find_desk_booking_id_url, headers=Parameters.headers,
                        params={"fromDate": date, "toDate": date}).json()
    print("Desk Booking ID:", desk_booking_id)
    desk_booking_id = data[0].get("deskBookingId")


class BookDesk:
    def __init__(self, seat_code, date):
        self.seat = seat_code
        self.date = date

    def update_seat(seat_code, date):
        desk_value = book_seat(seat_code)
        if desk_value:
            code = desk_value['code']
            positionId = desk_value['positionId']
            facilityId = desk_value['facilityId']
            x = desk_value['x']
            y = desk_value['y']



            data_to_send = Parameters.put_template.substitute(date=date, positionId=positionId, facilityId=facilityId, x=x, y=y)
            response = send_put(desk_booking_id, data_to_send)
        else:
            return False

        return response.status_code == 200
