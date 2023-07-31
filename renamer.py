import os

class FolderCopyRenamer:
    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path

    def sanitize_folder_name(self, name):
        # Remove characters that are not allowed in Windows filenames
        windows_reserved_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        sanitized_name = "".join(c for c in name if c not in windows_reserved_chars)

        # Remove trailing spaces at the end of the folder name
        sanitized_name = sanitized_name.rstrip()

        # Limit the folder name length to 95 characters
        return sanitized_name[:95]

    def remove_end_spaces_in_directory_tree(self):
        root_path = self.destination_path  # Use self.destination_path as the root_path
        if not os.path.exists(root_path):
            print("Error: The specified root path does not exist.")
            return

        for dirpath, dirnames, filenames in os.walk(root_path):
            for dirname in dirnames:
                src_dir = os.path.join(dirpath, dirname)
                dest_dir = os.path.join(dirpath, dirname.rstrip())
                if src_dir != dest_dir:
                    os.rename(src_dir, dest_dir)

            for filename in filenames:
                src_file = os.path.join(dirpath, filename)
                dest_file = os.path.join(dirpath, filename.rstrip())
                if src_file != dest_file:
                    os.rename(src_file, dest_file)

    def copy_folders(self):
        if not os.path.exists(self.destination_path):
            os.makedirs(self.destination_path)

        destination_contents = os.listdir(self.destination_path)
        folder_counts = {}

        for foldername in os.listdir(self.source_path):
            folderpath = os.path.join(self.source_path, foldername)

            # Skip non-directory files
            if not os.path.isdir(folderpath):
                continue

            newfoldername = self.sanitize_folder_name(foldername)

            # Handle duplicate folder names at the destination directory
            while newfoldername in destination_contents:
                folder_counts.setdefault(newfoldername, 0)
                folder_counts[newfoldername] += 1
                newfoldername = f"{newfoldername}_{folder_counts[newfoldername]}"

            destination_folder = os.path.join(self.destination_path, newfoldername)

            print(f"Copying '{folderpath}' to '{destination_folder}'")
            self.copy_folder_recursive(folderpath, destination_folder)

    def copy_folder_recursive(self, source, destination):
        if not os.path.exists(destination):
            os.makedirs(destination)

        for item in os.listdir(source):
            source_item = os.path.join(source, item)
            destination_item = os.path.join(destination, item)

            if os.path.isdir(source_item):
                self.copy_folder_recursive(source_item, destination_item)
            else:
                self.copy_file(source_item, destination_item)

    def copy_file(self, source, destination):
        with open(source, 'rb') as src_file:
            with open(destination, 'wb') as dest_file:
                dest_file.write(src_file.read())

if __name__ == "__main__":
    source_path = "/home/uwu/Desktop/PORNO/descargas"
    destination_path = "/home/uwu/Desktop/PORNO/descargasConOtroNombre"

    folder_copy_renamer = FolderCopyRenamer(source_path, destination_path)
    folder_copy_renamer.copy_folders()
    folder_copy_renamer.remove_end_spaces_in_directory_tree()
    print("Renaming process is complete.")
