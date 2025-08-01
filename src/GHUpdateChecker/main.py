from mod.settings import load_settings
from json import JSONDecodeError
from .mod.github_api import GitHubAPI
from mod.custom_exceptions import InvalidSettingsError

class Updater():
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

        self.github_api = GitHubAPI(self.ghUsername, self.ghRepo)

    def check_for_updates(self) -> bool:
        """Check for updates in the GitHub repository."""    
        latest_release = self.github_api.get_latest_release()
        if latest_release and latest_release != self.currentVersion:
            return True
        else:
            return False
