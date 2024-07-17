
# FIM - File Integrity Monitoring Tool

This tool monitors specified directories for changes in file integrity and sends Slack notifications when changes are detected.

![GitHub commit activity](https://img.shields.io/github/commit-activity/w/gmorgan9/FIM_project)
![GitHub License](https://img.shields.io/github/license/gmorgan9/FIM_project)



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

Install my-project with npm

```bash
 npm install my-project
 cd my-project
```
    

1. **Clone the repository:**

```bash
 git clone https://github.com/yourusername/file-integrity-monitor.git
 cd file-integrity-monitor
```

2. **Install dependencies:**

```bash
 pip install -r requirements.txt
```

3. **Setup environment variables:**

Create a `.env` file in the root directory with the following content:

```bash
 SLACK_WEBHOOK_URL=https://hooks.slack.com/services/your/slack/webhook/url
```

Replace `https://hooks.slack.com/services/your/slack/webhook/url` with your actual Slack webhook URL.

4. **Configure directories to monitor:** ***UPDATE THIS*****

Edit `directories.txt` file in the fim_tool directory to include directories you want to monitor, each on a new line.

Example `directories.txt`:

```bash
 /path/to/directory1
 /path/to/directory2
```

5. **Confirm the the installation script permissions:**

Move to the `scripts` directory within the project directory. Run the following command to allow for execution of both the installation and uninstallation scripts:

```
 chmod +x install_service_script.sh uninstall_service.sh
```

## Usage

Once installed and running, the tool will continuously monitor the specified directories for file changes and send Slack notifications accordingly.

## Contributing

Contributions are welcome via a request! If you encounter any issues or have suggestions for improvements, please open an issue on GitHub.

## License

This project is licensed under the MIT License - see the LICENSE file for details.