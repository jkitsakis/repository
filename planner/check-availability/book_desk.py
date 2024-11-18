from string import Template

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

# Function to send a POST request
def send_put(data):
    try:
        response = requests.put(Parameters.book_url, json=data, headers=Parameters.headers)
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

    def post_seat(seat_code, date):
        desk_value = book_seat(seat_code)
        if desk_value:
            code = desk_value['code']
            positionId = desk_value['positionId']
            facilityId = desk_value['facilityId']
            x = desk_value['x']
            y = desk_value['y']

            data_to_send = Parameters.put_template.substitute(date=date, code=code, positionId=positionId, facilityId=facilityId, x=x, y=y)
            response = send_put(data_to_send)
            # Print the response
            print("Response:", response)
            print(f"Status Code: {response.status_code}")
            print("Response JSON:", response.json())
        else:
            return False

        return response.status_code == 200
