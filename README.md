# README for Transmission Settings Script

## Overview

This Python script provides a simple graphical user interface (GUI) using `tkinter` to manage and download torrents via a Transmission server. The script allows users to configure their Transmission server settings, including enabling or disabling authorization (username and password), specifying the host and port, and selecting a folder containing `.torrent` files for downloading.

## Features

- **Authorization Toggle**: Enable or disable authentication for the Transmission server.
- **Folder Browsing**: Select a folder that contains `.torrent` files.
- **Host and Port Configuration**: Specify the host and port for the Transmission server.
- **Automatic Dependency Installation**: The script will automatically install missing dependencies (`tkinter`, `requests`, `transmission-rpc`) if they are not already installed.
- **Torrent Download**: Automatically adds `.torrent` files from the selected folder to the Transmission server for downloading.

## Requirements

- Python 3.x
- `pip` (Python package installer)

## Dependencies

The script requires the following Python packages:

- `tkinter` (built-in for most Python distributions)
- `requests`
- `transmission-rpc`

If any of these packages are not installed, the script will automatically install them.

## How to Use

1. **Run the Script**: Execute the script using Python:
    ```bash
    python your_script_name.py
    ```

2. **Interface Usage**:
    - **Authorization**:
      - Check the "Enable Authorization" checkbox if your Transmission server requires a username and password.
      - Enter the required credentials in the provided fields.
    - **Folder Selection**:
      - Use the "Browse" button to select the folder containing your `.torrent` files.
    - **Host and Port**:
      - Specify the host (default is `localhost`) and port (default is `9091`) for your Transmission server.
    - **Download**:
      - Click the "Download" button to add the `.torrent` files in the selected folder to the Transmission server for downloading.

3. **Authorization**:
    - If authorization is enabled, you will need to provide the correct username and password.
    - If authorization is disabled, the username and password fields will be grayed out and inactive.

4. **Download Process**:
    - The script will scan the selected folder for `.torrent` files and add them to the Transmission server.
    - It will print the status of the authorization, folder path, host, port, and each added torrent to the console.

## Troubleshooting

- **Dependencies**: If the script fails to install a dependency, you may need to manually install it using `pip`:
    ```bash
    pip install requests transmission-rpc
    ```

- **tkinter Not Found**: If `tkinter` is not installed, follow the instructions for your operating system to install it:
  - **Linux**: 
    ```bash
    sudo apt-get install python3-tk
    ```
  - **Windows/MacOS**: `tkinter` usually comes pre-installed with Python. If not, reinstall Python with the `tkinter` option enabled.

## Customization

You can modify the script to suit your specific needs, such as changing default host and port values, or adding additional functionality to handle torrent files differently.


## Contact

If you encounter any issues or have suggestions for improvements, please feel free to reach out. Or open an issue. i'll try to add content as people tell me. 
