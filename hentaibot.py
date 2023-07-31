import tkinter as tk
from tkinter import filedialog
from renamer import FolderCopyRenamer
from torrent_downloader import TorrentDownload
import configparser
import os
import threading

# Configuration file path
config_file = "config.ini"

# Create and read the configuration file
config = configparser.ConfigParser()
config.read(config_file)

# Retrieve the last entered paths from the configuration file (if available)
last_torrents_path = config.get("Paths", "LastTorrentsPath", fallback="")
last_destination_path = config.get("Paths", "LastDestinationPath", fallback="")
last_destination_renamed_path = config.get("Paths", "LastDestinationRenamedPath", fallback="")

def browse_torrents_path():
    selected_path = filedialog.askdirectory()
    torrents_path_entry.delete(0, tk.END)
    torrents_path_entry.insert(0, selected_path)

def browse_destination_path():
    selected_path = filedialog.askdirectory()
    destination_path_entry.delete(0, tk.END)
    destination_path_entry.insert(0, selected_path)

def browse_destination_renamed_path():
    selected_path = filedialog.askdirectory()
    destination_renamed_path_entry.delete(0, tk.END)
    destination_renamed_path_entry.insert(0, selected_path)

def run_torrent_downloader():
    def download_torrents():
        # Get the source and destination paths from the GUI
        torrents_path = torrents_path_entry.get()
        destination_path = destination_path_entry.get()

        # Check if the required paths are not empty
        if not torrents_path or not destination_path:
            print("Error: Please provide both torrents path and destination path.")
            return

        # Print entered paths
        print("Entered Torrents Path:", torrents_path)
        print("Entered Destination Path:", destination_path)

        # Save the entered paths to the configuration file
        config["Paths"] = {
            "LastTorrentsPath": torrents_path,
            "LastDestinationPath": destination_path,
            "LastDestinationRenamedPath": destination_renamed_path_entry.get()
        }
        with open(config_file, "w") as configfile:
            config.write(configfile)

        # Print the paths read from the configuration file
        print("Last Torrents Path from Config:", config.get("Paths", "LastTorrentsPath"))
        print("Last Destination Path from Config:", config.get("Paths", "LastDestinationPath"))
        print("Last Destination Renamed Path from Config:", config.get("Paths", "LastDestinationRenamedPath"))

        # Create an instance of the TorrentDownload class with the provided paths
        global torrent_downloader
        torrent_downloader = TorrentDownload(torrents_path, destination_path)

        # Call the download_torrents_in_folder method to start the torrent download
        torrent_downloader.download_torrents_in_folder()

    # Create a separate thread for running the torrent downloader
    download_thread = threading.Thread(target=download_torrents)
    download_thread.start()

def cancel_torrent_download():
    if 'torrent_downloader' in globals():
        torrent_downloader.cancel_download()

def run_renamer_script():
    # Get the destination renamed path from the GUI
    destination_renamed_path = destination_renamed_path_entry.get()

    # Check if the required path is not empty
    if not destination_renamed_path:
        print("Error: Please provide the destination renamed path.")
        return

    # Get the source path from the GUI
    source_path = destination_path_entry.get()

    # Check if the source path is not empty
    if not source_path:
        print("Error: Please provide the source path.")
        return

    # Print entered paths
    print("Entered Source Path:", source_path)
    print("Entered Destination Renamed Path:", destination_renamed_path)

    # Create an instance of the FolderCopyRenamer class with the provided paths
    folder_renamer = FolderCopyRenamer(source_path, destination_renamed_path)

    # Call the copy_folders and remove_end_spaces_in_directory_tree methods to perform the renaming
    folder_renamer.copy_folders()
    folder_renamer.remove_end_spaces_in_directory_tree()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Torrent Downloader and Renamer")

    # Create the torrent's path Browse button and entry field
    torrents_path_frame = tk.Frame(root)
    torrents_path_frame.pack(pady=5)

    torrents_path_button = tk.Button(torrents_path_frame, text="Browse Torrents Path", command=browse_torrents_path)
    torrents_path_button.pack(side=tk.LEFT)

    torrents_path_entry = tk.Entry(torrents_path_frame, width=40)
    torrents_path_entry.pack(side=tk.LEFT, padx=10, fill=tk.X)

    # Set the last entered torrents path if available
    if last_torrents_path:
        torrents_path_entry.insert(0, last_torrents_path)

    # Create the destination path Browse button and entry field
    destination_path_frame = tk.Frame(root)
    destination_path_frame.pack(pady=5)

    destination_path_button = tk.Button(destination_path_frame, text="Browse Destination Path", command=browse_destination_path)
    destination_path_button.pack(side=tk.LEFT)

    destination_path_entry = tk.Entry(destination_path_frame, width=40)
    destination_path_entry.pack(side=tk.LEFT, padx=10, fill=tk.X)

    # Set the last entered destination path if available
    if last_destination_path:
        destination_path_entry.insert(0, last_destination_path)

    # Create the renamed destination path Browse button and entry field
    destination_renamed_path_frame = tk.Frame(root)
    destination_renamed_path_frame.pack(pady=5)

    destination_renamed_path_button = tk.Button(destination_renamed_path_frame, text="Browse Destination Renamed Path", command=browse_destination_renamed_path)
    destination_renamed_path_button.pack(side=tk.LEFT)

    destination_renamed_path_entry = tk.Entry(destination_renamed_path_frame, width=40)
    destination_renamed_path_entry.pack(side=tk.LEFT, padx=10, fill=tk.X)

    # Set the last entered destination renamed path if available
    if last_destination_renamed_path:
        destination_renamed_path_entry.insert(0, last_destination_renamed_path)

    # Create a button to run the Torrent Downloader
    run_torrent_button = tk.Button(root, text="Run Torrent Downloader", command=run_torrent_downloader)
    run_torrent_button.pack(pady=10)

    # Create a button to cancel the Torrent Downloader
    cancel_torrent_button = tk.Button(root, text="Cancel Download", command=cancel_torrent_download)
    cancel_torrent_button.pack(pady=5)

    # Create a button to run the renamer.py script
    run_renamer_button = tk.Button(root, text="Run renamer.py Script", command=run_renamer_script)
    run_renamer_button.pack(pady=10)

    root.mainloop()
