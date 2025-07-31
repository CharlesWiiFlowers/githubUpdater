from mod.settings import load_settings
import warnings
from json import JSONDecodeError
from mod.custom_exceptions import InvalidSettingsError

class Main():
    """Main class for the GHUpdateChecker package."""

    def __init__(self):
        """Initialize the Main class."""

        # Load settings from the JSON file
        try:
            settings = load_settings()

            self.ghUsername = settings[0]
            self.ghRepo = settings[1]
            self.runFile = settings[2]
            self.rootProject = settings[3]
            self.currentVersion = settings[4]
            self.debug = settings[5]
            self.whitelist = settings[6]

        except FileNotFoundError:
            #TODO: Add a autocreation of the settings file if it does not exist
            raise InvalidSettingsError("GHUpdateSettings.json not found. Please ensure it exists in the correct directory.")
        except JSONDecodeError:
            raise InvalidSettingsError("Error decoding GHUpdateSettings.json. Please ensure it is valid JSON.")