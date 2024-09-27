import subprocess
import sys

# List of packages to install
packages = [
    'requests',
    'Pillow',  # This package corresponds to 'from PIL import ImageGrab'
    'pygetwindow',
    'keyboard',
]

def install(package):
    """Install a package using pip."""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

def main():
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"{package} not installed. Installing...")
            install(package)
        else:
            print(f"{package} is already installed.")

if __name__ == "__main__":
    main()
