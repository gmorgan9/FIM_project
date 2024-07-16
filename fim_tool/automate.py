import os
import hashlib
import time
import requests
import socket  # for getting hostname
import pwd  # for getting username from UID
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to calculate MD5 hash of a file
def calculate_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

# Function to get hostname
def get_hostname():
    return socket.gethostname()

# Function to get the username from UID
def get_username(uid):
    try:
        return pwd.getpwuid(uid).pw_name
    except KeyError:
        return "Unknown"

# Function to send Slack notification with structured message
def send_slack_notification(file_path, directory, file_name, change_type, user, webhook_url):
    hostname = get_hostname()

    # Construct the Slack message using Block Kit JSON
    message = (
        f"*File Integrity Alert*\n"
        f"Host: `{hostname}`\n"
        f"File Path: `{file_path}`\n"
        f"Directory: `{directory}`\n"
        f"File Name: `{file_name}`\n"
        f"Change Type: `{change_type}`\n"
        f"Changed By: `{user}`"
    )

    data = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": message
                }
            }
        ]
    }
    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        print("Slack notification sent successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Slack notification: {e}")

# Function to read directories from inventory file
def read_directories_from_file(file_path):
    directories = []
    with open(file_path, 'r') as f:
        for line in f:
            directory = line.strip()
            if directory:
                directories.append(directory)
    return directories

# Function to monitor directories
def monitor_directories(directories, webhook_url):
    monitored_files = {}

    # Initial scan of directories
    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                monitored_files[file_path] = calculate_hash(file_path)

    # Monitoring loop
    while True:
        for file_path in list(monitored_files.keys()):
            if not os.path.exists(file_path):
                directory, file_name = os.path.split(file_path)
                send_slack_notification(file_path, directory, file_name, "Deleted", "Unknown", webhook_url)
                del monitored_files[file_path]
            else:
                current_hash = calculate_hash(file_path)
                if monitored_files[file_path] != current_hash:
                    directory, file_name = os.path.split(file_path)
                    user = get_username(os.stat(file_path).st_uid)
                    send_slack_notification(file_path, directory, file_name, "Modified", user, webhook_url)
                    monitored_files[file_path] = current_hash

        # Check for new files in all directories
        for directory in directories:
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file_path not in monitored_files:
                        user = get_username(os.stat(file_path).st_uid)
                        send_slack_notification(file_path, directory, file, "Created", user, webhook_url)
                        monitored_files[file_path] = calculate_hash(file_path)

        time.sleep(5)  # Adjust the interval as needed

# Example usage
if __name__ == "__main__":
    # Load directories to monitor from inventory file
    inventory_file = "directories.txt"
    directories_to_monitor = read_directories_from_file(inventory_file)

    # Load Slack webhook URL from environment variable
    slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")

    # Start monitoring directories
    monitor_directories(directories_to_monitor, slack_webhook_url)
