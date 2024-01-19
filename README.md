# ThousandEyes Telescope CLI

![Telescope CLI](telescope.jpeg)

This Python-based Command Line Interface (CLI) application, designed for interaction with the ThousandEyes API, emulates the syntax familiar to Cisco device users. It supports various "show" commands, much like a network operating system CLI.

Key Features:

- **Data Retrieval and Formatting:** The CLI fetches and formats data from the ThousandEyes API, offering a variety of output formats such as YAML, CSV, JSON, and human-readable text. This flexibility allows users to conveniently analyze and process the data as per their requirements.

- **Single Input Bearer Token:** A standout feature of this CLI is its one-time requirement for the ThousandEyes API Bearer Token. After the initial input, the application retains the token for the entire session, facilitating uninterrupted interaction with the API without necessitating repeated token entries.

- **Data Output Options:** The CLI provides two primary modes for data output. Users can opt to directly print the API response data to the terminal window or export the data to output files in their chosen format. This feature supports offline data analysis and record maintenance.

## Getting Started

To run the script, you'll need to have Python installed on your machine. Install the required Python libraries listed in the `requirements.txt` file using pip:

```
pip install -r requirements.txt
```

## Author

Miguel Hernandez

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

## Usage Instructions

Follow these steps to run the script:

1. Open a command line terminal. 

2. Navigate to the directory containing the `telescope.py` script. 

For example, if the script is in a directory called `my_scripts` in your home directory, you would navigate there with the command `cd ~/my_scripts` on macOS or `cd \Users\YourUsername\my_scripts` on Windows. Please replace `YourUsername` with your actual username.

3. Once inside the directory, you can run the script with the following command:

```
python telescope.py
```

4. After launching the script, you'll be greeted with the `telescope#` prompt. Here, you can enter the following commands:

- `debug enabled`: Enables debug mode.
- `debug disabled`: Disables debug mode.
- `ls`: Lists available resources.
- `show`: Retrieves and displays commands from the execute directory in the specified format (YAML, CSV, JSON, or human-readable).
- `exit`: Exits the program.

Remember, you must navigate to the script's directory before running it, as the script uses relative paths to access other files and directories. If you attempt to run the script from a different directory, it will not work correctly.

## Usability Available Commands
The following commands are currently available. Note that this list may expand over time:

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

To use these commands, simply type them at the `telescope#` prompt.

By default, these commands will provide information in JSON format. However, you can specify the output format using the file argument followed by the desired format (json, yaml, human, or csv). 

For example `show accounts file csv` will display account information in CSV format.

```bash
show accounts file csv
"netops1_te","1334416"
"netops2_te","1334421"
"netops3_te","1334426"
```

Changing the file extension to YAML:

```bash
telescope# show accounts file yaml
_links:
  self:
    href: https://api.thousandeyes.com/v7/account-groups
accountGroups:
- accountGroupName: netops1_te
  aid: '1334416'
  isCurrentAccountGroup: false
  isDefaultAccountGroup: false
  organizationName: Test
- accountGroupName: netops2_te
  aid: '1334421'
  isCurrentAccountGroup: false
  isDefaultAccountGroup: false
  organizationName: Test
```

If you want to filter the output for a specific aid, use the `aid` argument followed by the respective number. 

```bash
show endpoints aid 1374361
```

To write the output to a file in the `./output` directory (which will be created in the script's directory if it doesn't exist), use the write argument. For example, `show accounts write` will write account information to a file.

## Combining Arguments

The CLI also allows you to combine arguments for more specific outputs. Here's an example:

```
show endpoints file human aid 1234 write
```

In this command:

- `show endpoints` tells the CLI to retrieve endpoint data.
- `file human` specifies that the output format should be human-readable.
- `aid 1234` filters the output to only include data for the endpoint with aid 1234.
- `write` instructs the CLI to write the output to a file.

The resulting output will be written to a file in the `./output` directory. The file will contain human-readable endpoint data for the endpoint with aid 1234.

This combination of arguments provides a powerful and flexible way to retrieve and format data from the ThousandEyes API. You can mix and match arguments according to your needs.

## Environment Variable
You can also set the TELESCOPE_BEARER environment variable to your Bearer Authentication Token. This allows the script to authenticate with the ThousandEyes API without needing to enter the token every time.

### On macOS:

If you're using the zsh shell (the default on macOS Catalina and later), add the following line to your ~/.zshrc file:

```bash
export TELESCOPE_BEARER=your_token_here
```

Then, apply the changes with the command `source ~/.zshrc`.

### On Windows:

Use the setx command in Command Prompt:

```bash
setx TELESCOPE_BEARER "your_token_here"
```

Please replace `your_token_here` with your actual Bearer Authentication Token.

**Note:** Remember to restart your terminal or command prompt after setting the environment variable.
