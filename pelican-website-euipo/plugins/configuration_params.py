import json
import logging
import os

logger = logging.getLogger(__name__)

class Parameters:
    LOCAL_BUILD = ""
    SITEURL=""
    SITEURL_GITHUB=""

    @staticmethod
    def load_from_json(json_file):
        """Load parameters from the provided JSON file."""
        with open(json_file,  'r', encoding='utf-8') as file:
            config = json.load(file)

        Parameters.LOCAL_BUILD = config.get("LOCAL_BUILD", "")
        Parameters.SITEURL_GITHUB = config.get("SITEURL_GITHUB", "")
        Parameters.SITEURL = config.get("SITEURL", "")

logger.info(f"load configuration: resources.json")
# Example usage
Parameters.load_from_json(os.path.join(os.path.dirname(__file__), 'resources.json'))