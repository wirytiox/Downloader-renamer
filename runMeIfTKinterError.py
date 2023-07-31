import subprocess
import platform

def install_tkinter():
    try:
        if platform.system() == "Linux":
            subprocess.run(['sudo', 'apt-get', 'install', 'python3-tk'], check=True)
            print("python3-tk installed successfully!")
        else:
            print("python3-tk installation is only supported on Linux.")
    except subprocess.CalledProcessError:
        print("Error occurred while installing python3-tk.")

if __name__ == "__main__":
    install_tkinter()
