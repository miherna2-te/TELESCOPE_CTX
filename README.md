# ThousandEyes Telescope CLI

![Telescope CLI](telescope.jpeg)

This Python script is a Command Line Interface (CLI) application designed to interact with the ThousandEyes API, using a syntax similar to Cisco devices. The application gives users the ability to execute various "show" commands, similar to a network operating system command-line interface (CLI).

The CLI retrieves and formats data from the ThousandEyes API, displaying it in multiple output formats including YAML, CSV, JSON, and human-readable format. This variety of output formats enables users to easily analyze and manipulate the data according to their needs.

One of the key features of this CLI is that it requires the ThousandEyes API Bearer Token to be entered only once. After initial input, the application retains the token for the duration of the session, allowing for continuous interaction with the API without the need to repeatedly enter the token.

The CLI offers two primary methods for data output. The first is to print the API response data directly to the terminal window. Alternatively, the CLI can export the data to output files in the specified format, allowing for offline analysis and record-keeping.

## Getting Started

To run the script, you'll need to have Python installed on your machine. Install the required Python libraries listed in the `requirements.txt` file using pip:

```
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

These libraries can be installed via pip using the `requirements.txt` file.

## How to Use

The script can be run from a command line terminal using the following command:

```
python telescope.py
```

Once the script is running, you will be prompted to enter your commands at the `telescope#` prompt. The script accepts the following commands:

- `debug enabled`: Enables debug mode.
- `debug disabled`: Disables debug mode.
- `ls`: Lists available resources.
- `show`: Retrieves and displays commands from the execute directory in the specified format (YAML, CSV, JSON, or human-readable).
- `exit`: Exits the program.

## Error Handling

If an error occurs while the script is running, it will be printed to the console with a message indicating that an error occurred.

## Author

Miguel Hernandez

## Usability Available Commands
The following commands are currently available. Note that this list may expand over time:

show accounts
show agents
show alerts
show alerts rules
show alerts suppression windows
show bgp monitors
show credentials
show dashboards
show endpoints
show endpoints labels
show endpoints tests
show run
show tags
show tests

To use these commands, simply type them at the telescope# prompt.

By default, these commands will provide information in JSON format. However, you can specify the output format using the file argument followed by the desired format (json, yaml, human, or csv). For example, show accounts file yaml will display account information in YAML format.

If you want to filter the output for a specific aid, use the aid argument followed by the aid number. For example, show accounts aid 1234 will display information for the account with aid 1234.

To write the output to a file in the ./output directory (which will be created in the script's directory if it doesn't exist), use the write argument. For example, show accounts write will write account information to a file.

Environment Variable
You can also set the TELESCOPE_BEARER environment variable to your Bearer Authentication Token. This allows the script to authenticate with the ThousandEyes API without needing to enter the token every time.

On macOS:

If you're using the zsh shell (the default on macOS Catalina and later), add the following line to your ~/.zshrc file:

export TELESCOPE_BEARER=your_token_here
Then, apply the changes with the command source ~/.zshrc.

On Windows:

Use the setx command in Command Prompt:

setx TELESCOPE_BEARER "your_token_here"
Please replace your_token_here with your actual Bearer Authentication Token.

Note: Remember to restart your terminal or command prompt after setting the environment variable.
