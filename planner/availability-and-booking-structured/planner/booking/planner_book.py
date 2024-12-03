import concurrent.futures
import json
import random
import threading
import time
from datetime import datetime

import requests

from configuration.configuration_params import Parameters


def pick_random_seat(file_path):
    try:
        # Open and load the JSON file
        with open(file_path, 'r') as file:
            seats = json.load(file)

        # Check if the list is not empty
        if not seats:
            raise ValueError("The JSON list is empty.")

        # Extract weights
        weights = [obj['weight'] for obj in seats]

        # Make a weighted random choice
        random_seat = random.choices(seats, weights=weights, k=1)[0]
        # Select a random object from the list
        # random_seat = random.choice(seats)
        return random_seat

    except FileNotFoundError:
        print(f"File not found: {file_path} \n")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {file_path} \n")
    except Exception as e:
        print(f"An error occurred: {e} \n")


lock = threading.Lock()

def post_request(json_object):
    with lock: # ensure only one request is processed at a time
        try:
            response = requests.post(Parameters.post_url, data=json_object, headers=Parameters.post_headers)
            return {
                "status_code": response.status_code,
                "json": response.json() if response.content else None,
                "data": json_object
            }
        except requests.RequestException as e:
            return {"error": str(e), "data": json_object}

def post_json_in_parallel(json_list, max_workers):
    # Use ThreadPoolExecutor to post in parallel
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers) as executor:
        future_to_json = {executor.submit(post_request, json_obj): json_obj for json_obj in json_list}
        for future in concurrent.futures.as_completed(future_to_json):
            results.append(future.result())

    return results

def prepare_json_list(days):
    json_list=[]
    for day in days:
        random_seat = pick_random_seat("resources/seats.json")
        json= Parameters.post_template.substitute(date=day,
                                                  code=random_seat['code'],
                                                  positionId=random_seat['positionId'],
                                                  facilityId=random_seat['facilityId'],
                                                  x=random_seat['x'],
                                                  y=random_seat['y'])
        json_list.append(json)

    return json_list

def start_post():
    start_time = time.time()
    days = Parameters.dates
    while days:
        start_time_parallel = time.time()
        desk_list = prepare_json_list(days)
        responses = post_json_in_parallel(desk_list, 5)
        for response in responses:
            print(f"{response} \n")
            data_str = response.get('data', '')
            data_dict = json.loads(data_str)
            date = data_dict['dates'][0]
            if response['status_code'] == 200:
                days.remove(date)

        end_time_parallel = time.time()
        execution_time_parallel = end_time_parallel - start_time_parallel
        print(f"Execution Time parallel call: {execution_time_parallel:.3f} seconds \n")
        if not days:
            print("All days processed with available data found.")
            break  # Exit the loop if all days have been processed successfully

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution Time: {execution_time:.3f} seconds \n")

def main_book():
    target_time = Parameters.start_time
    while True:
        # Get the current time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S.%f")[:-2]  # Match format to "12:00:00.0000"
        if current_time >= target_time:
            print(f"Execution Time: {current_time}\n")
            start_post()
            break  # Exit loop after execution

        time.sleep(Parameters.sleep_in_book)  # Sleep for 1 ms to mini






