# RAR-ZIP-Files-Password-Breaker
This Python script is a multi-functional security utility designed to perform Dictionary Attacks against password-protected ZIP and RAR archives. The project showcases fundamental concepts in Offensive Security and local system exploitation.

It includes two primary functions: a secure, number-based Wordlist Generator and dedicated Brute-Force Attack modules for both popular archive formats.

⚙️ Key Features
The tool offers the following functionalities via a command-line interface:

Password List Creation: Generates a custom wordlist (limited to numeric characters) based on user-defined length and quantity.

ZIP Cracking: Attempts to guess the password of a ZIP file using a specified wordlist, utilizing the pyzipper library for robust AES encryption support.

RAR Cracking: Attempts to guess the password of a RAR file using a specified wordlist, utilizing the rarfile library.

⚠️ Prerequisites and Requirements
To run this tool, you must install the required Python libraries.

Python Libraries:

Bash

pip install pyzipper rarfile
RAR Support: For the RAR cracking feature to work, the unrar command-line utility must be installed and accessible by your system (standard on most Linux distributions). (If running on Windows, the path to the unrar.exe tool may need configuration.)

🚀 Usage Steps
Run the Script:

Bash

python3 archive_cracker.py
Main Menu: Select the desired option (1, 2, or 3).

Wordlist Preparation: Always start by generating or specifying a wordlist (e.g., option 1 creates a list named password_list.txt).

Cracking: Provide the file name and the tool will iterate through the wordlist to find the password.

🎯 Cybersecurity Focus
This project serves as a strong demonstration of the following concepts:

Offline Brute-Force: Understanding the mechanics of dictionary attacks against poorly secured files.

Password Strength: Illustrating the vulnerability of short or numeric-only passwords.

Encryption Testing: Applying cryptographic libraries (pyzipper) to test archive security.
