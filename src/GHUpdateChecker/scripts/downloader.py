import requests
import warnings

class ReleaseDownloader:
    """Class for downloading the latest release from a GitHub repository."""

    def __init__(self, username, repo):
        self.username = username
        self.repo = repo
        self.URL = f"https://api.github.com/repos/{self.username}/{self.repo}/releases/latest"

    def download_latest_release(self) -> bool:
        """Download the latest release from the GitHub repository.\n
        @return: True if download was successful, False otherwise."""
        response = requests.get(self.URL)
        if response.status_code == 200:
            release_data = response.json()
            download_url = release_data.get("zipball_url", None)
            if download_url:
                return self._download_file(download_url, release_data.get("id"))
            else:
                warnings.warn("No downloadable asset found.")
                return False
        else:
            warnings.warn(f"Failed to retrieve latest release: {response.status_code}")
            return False

    def _download_file(self, url, id) -> bool:
        """Download a file from a URL."""
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"./__temp__/{id}.zip", "wb") as f:
                f.write(response.content)
            return True
        else:
            warnings.warn(f"Failed to download file: {response.status_code}")
            return False
