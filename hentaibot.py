import subprocess
import sys
def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
try:
    import tkinter as tk
    from tkinter import filedialog
except ImportError:
    print("tkinter not found, installing...")
    install_package("tk")
try:
    import requests
except ImportError:
    print("requests not found, installing...")
    install_package("requests")
try:
    from transmission_rpc import Client
except ImportError:
    print("transmission_rpc not found, installing...")
    install_package("transmission-rpc")


# Function to browse and select a folder path
def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_path_entry.delete(0, tk.END)
        folder_path_entry.insert(0, folder_path)

# Function to toggle authorization state
def toggle_authorization():
    if auth_var.get() == 1:
        username_entry.config(state=tk.NORMAL)
        password_entry.config(state=tk.NORMAL)
        print("Authorization enabled")
    else:
        username_entry.config(state=tk.DISABLED)
        password_entry.config(state=tk.DISABLED)
        print("Authorization disabled")
        


# Function to handle the download button click
def download_action():
    authorization_status = "Enabled" if auth_var.get() == 1 else "Disabled"
    folder_path = folder_path_entry.get()
    host = host_entry.get()
    port = port_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if auth_var.get() == 1:
        c = Client(host=host, port=port,username=username, password=password)
    else:
        c = Client(host=host, port=port)
    # Print the settings to the console (or perform actual download logic here)
    print(f"Authorization: {authorization_status}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Folder Path: {folder_path}")
    print(f"Host: {host}")
    print(f"Port: {port}")
    print("Download initiated...")
        # Iterate through the files in the specified directory
    torrent_files = []
    directory_path=folder_path
    for filename in os.listdir(directory_path):
        # Check if the file ends with '.torrent'
        if filename.endswith('.torrent'):
            # Add the full path of the .torrent file to the list
            full_path = os.path.join(directory_path, filename)
            print("filename is " + filename)
            torrent_files.append(full_path)

            # Open the .torrent file and read its content
            with open(full_path, 'rb') as torrent_file:
                torrent_data = torrent_file.read()

            # Add the torrent to the Transmission server
            torrent = c.add_torrent(torrent_data)
            print(f"Added torrent with ID: {torrent.id}")

root = tk.Tk()
root.title("Transmission Settings")

# Authorization Checkbox
auth_var = tk.IntVar()
auth_checkbox = tk.Checkbutton(root, text="Enable Authorization", variable=auth_var, command=toggle_authorization)
auth_checkbox.grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=10, padx=10)

# Username entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=0, sticky=tk.E, padx=10, pady=5)
username_entry = tk.Entry(root, width=40)
username_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

# Password entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=5)
password_entry = tk.Entry(root, show="*", width=40)
password_entry.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

# Folder path entry and button
folder_path_entry = tk.Entry(root, width=35)
folder_path_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.E)

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=3, column=2, padx=10, pady=5, sticky=tk.W)

# Input for localhost
host_label = tk.Label(root, text="Host:")
host_label.grid(row=4, column=0, sticky=tk.E, padx=10, pady=5)
host_entry = tk.Entry(root, width=40)
host_entry.insert(0, "localhost")
host_entry.grid(row=4, column=1, padx=10, pady=5, columnspan=2)

# Input for port
port_label = tk.Label(root, text="Port:")
port_label.grid(row=5, column=0, sticky=tk.E, padx=10, pady=5)
port_entry = tk.Entry(root, width=40)
port_entry.insert(0, "9091")
port_entry.grid(row=5, column=1, padx=10, pady=5, columnspan=2)

# Download button
download_button = tk.Button(root, text="Download", command=download_action)
download_button.grid(row=6, column=0, columnspan=3, pady=10)

# Disable username and password fields by default
username_entry.config(state=tk.DISABLED)
password_entry.config(state=tk.DISABLED)

# Run the application
root.mainloop()