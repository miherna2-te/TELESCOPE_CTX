# TELESCOPE: A Python CLI for ThousandEyes API

![Telescope CLI](telescope.jpeg)

## Introduction
TELESCOPE is a Python-based Command Line Interface (CLI) application, that provides a seamless interaction with the ThousandEyes API. It emulates a familiar syntax and context for Cisco device users, supporting various "show" commands akin to a network operating system CLI.

## Problem Statement
The complex nature of APIs and the steep learning curve associated with them can pose challenges for users of the ThousandEyes platform.

## Solution
TELESCOPE bridges this gap by offering a user-friendly translator that speaks the language of Cisco and ThousandEyes API, simplifying the interaction process.

## Key Features
- **Usability:** Highly extendable and user-friendly.
- **Single Input Bearer Token:** Requires the ThousandEyes API Bearer Token only once, retaining it for the entire session.
- **Multiple Data Formats:** Supports JSON, YAML, CSV, and Human-readable formats.
- **Data Output Redirect:** Option to redirect data output to a console or a file.

## Versions
TELESCOPE is available in two versions: CLI and Context.

- **Command Line:** Integrates with Linux CLI, supporting redirection to commands like grep.
- **Cisco Context:** Mirrors the Cisco device experience for intuitive interaction with the ThousandEyes API.

## Getting Started
Ensure Python is installed on your machine. Install the required Python libraries listed in the `requirements.txt` file using pip:

```bash
pip install -r requirements.txt
```

## Dependencies
The script requires the following Python libraries:

- os
- re
- readline
- socket
- getpass
- rich
- importlib
- requests
- yaml
- json
- datetime
- jinja2

## Usage Instructions
1. Open a command line terminal.
2. Navigate to the directory containing the `telescope.py` script.
3. Run the script using the command:

```bash
python telescope.py
```

## Available Commands
- show accounts
- show agents
- show alerts
- show alerts rules
- show alerts suppression windows
- show bgp monitors
- show credentials
- show dashboards
- show endpoints
- show endpoints labels
- show endpoints tests
- show run
- show tags
- show tests

## Command Line Usage
```bash
show [command] file [csv | yaml | human | json] aid [aid-number] write
```
- `show [command]`: Base command. Replace `[command]` with the desired command.
- `file [csv | yaml | human | json]`: Optional. Specifies output format.
- `aid [aid-number]`: Optional. Filters output for a specific `aid`.
- `write`: Optional. Writes output to a file in the `./output` directory.

Examples:

To print out all the accounts run:

```bash
show accounts
```

To change the format to csv use:

```bash
show accounts file csv
```

The information can be filtered by using a specific AID as follows:

```bash
show endpoints file human aid 1234
```
To save the output as file, include `write` keyword:

```bash
show endpoints file human aid 1234 write
```

## Environment Variable
Set the TELESCOPE_BEARER environment variable to your Bearer Authentication Token to authenticate with the ThousandEyes API without needing to enter the token every time.

On macOS:
```bash
export TELESCOPE_BEARER=your_token_here
```

On Windows:
```bash
setx TELESCOPE_BEARER "your_token_here"
```
Replace `your_token_here` with your actual Bearer Authentication Token. 

**Note:** Remember to restart your terminal or command prompt after setting the environment variable.
