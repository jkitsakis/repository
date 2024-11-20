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
def send_put(desk_booking_id, payload, cookies_dict):
    # Update the Cookie header
    cookie_header = '; '.join([f"{key}={value}" for key, value in cookies_dict.items()])
    Parameters.headers["Cookie"] = cookie_header

    put_url = Parameters.put_url.substitute(deskbookingid=desk_booking_id)
    Parameters.headers["Referer"] = Parameters.referer_put_url.substitute(deskbookingid=desk_booking_id)

    print(f"Update Desk... \n")
    print(f"URL : {put_url}\n")
    print(f"Headers : {Parameters.headers}'\n")
    print(f"Payload: {payload}\n")
    print(type(f"Payload type: {payload}\n"))  # Should be <class 'dict'> if using json=
    print(f"Cookies: {cookies_dict}\n")
    # json=json.loads(data)
    try:
        response = requests.put(put_url, data= payload, headers=Parameters.headers)
        print(f"Request  Headers:{response.request.headers}\n")
        print(f"Request  Body: {response.request.body}\n")
        print(f"Response:{response.text}\n")
        print(f"Response cookies : {response.cookies}\n")
        print(f"Status Code: {response.status_code}")
        return response
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

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
            response_bookingId = requests.get(Parameters.find_desk_booking_id_url, headers=Parameters.headers,
                                    params={"fromDate": date, "toDate": date})
            data_bookingId = response_bookingId.json()
            desk_booking_id = data_bookingId[0].get("deskBookingId")
            print("Desk Booking ID:", desk_booking_id)

            # make this call because of referer header and get cookies
            response_referer = requests.get(Parameters.referer_put_url.substitute(deskbookingid=desk_booking_id))
            print(f"Response Referer:{response_referer.text}\n")
            print(f"Response Referer cookies : {response_referer.cookies}\n")
            print(f"Referer Status Code: {response_referer.status_code}")
            cookies_dict = requests.utils.dict_from_cookiejar(response_referer.cookies)

            data_to_send = Parameters.put_template.substitute(date=date, positionId=positionId, facilityId=facilityId, x=x, y=y)
            response = send_put(desk_booking_id, data_to_send, cookies_dict)
        else:
            return False

        return response.status_code == 200
