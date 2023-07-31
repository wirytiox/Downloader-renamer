import os
import time
import importlib
import libtorrent as lt

class TorrentDownload:
    def __init__(self, folder_path, save_path):
        self.folder_path = folder_path
        self.save_path = save_path
        self.cancel_flag = False  # Flag to indicate whether the download should be canceled

    def download_torrents_in_folder(self):
        # Create a session with increased metadata size settings
        settings = lt.session_params()
        settings.max_metadata_size = 100 * 1024 * 1024  # Increase the maximum metadata size to 100 MB
        ses = lt.session(settings)

        # Iterate over files in the folder
        for file_name in os.listdir(self.folder_path):
            if self.cancel_flag:
                print("Download canceled.")
                break

            torrent_file_path = os.path.join(self.folder_path, file_name)

            # Check if it's a torrent file
            if file_name.endswith('.torrent'):
                try:
                    # Add the torrent
                    handle = ses.add_torrent({'ti': lt.torrent_info(torrent_file_path), 'save_path': self.save_path})

                    # Start the download
                    print("Downloading:", torrent_file_path)
                    while not handle.status().is_seeding:
                        s = handle.status()

                        # Print download progress (overwrites the previous progress message)
                        print("\rProgress: %.2f%%" % (s.progress * 100), end='')

                        # Sleep for a while (1 second)
                        time.sleep(1)

                        # Check if download should be canceled
                        if self.cancel_flag:
                            handle.pause()
                            break

                    # Print a new line after the download is complete
                    print("\nDownload complete for", torrent_file_path)

                except Exception as e:
                    print("\nError occurred during download for", torrent_file_path + ":", str(e))
                    print("Download failed for", torrent_file_path)
                    break

    def cancel_download(self):
        self.cancel_flag = True

# Rest of the code remains unchanged
