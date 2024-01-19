# ThousandEyes Telescope CLI (CONTEXT)

![Telescope CLI](telescope.jpeg)

This Python-based Command Line Interface (CLI) application, designed for interaction with the ThousandEyes API, emulates the syntax and context familiar to Cisco device users. It supports various "show" commands, much like a network operating system CLI.

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
- `ls` or `show`: Lists available commands.
- `exit`: Exits the program.

Remember, you must navigate to the script's directory before running it, as the script uses relative paths to access other files and directories. If you attempt to run the script from a different directory, it will not work.

## Available Commands
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

## Command Line Usage

Once the Telescope CLI script is running and you're inside the `telescope#` context, you can use the following command structure:

```
show [command] file [csv | yaml | human | json] aid [aid-number] write
```

Here's a breakdown of the command structure:

- `show [command]`: This is the base command. Replace `[command]` with any of the available commands such as `accounts`, `agents`, `alerts`, etc.
- `file [csv | yaml | human | json]`: This is an optional command used to specify the output format. Replace `[csv | yaml | human | json]` with your preferred format.
- `aid [aid-number]`: This is another optional command used to filter the output for a specific `aid`. Replace `[aid-number]` with the `aid` you want to filter by.
- `write`: This is a standalone optional command. If included, the output will be written to a file in the `./output` directory.

Here's an example of how to use these commands:

```
show endpoints file human aid 1234 write
```

In this example, the `show endpoints` command retrieves endpoint data. The `file human` command specifies the output in a human-readable format. The `aid 1234` command filters the output for an endpoint with `aid` 1234. The `write` command writes this output to a file in the `./output` directory.

Remember, `file`, `aid`, and `write` are all optional. If you don't specify an output format, the default is JSON. If you don't specify an `aid`, the command will return data for the default `aid`. If you don't include `write`, the output will be printed to the terminal

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
