import json
import logging

logger = logging.getLogger(__name__)

class Parameters:
    AUTHOR= ""
    SITEURL=""
    SITEURL_OG=""
    SITE_LOGO=""
    SITENAME= ""
    SITESUBTITLE=""
    SITESUBTITLE_ESY=""
    HOME_COVER=""
    HOME_COVER_URL_OG=""
    HOME = ""
    SERVICES= ""
    KEYWORDS=""
    SITE_DESCRIPTION=""
    FACEBOOK_URL=""
    LINKEDIN_URL=""
    INSTAGRAM_URL=""

    @staticmethod
    def load_from_json(json_file):
        """Load parameters from the provided JSON file."""
        with open(json_file,  'r', encoding='utf-8') as file:
            config = json.load(file)

        Parameters.AUTHOR = config.get("AUTHOR", "")
        Parameters.SITEURL = config.get("SITEURL", "")
        Parameters.SITEURL_OG = config.get("SITEURL_OG", "")
        Parameters.SITE_LOGO = config.get("SITE_LOGO", "")
        Parameters.SITENAME = config.get("SITENAME", "")
        Parameters.SITESUBTITLE = config.get("SITESUBTITLE", "")
        Parameters.SITESUBTITLE_ESY = config.get("SITESUBTITLE_ESY", "")
        Parameters.HOME_COVER = config.get("HOME_COVER", "")
        Parameters.HOME_COVER_URL_OG = config.get("HOME_COVER_URL_OG", "")
        Parameters.HOME = config.get("HOME", "")
        Parameters.SERVICES= config.get("SERVICES", "")
        Parameters.KEYWORDS = config.get("KEYWORDS", "")
        Parameters.SITE_DESCRIPTION = config.get("SITE_DESCRIPTION", "")
        Parameters.FACEBOOK_URL = config.get("FACEBOOK_URL", "")
        Parameters.LINKEDIN_URL = config.get("LINKEDIN_URL", "")
        Parameters.INSTAGRAM_URL = config.get("INSTAGRAM_URL", "")


logger.info(f"load configuration: plugins/resources.json")
# Example usage
Parameters.load_from_json('plugins/resources.json')