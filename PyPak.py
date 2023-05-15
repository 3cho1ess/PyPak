#This script is a Python program that automates the installation of multiple Python packages. It uses the pip command to check if a package is already installed and installs the package if it is not.

#The script sorts the list of packages in alphabetical order and installs them concurrently using multiple threads. It provides colorful console output using the colorama module.

#After installing all the packages, it displays a thank you message and waits for user input to exit.

#Made By Echoless#6801

import subprocess
import colorama
from colorama import Fore, Style
import concurrent.futures

colorama.init()

packages = [
    "beautifulsoup4", 
    "colorama", 
    "django", 
    "elasticsearch", 
    "fastapi", 
    "flask", 
    "google-cloud-storage", 
    "imageio", 
    "jupyter", 
    "kafka-python", 
    "keras", 
    "matplotlib", 
    "networkx", 
    "numpy", 
    "opencv-python", 
    "pdfkit", 
    "pandas", 
    "pygame", 
    "pyarrow", 
    "pydot", 
    "pyinstaller", 
    "pyjwt", 
    "pyodbc", 
    "pytesseract", 
    "python-docx", 
    "python-twitter", 
    "psycopg2", 
    "pyqt5", 
    "pyyaml", 
    "qrcode", 
    "redis", 
    "requests", 
    "scikit-learn", 
    "selenium", 
    "sqlalchemy", 
    "tensorflow", 
    "torch", 
    "tqdm", 
    "websockets", 
    "xlrd", 
    "pytorch-lightning", 
    "pandas-profiling", 
    "python-dotenv", 
    "PyMySQL", 
    "scipy", 
    "seaborn", 
    "transformers", 
    "tweepy", 
    "streamlit", 
    "pydantic", 
    "nltk", 
    "scrapy", 
    "bokeh", 
    "statsmodels", 
    "dash", 
    "xlwt", 
    "pycairo", 
    "tabulate", 
    "networkx", 
    "ipywidgets", 
    "pymongo", 
    "prettytable", 
    "altair", 
    "pygments", 
    "imutils", 
    "deap", 
    "ipyleaflet", 
    "pygraphviz", 
    "sphinx", 
    "pymc3", 
    "python-jose", 
    "pyglet", 
    "reportlab", 
    "kivy", 
    "flask-restful", 
    "pytz", 
    "matplotlib-venn", 
    "pyspark", 
    "suds", 
    "graph-tool", 
    "flask-socketio", 
    "cryptography", 
    "pyproj", 
    "google-api-python-client", 
    "jsonpickle", 
    "urllib3", 
    "faker", 
    "openpyxl", 
    "regex", 
    "sqlparse", 
    "pyautogui", 
    "faker", 
    "shapely", 
    "matplotlib-label-lines", 
    "pypdf2", 
    "qtpy", 
    "google-cloud-vision", 
    "flask-login", 
    "retrying", 
    "pretty_midi",
    "pandas-datareader",
    "pyarrow",
    "pydub",
    "pylint",
    "pyrebase",
    "pyttsx3",
    "pytube",
    "pyzmq",
    "scikit-image",
    "scikit-optimize",
    "scikit-posthocs",
    "scikit-surprise",
    "scipy",
    "seaborn",
    "sklearn",
    "statsmodels",
    "sympy",
    "textblob",
    "tqdm",
    "umap-learn",
    "xgboost"
]

def check_package_installed(package):
    try:
        result = subprocess.run(
            ["pip", "show", package], capture_output=True, text=True
        )
        return result.returncode == 0
    except Exception:
        return False


def install_package(package):
    if check_package_installed(package):
        print(f"{Fore.YELLOW}{package} - Package already installed{Style.RESET_ALL}")
        return

    try:
        result = subprocess.run(
            ["pip", "install", package], capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"{Fore.GREEN}{package} - Done installing{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}{package} - Can't install{Style.RESET_ALL}")
    except Exception:
        print(f"{Fore.RED}{package} - Can't install{Style.RESET_ALL}")


def main():
    print("Installing important packages...")

    packages.sort()  # Sort the packages list in alphabetical order

    max_workers = min(32, len(packages))  # Limiting max_workers to a reasonable number
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(install_package, package) for package in packages]

        for future in concurrent.futures.as_completed(futures):
            future.result()

    print(
        "\n"
        + Fore.GREEN
        + "Thank You For Using PyPak (Press Enter To Exit)"
        + Style.RESET_ALL
    )

    # Wait for user input to exit
    input()


if __name__ == "__main__":
    main()
