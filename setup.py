"""
This setup.py file is used by py2app to create a standalone macOS .app bundle.
"""
from setuptools import setup, find_packages

APP = ['autoclicker/__main__.py']  # Path to your main script
DATA_FILES = []                   # Add any additional non-python files here if needed
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'applogo.png',    # Path to your icon file. Preferably use an .icns file.
    'packages': [],
}

setup(
    name="afk-destroyer",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pyautogui",
    ],
    python_requires=">=3.6",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
) 