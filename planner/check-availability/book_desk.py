from string import Template

import requests
import json

# Define the URL to send requests to
url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking"
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'Path=/; Path=/; Path=/; _ga=GA1.1.2086248922.1725605193; _ga_PV0JVKBGJ5=GS1.1.1728549146.3.1.1728549241.0.0.0; TS00000000076=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4109d0002c414daca58a0b699f46146bcbde638c98ad92ed06571e023144e38b763b9466c6b7bf992381b930f3125a803c7b3e4e3bda2704b04d7c23c1bf8fbb57c98046742f4ddb9b2e79b8514879e75568ac15d179109caeaebf3e0a82af0718e8372c5870af9f96c815662ae274527f65aa5e977b4fd7820b34da5938db370b9138f90138be50d7c51564be260b2d32c0e4ddf82d17a7bef6a7fd0ca61788d469ad71428bf9c346073af2a64d77d44810d7005e3f11a26b0480f6b76c05f82fc5a4bfb36cb5f3ee07a899697550a1a8ae6d59; TSPD_101_DID=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4106380090e31c1c8fd8def8622a1c50a3e582f0eafd739bc15ef7424e7b0df059e5eb21ab4ad20ffe6c716dfc942ac32212737c2234ecd3605f0866; JSESSIONID=C11A8B713C466DC8FDE84169ABB5773D; TS010ee64b=01eb1053a04f096b9cc56502285e9d3707b1549f575ca8e7837d26ed3960ec09baf8b17fe48df2d5e18f110bdfb23bc6461b1e1ced8e611facb0cfa503ff21ea3a3753ef74686fe2eb3d57d1309e31dfe4e55f6b31; TSf455e12a027=0804a8c53bab2000475ef965071ca89e8716e7fce2c99bcfd73ba02e5d6ec9fe2e666e1576f8768208bdf5807211300046288872c5fecdae07aaf4d432dac2ae67c590a903c06f32344ee4814de95f7eb4d2c9d970b222a248075b9ecd31cf4f',  # Change this to your actual token if needed
}
template = Template("{\"dates\":[\"$date\"],\"facilityId\":\"$facilityId\",\"positionId\":\"$positionId\",\"x\":$x,\"y\":$y,\"code\":\"$code\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"$date\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}")


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

# Example usage:
# Assuming the JSON file contains a list of dictionaries.
# json_file_path = "data.json"
# result = read_json_and_create_dict(json_file_path)
# print(result)


# Function to send a POST request
def send_post(data):
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.status_code
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

    def post_seat(self):
        desk_value = book_seat(self.seat)
        print(f"desk positionId:{desk_value}")
        print(f"desk positionId:{desk_value['code']}")

        code = desk_value['code']
        positionId = desk_value['positionId']
        facilityId = desk_value['facilityId']
        x = desk_value['x']
        y = desk_value['y']

        data_to_send = template.substitute(date=self.date, code=code, positionId=positionId, facilityId=facilityId, x=x, y=y)
        response = requests.post(url, json=data_to_send, headers=headers)
        # Print the response
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())

        return response.status_code == 200
