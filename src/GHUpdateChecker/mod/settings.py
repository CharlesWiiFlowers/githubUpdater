import json
from warnings import warn

def load_settings(path="GHUpdateSettings.json"):
    with open(path, "r") as f:
        settings = json.load(f)

    ghUsername = settings.get("GitHubUsername")
    ghRepo = settings.get("GitHubRepo")
    runFile = settings.get("Run", None)
    rootProject = settings.get("Root")
    currentVersion = settings.get("CurrentVersion", None)
    debug = settings.get("Debug", False)
    whitelist = settings.get("Whitelist", ["GHUpdateSettings.json", "README.md", "LICENSE", "CONTRIBUTING.md", ".env", ".gitignore"])

    return (ghUsername, ghRepo, runFile, rootProject, currentVersion, debug, whitelist)

    # TODO: Add a autocreation of the settings file if it does not exist