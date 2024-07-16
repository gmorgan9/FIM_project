import os

# Path to the directories.txt file
directories_file = "/usr/local/bin/fim_tool/directories.txt"

def add_directories_to_file(directories):
    try:
        with open(directories_file, 'a') as f:
            for directory in directories:
                f.write(directory + '\n')
        print("Directories added successfully.")
    except IOError as e:
        print(f"Error writing to {directories_file}: {e}")

if __name__ == "__main__":
    print("Enter directories to add (one per line). Press Enter on a blank line to finish.")
    directories = []
    while True:
        directory = input("> ").strip()
        if not directory:
            break
        directories.append(directory)

    if directories:
        add_directories_to_file(directories)
