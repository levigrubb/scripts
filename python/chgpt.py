#!/usr/bin/python3

import subprocess
import getpass
import argparse

# Function to run a command and enter the password when prompted
def run_command_with_password(command, password):
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        universal_newlines=True,
    )

    while True:
        output = process.stdout.readline()
        if not output and process.poll() is not None:
            break

        print(output, end="")  # Print the terminal output

        if "[sudo] password" in output or "password" in output:
            process.stdin.write(password + "\n")
            process.stdin.flush()

    process.stdout.close()
    process.stderr.close()

# Main function
def main():
    # Get the password from the user securely
    password = getpass.getpass("Enter your password: ")

    # Replace this with the actual command you want to run
    command = ["your_command_here"]

    try:
        run_command_with_password(command, password)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
