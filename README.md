# Instagram Account Hacking Script

## Overview

This Python script is designed to automate the process of hacking into Instagram accounts using Selenium, a web automation tool. It utilizes a Chrome WebDriver to interact with the Instagram login page, attempting to brute force the password by trying out a list of passwords from a file.

## Dependencies

- Python 3.x
- Selenium library
- Chrome WebDriver

## Installation

1. Install [Python 3.x](https://www.python.org/downloads/).
2. Install the Selenium library by running `pip install selenium`.
3. Download the [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your Python Scripts directory (or any directory of your choice).
4. Ensure that Chrome WebDriver path is correctly set in the script.

## Usage

1. Run the script using Python.
2. Enter the username of the Instagram account you want to hack.
3. Ensure you have a file named `mat.txt` containing a list of passwords to try, each on a separate line.
4. The script will then attempt to log in using each password from the file.
5. If successful, it will print the password to the console.

## Disclaimer

This script is for educational purposes only. Unauthorized access to someone's Instagram account is illegal and unethical. Use this script responsibly and only on accounts with explicit permission.
