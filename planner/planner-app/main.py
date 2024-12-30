from booking.planner_book import main_book
from availability.planner_available import main_avalilability

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


def main():
    print("Which module would you like to run?")
    print("1. Booking Module")
    print("2. Availability Module")
    choice = input("Enter the number of your choice: ")
    print("---")
    if choice == "1":
        call_booking_module()
    elif choice == "2":
        call_availability_module()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
