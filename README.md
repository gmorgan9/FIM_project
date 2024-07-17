
# FIM - File Integrity Monitoring Tool

This tool monitors specified directories for changes in file integrity and sends Slack notifications when changes are detected.

![GitHub License](https://img.shields.io/github/license/gmorgan9/FIM_project?style=for-the-badge)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/gmorgan9/FIM_project?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/gmorgan9/FIM_project?style=for-the-badge&label=project%20size)
![GitHub Release Date](https://img.shields.io/github/release-date/gmorgan9/FIM_project?style=for-the-badge)
![GitHub Release](https://img.shields.io/github/v/release/gmorgan9/FIM_project?style=for-the-badge)

## Features

- Monitors multiple directories simultaneously.
- Sends Slack notifications on file creation, modification, and deletion.
- Supports skipping `.swp` files (optional).


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- `pip` package manager
- Access to Slack webhook URL for notifications
## Installation

1. **Clone the repository:**

```bash
 git clone https://github.com/gmorgan9/FIM_project.git
 cd FIM_project
```

2. **Setup environment variables:**

Create a `.env` file in the root directory with the following content:

```bash
 SLACK_WEBHOOK_URL=https://hooks.slack.com/services/your/slack/webhook/url
```

Replace `https://hooks.slack.com/services/your/slack/webhook/url` with your actual Slack webhook URL.

3. **Install as a service:**

```bash
 cd scripts
 chmod +x install_service.sh uninstall_service.sh
 sudo ./install_service.sh
```

4. **Configure directories to monitor:**

Add directories to the `directories.txt` file using the following python script. This script will allow you to include directories you want to monitor, each on a new line.

```bash
 sudo python3 add_directory.py
```

5. **Restart the FIM Project Tools:**

```bash
 sudo systemctl restart file_integrity_monitor.service
```

## Uninstall Service

Redirect to the `FIM_project/scripts` directory to run the following command:

```bash
 sudo ./uninstall_service.sh
```

## Usage

Once installed and running, the tool will continuously monitor the specified directories for file changes and send Slack notifications accordingly.

## Contributing

Contributions are welcome via a request! If you encounter any issues or have suggestions for improvements, please open an issue on GitHub.

## License

This project is licensed under the GPL-3.0 License - see the LICENSE file for details.