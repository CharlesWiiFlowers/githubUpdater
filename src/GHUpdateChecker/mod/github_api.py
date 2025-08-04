import requests
import warnings

class GitHubAPI:
    """Class for interacting with the GitHub API."""

    def __init__(self, username, repo):
        self.username = username
        self.repo = repo
        self.URL = f"https://api.github.com/repos/{self.username}/{self.repo}"

    def get_latest_release_tag(self):
        """Get the latest release information from the GitHub repository."""
        response = requests.get(f"{self.URL}/releases/latest")
        if response.status_code == 200:
            return response.json()["tag_name"]
        else:
            warnings.warn(f"Failed to retrieve latest release: {response.status_code}") 
            return None