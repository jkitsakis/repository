import json
from string import Template


class Parameters:
    dates = []
    start_time=""
    cookie = ""
    planner_url = ""
    available_seats_url = ""
    my_booked_desks_url = ""
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
    post_template=""
    put_template=""

    @staticmethod
    def load_from_json(json_file):
        """Load parameters from the provided JSON file."""
        with open(json_file, 'r') as file:
            config = json.load(file)

        Parameters.dates = config.get("dates", [])
        Parameters.start_time= config.get("start_time", "12:00:03.0000")
        Parameters.cookie = config.get("cookie", "")
        Parameters.planner_url = config.get("planner_url", "")
        Parameters.available_seats_url = config.get("available_seats_url", "")
        Parameters.my_booked_desks_url = config.get("my_booked_desks_url", "")
        Parameters.find_desk_booking_id_url = config.get("find_desk_booking_id_url", "")
        Parameters.put_url = Template(config.get("put_url", ""))
        Parameters.post_url = config.get("post_url", "")
        Parameters.referer_url = Template(config.get("referer_url", ""))
        Parameters.get_my_booking_details_url = Template(config.get("get_my_booking_details_url", ""))

        # Replace cookie placeholder
        cookie_value = Parameters.cookie
        Parameters.get_headers = {
            key: value.replace("cookie_placeholder", cookie_value) if isinstance(value, str) else value for key, value
            in config.get("get_headers", {}).items()}
        Parameters.put_headers = {
            key: value.replace("cookie_placeholder", cookie_value) if isinstance(value, str) else value for key, value
            in config.get("put_headers", {}).items()}
        Parameters.post_headers = {
            key: value.replace("cookie_placeholder", cookie_value) if isinstance(value, str) else value for key, value
            in config.get("post_headers", {}).items()}

        Parameters.post_template = Template(config.get("post_template", ""))
        Parameters.put_template = Template(config.get("put_template", ""))
        Parameters.message_title_template = Template(config.get("message_title_template", ""))
        Parameters.message_txt_template = Template(config.get("message_txt_template", ""))
        Parameters.mail_success_template = Template(config.get("mail_success_template", ""))


# Example usage
Parameters.load_from_json('config.json')