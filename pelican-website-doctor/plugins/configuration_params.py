import json


class Parameters:
    AUTHOR= ""
    SITEURL=""
    SITENAME= ""
    SITESUBTITLE=""
    SITESUBTITLE_ESY=""
    HOME = ""
    SERVICES= ""
    KEYWORDS=""
    SITE_DESCRIPTION=""

    @staticmethod
    def load_from_json(json_file):
        """Load parameters from the provided JSON file."""
        with open(json_file,  'r', encoding='utf-8') as file:
            config = json.load(file)

        Parameters.AUTHOR = config.get("AUTHOR", "")
        Parameters.SITEURL = config.get("SITEURL", "")
        Parameters.SITENAME = config.get("SITENAME", "")
        Parameters.SITESUBTITLE = config.get("SITESUBTITLE", "")
        Parameters.SITESUBTITLE_ESY = config.get("SITESUBTITLE_ESY", "")
        Parameters.HOME = config.get("HOME", "")
        Parameters.SERVICES= config.get("SERVICES", "")
        Parameters.KEYWORDS = config.get("KEYWORDS", "")
        Parameters.SITE_DESCRIPTION = config.get("SITE_DESCRIPTION", "")

# Example usage
Parameters.load_from_json('plugins/resources.json')