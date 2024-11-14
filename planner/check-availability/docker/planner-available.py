import time
import requests
import datetime
import ctypes

url = "https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/facility/facilities/available/map"


# Define the headers for the GET request
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'Path=/; Path=/; Path=/; _ga=GA1.1.2086248922.1725605193; _ga_PV0JVKBGJ5=GS1.1.1728549146.3.1.1728549241.0.0.0; TS00000000076=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4109d0002c414daca58a0b699f46146bcbde638c98ad92ed06571e023144e38b763b9466c6b7bf992381b930f3125a803c7b3e4e3bda2704b04d7c23c1bf8fbb57c98046742f4ddb9b2e79b8514879e75568ac15d179109caeaebf3e0a82af0718e8372c5870af9f96c815662ae274527f65aa5e977b4fd7820b34da5938db370b9138f90138be50d7c51564be260b2d32c0e4ddf82d17a7bef6a7fd0ca61788d469ad71428bf9c346073af2a64d77d44810d7005e3f11a26b0480f6b76c05f82fc5a4bfb36cb5f3ee07a899697550a1a8ae6d59; TSPD_101_DID=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4106380090e31c1c8fd8def8622a1c50a3e582f0eafd739bc15ef7424e7b0df059e5eb21ab4ad20ffe6c716dfc942ac32212737c2234ecd3605f0866; JSESSIONID=0CBC02C4AC845EF525F3C49A21115865; TS010ee64b=01eb1053a029f9639750b82a2855e0072b42a602e8be12fc94c35fe2d773006b5f7ff903dd7a7c1c8fb371b3ef9ff7c68059d1769160c2571965ab35c1338fdd10ed7470fe249b1c270a9497561d8b02648d879039; TSf455e12a027=0804a8c53bab20009b6cb920b95e117f354cf70c67289551357acd83534a9545d0464c271231b9e508a3602ff41130005e5aaaadcf61fcb0d88b8600ba578a65d0e69933244bdaf03772121ba68b98729b092e517f4357d3d80ad419761f5a90'

}

def get_tomorrow_date():
    """Returns tomorrow's date."""
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    return tomorrow.strftime('%Y-%m-%d')


def get_days_for_week():
    """Returns the list of dates from tomorrow until Friday."""
    today = datetime.datetime.now()
    days = []
    # Get dates from tomorrow till Friday (5 days in total)
    for i in range(1, 9):
        day = today + datetime.timedelta(days=i)
        # Only include weekdays (Monday = 0, Sunday = 6)
        if day.weekday() < 5:
            days.append(day.strftime('%Y-%m-%d'))
    return days


def process_response(response):
    """Process the JSON response to extract the required data."""
    if "AMALIAS" in response:
        for floor in response["AMALIAS"]:
            if floor.get("positionDtoList"):
                floorInResposnse = floor.get("floor")
                position = floor["positionDtoList"][0]  # Get first element in positionDtoList
                # Extract required data if available
                if "floor" in floor and "id" in position and "x" in position and "y" in position and "code" in position and "available" in position:
                    return {
                        "floor": floorInResposnse,
                        "id": position["id"],
                        "x": position["x"],
                        "y": position["y"],
                        "code": position["code"],
                        "available": position["available"]
                    }
    return None


def make_get_request(date):
    """Make a GET request for a specific date."""
    response = requests.get(url, headers=headers, params={"dates": date,"sectorName":"AMALIAS"})

    if response.status_code == 200:
        response_data = response.json()
        return process_response(response_data)
    else:
        print(f"Request failed for {date} with status code {response.status_code}")
        return None

def show_notification(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)


def main():
    # Get tomorrow's date and days for the rest of the week (till Friday)
    days = get_days_for_week()
    while True:
        data_found = False
        for date in days:
            print(f"Processing data for {date}")
            data = make_get_request(date)

            if data:
                print(f"Found data for {date}:")
                print(
                    f"Floor: {data['floor']}, X: {data['x']}, Y: {data['y']}, Code: {data['code']}, Available: {data['available']}\n")
                show_notification("Desk available ...", f" Date {date}\n\n Floor {data['floor']}\n\n Desk {data['code']}\n\n ")

                # specific floor
                #----------------------------------------
                if (data['floor'] == "1st Floor"  or data['floor'] =="Mezzazine"):
                    days.remove(date)
            else:
                print(f"No data found for {date}\n")

        if not days:
            print("All days processed with available data found.")
            break  # Exit the loop if all days have been processed successfully


        # Wait before checking again (e.g., 1 hour)
        print("Waiting for the next check...")
        time.sleep(5)  # Delay in seconds (3600 seconds = 1 hour)

if __name__ == "__main__":
    main()
