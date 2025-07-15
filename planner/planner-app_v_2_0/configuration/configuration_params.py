import json
from string import Template


class Parameters:
    dates = []
    parking_dates= []
    book_parking_slot= True
    seats_dir=""
    start_time=""
    sleep_in_availability=""
    sleep_in_parking_availability=""
    sleep_in_book=""
    cookie = ""
    planner_url = ""
    available_seats_url = ""
    my_booked_desks_url = ""
    available_parking_slots_url = ""
    find_desk_booking_id_url = ""
    put_url = Template("")
    post_url = ""
    referer_url = Template("")
    get_my_booking_details_url = Template("")
    get_headers = {}
    post_headers = {}
    put_headers = {}
    message_title_template=""
    message_txt_template=""
    mail_success_template=""

    @staticmethod
    def load_from_json(json_file):
        """Load parameters from the provided JSON file."""
        with open(json_file, 'r') as file:
            config = json.load(file)

        Parameters.dates = config.get("dates", [])
        Parameters.parking_dates = config.get("parking_dates", [])
        Parameters.book_parking_slot = config.get("book_parking_slot", False)
        Parameters.seats_dir = config.get("seats_dir", "")
        Parameters.start_time= config.get("start_time", "12:00:03.0000")
        Parameters.sleep_in_availability= config.get("sleep_in_availability", 10)
        Parameters.sleep_in_parking_availability = config.get("sleep_in_parking_availability", 1800)
        Parameters.sleep_in_book = config.get("sleep_in_book", 0.001)
        Parameters.cookie = config.get("cookie", "")
        Parameters.planner_url = config.get("planner_url", "")
        Parameters.available_seats_url = config.get("available_seats_url", "")
        Parameters.my_booked_desks_url = config.get("my_booked_desks_url", "")
        Parameters.available_parking_slots_url = config.get("available_parking_slots_url", "")
        Parameters.find_desk_booking_id_url = config.get("find_desk_booking_id_url", "")
        Parameters.put_url = Template(config.get("put_url", ""))
        Parameters.post_url = config.get("post_url", "")
        Parameters.referer_url = Template(config.get("referer_url", ""))
        Parameters.get_my_booking_details_url = Template(config.get("get_my_booking_details_url", ""))
        Parameters.get_headers =config.get("get_headers", "")
        Parameters.put_headers = config.get("put_headers", "")
        Parameters.post_headers = config.get("post_headers", "")
        Parameters.post_template = Template(config.get("post_template", ""))
        Parameters.post_template_parking = Template(config.get("post_template_parking", ""))
        Parameters.put_template = Template(config.get("put_template", ""))
        Parameters.put_template_parking = Template(config.get("put_template_parking", ""))
        Parameters.message_title_template = Template(config.get("message_title_template", ""))
        Parameters.message_txt_template = Template(config.get("message_txt_template", ""))
        Parameters.mail_success_template = Template(config.get("mail_success_template", ""))


# Example usage
Parameters.load_from_json('resources/config.json')