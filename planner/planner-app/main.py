from booking.planner_book import main_book
from availability.planner_available import main_avalilability
from configuration.configuration_params import Parameters

def call_booking_module():
    try:
        main_book()
    except Exception as e:
        print("An error occurred in the Booking Module:", e)


def call_availability_module():
    try:
        main_avalilability()
    except Exception as e:
        print("An error occurred in the Availability Module:", e)

def ask_for_cookie():
    print("Please paste the cookie you copied from the browser:")
    pasted_cookie = input("> ").strip()
    print("✅ Cookie received.\n---")
    return pasted_cookie

def replace_cookie_in_headers(cookie):
    # Inject cookie into parameters
    Parameters.cookie = cookie

    # Update headers dynamically
    Parameters.get_headers = {
        key: value.replace("cookie_placeholder", cookie) if isinstance(value, str) else value
        for key, value in Parameters.get_headers.items()
    }
    Parameters.post_headers = {
        key: value.replace("cookie_placeholder", cookie) if isinstance(value, str) else value
        for key, value in Parameters.post_headers.items()
    }
    Parameters.put_headers = {
        key: value.replace("cookie_placeholder", cookie) if isinstance(value, str) else value
        for key, value in Parameters.put_headers.items()
    }

def main():
    print("Which module would you like to run?")
    print("1. Booking Module")
    print("2. Availability Module")
    choice = input("Enter the number of your choice: ")

    cookie = Parameters.cookie if Parameters.cookie.strip() else ask_for_cookie()
    replace_cookie_in_headers(cookie)

    print("---")
    if choice == "1":
        call_booking_module()
    elif choice == "2":
        call_availability_module()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
