import requests
import json

from plyer import notification

from configuration.configuration_params import Parameters

def read_json_and_create_dict():
    json_file_path = "resources/seats-maroussi.json"
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

def book_seat(available_seat_code, date):
    seat_details = find_seat_details(available_seat_code)
    if seat_details:
        code = seat_details['code']
        positionId = seat_details['positionId']
        facilityId = seat_details['facilityId']
        x = seat_details['x']
        y = seat_details['y']

        data_to_send = Parameters.put_template.substitute(date=date,
                                                          code=code,
                                                          positionId=positionId,
                                                          facilityId=facilityId,
                                                          x=x,
                                                          y=y)
        booking_id = get_my_booking_id(date)

        if booking_id:
            put_response = send_put(booking_id, data_to_send)
            if (put_response['status_code'] != 200 or
                    any(keyword in put_response['text'].lower() for keyword in ['rejected', 'unauthorized'])):
                notification.notify(
                    title=f"Update Failed (Status: {put_response['status_code']})",
                    message=f"Error: {put_response['text']} ",
                    app_name="Data Alert",
                    timeout=60  # Duration of the notification in seconds
                )
                print(f"Error: {put_response['status_code']} - {put_response['text']} ")
                return False
                # raise Exception(f"PUT request failed with status code {put_response.status_code}")
            else:
                print(f"Desk booked: {code}")
                notification.notify(
                    title="Update Success !!!",
                    message=f"Success: {put_response['text']} (Status: {put_response['status_code']})",
                    app_name="Data Alert",
                    timeout=60  # Duration of the notification in seconds
                )
                print(f"Success: {put_response['status_code']} - {put_response['text']}")
                return True
        else:
            print(f"No booking_id Found for {date}")
            return False
    else:
        print(f"No seat_details Found for {date}")
        return False



class UpdateDesk:
    def __init__(self, seat_code, date):
        self.seat = seat_code
        self.date = date

    def book_seat(availale_seat_code, date):
        return book_seat(availale_seat_code, date)


    def get_my_booking_id(date):
        return get_my_booking_id(date)
