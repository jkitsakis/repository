import requests
import concurrent.futures
import time

# Define the URL to send requests to
url = "https://httpbin.org/post"  # Change this to your target URL

headers = {
    'Content-Type': 'application/json',
    'Cookie': 'Path=/; Path=/; Path=/; _ga=GA1.1.2086248922.1725605193; _ga_PV0JVKBGJ5=GS1.1.1728549146.3.1.1728549241.0.0.0; TS00000000076=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4109d0002c414daca58a0b699f46146bcbde638c98ad92ed06571e023144e38b763b9466c6b7bf992381b930f3125a803c7b3e4e3bda2704b04d7c23c1bf8fbb57c98046742f4ddb9b2e79b8514879e75568ac15d179109caeaebf3e0a82af0718e8372c5870af9f96c815662ae274527f65aa5e977b4fd7820b34da5938db370b9138f90138be50d7c51564be260b2d32c0e4ddf82d17a7bef6a7fd0ca61788d469ad71428bf9c346073af2a64d77d44810d7005e3f11a26b0480f6b76c05f82fc5a4bfb36cb5f3ee07a899697550a1a8ae6d59; TSPD_101_DID=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4106380090e31c1c8fd8def8622a1c50a3e582f0eafd739bc15ef7424e7b0df059e5eb21ab4ad20ffe6c716dfc942ac32212737c2234ecd3605f0866; JSESSIONID=C11A8B713C466DC8FDE84169ABB5773D; TS010ee64b=01eb1053a04f096b9cc56502285e9d3707b1549f575ca8e7837d26ed3960ec09baf8b17fe48df2d5e18f110bdfb23bc6461b1e1ced8e611facb0cfa503ff21ea3a3753ef74686fe2eb3d57d1309e31dfe4e55f6b31; TSf455e12a027=0804a8c53bab2000475ef965071ca89e8716e7fce2c99bcfd73ba02e5d6ec9fe2e666e1576f8768208bdf5807211300046288872c5fecdae07aaf4d432dac2ae67c590a903c06f32344ee4814de95f7eb4d2c9d970b222a248075b9ecd31cf4f',  # Change this to your actual token if needed

}

# Data to be sent in each request
data_list = [
    {'data': '{\"dates\": [\"2024-11-18\"], \"facilityId\": \"6448cee7bf530c0226ea4d4d\", \"positionId\": \"6448cee7bf530c0226ea4d55\", \"x\": 1225, \"y\": 1504, \"code\": \"008\", \"parking\": [{\"parkingRequested\": false, \"plateNumber\": \"\", \"type\": \"All\"}], \"datesAndType\": [{\"date\": \"2024-11-11\", \"type\": \"0036\", \"clientName\": \"\", \"clientAddress\": \"\"}]}'},
    {'data': '{\"dates\": [\"2024-11-19\"], \"facilityId\": \"6448cee7bf530c0226ea4d4d\", \"positionId\": \"6448cee7bf530c0226ea4d55\", \"x\": 1225, \"y\": 1504, \"code\": \"008\", \"parking\": [{\"parkingRequested\": false, \"plateNumber\": \"\", \"type\": \"All\"}], \"datesAndType\": [{\"date\": \"2024-11-11\", \"type\": \"0036\", \"clientName\": \"\", \"clientAddress\": \"\"}]}'},
    {'data': '{\"dates\": [\"2024-11-20\"], \"facilityId\": \"6448cee7bf530c0226ea4d4d\", \"positionId\": \"6448cee7bf530c0226ea4d55\", \"x\": 1225, \"y\": 1504, \"code\": \"008\", \"parking\": [{\"parkingRequested\": false, \"plateNumber\": \"\", \"type\": \"All\"}], \"datesAndType\": [{\"date\": \"2024-11-11\", \"type\": \"0036\", \"clientName\": \"\", \"clientAddress\": \"\"}]}'},
    {'data': '{\"dates\": [\"2024-11-21\"], \"facilityId\": \"6448cee7bf530c0226ea4d4d\", \"positionId\": \"6448cee7bf530c0226ea4d55\", \"x\": 1225, \"y\": 1504, \"code\": \"008\", \"parking\": [{\"parkingRequested\": false, \"plateNumber\": \"\", \"type\": \"All\"}], \"datesAndType\": [{\"date\": \"2024-11-11\", \"type\": \"0036\", \"clientName\": \"\", \"clientAddress\": \"\"}]}'},
    {'data': '{\"dates\": [\"2024-11-22\"], \"facilityId\": \"6448cee7bf530c0226ea4d4d\", \"positionId\": \"6448cee7bf530c0226ea4d55\", \"x\": 1225, \"y\": 1504, \"code\": \"008\", \"parking\": [{\"parkingRequested\": false, \"plateNumber\": \"\", \"type\": \"All\"}], \"datesAndType\": [{\"date\": \"2024-11-11\", \"type\": \"0036\", \"clientName\": \"\", \"clientAddress\": \"\"}]}'}
]


# Function to send a POST request
def send_post(data):
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.status_code
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


# Main function to send requests in parallel
def main():
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_data = {executor.submit(send_post, data): data for data in data_list}

        while future_to_data:
            for future in list(future_to_data):
                data = future_to_data[future]
                try:
                    status_code = future.result()
                    if status_code == 200:
                        print(f"Request with data {data} completed with status {status_code}. Not sending again.")
                        del future_to_data[future]
                        print(f"Length of remaining requests: {len(future_to_data)}")
                    else:
                        print(f"Request with data {data} failed with status {status_code}. Retrying...")
                        # Optionally, resubmit the failed request
                        future_to_data[executor.submit(send_post, data)] = data
                except Exception as e:
                    print(f"Request with data {data} generated an exception: {e}")
                    del future_to_data[future]

            # Wait a moment before checking responses again
            time.sleep(1)
    end_time = time.time()  # End timer
    execution_time = end_time - start_time  # Calculate total time
    print(f"Total execution time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    main()
