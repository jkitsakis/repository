import requests
import json
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
    put_url = Parameters.put_url.substitute(deskbookingid=desk_booking_id)
    get_url =  Parameters.get_my_booking_details_url.substitute(deskbookingid=desk_booking_id)

    # Step 1: Create a session
    session = requests.Session()
    # Step 2: Make a GET request to retrieve the cookie
    get_response = session.get(get_url)
    # Check if the GET request was successful
    if get_response.status_code != 200:
        raise Exception(f"GET request failed with status code {get_response.status_code}")

    # Step 3: Extract the cookie
    cookies_dict = session.cookies.get_dict()  # Retrieve all cookies as a dictionary

    # Step 4: Include the cookie in the headers for the PUT request
    cookie_header = '; '.join([f"{key}={value}" for key, value in cookies_dict.items()])
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'text/plain',
        "Cookie": f"{cookie_header}"
    }
    # Step 5: Make the PUT request
    put_response = session.put(put_url, headers=headers, data=put_data)

    print(f"PUT Result :{put_response.text}")

    if put_response.status_code not in [200, 204]:
        raise Exception(f"PUT request failed with status code {put_response.status_code}")

    return put_response

def book_seat(found_seat):
    seats_db =read_json_and_create_dict()
    if found_seat in seats_db:
       return seats_db[found_seat]
    else:
        print("Code not found in the dictionary.")

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

            """Find desk_booking_id"""
            print(f"URL desk_booking_id: {Parameters.find_desk_booking_id_url}?fromDate={date}&toDate={date}")
            data = requests.get(Parameters.find_desk_booking_id_url, headers=Parameters.headers,
                                    params={"fromDate": date, "toDate": date}).json()
            desk_booking_id = data[0].get("deskBookingId")
            print("Desk Booking ID:", desk_booking_id)

            data_to_send = Parameters.put_template.substitute(date=date, positionId=positionId, facilityId=facilityId, x=x, y=y)
            response = send_put(desk_booking_id, data_to_send)
        else:
            return False

        return response.status_code == 200
