import sys
import scripts.downloader

if __name__ == "__main__":
    # Get command line arguments
    ghUsername = sys.argv[1]
    ghRepo = sys.argv[2]
    runFile = sys.argv[3]
    rootProject = sys.argv[4]
    currentVersion = sys.argv[5]
    debug = sys.argv[6]
    whitelist = sys.argv[7]

    # Initialize the downloader
    downloader = scripts.downloader.ReleaseDownloader(ghUsername, ghRepo)
    downloader.download_latest_release()

    