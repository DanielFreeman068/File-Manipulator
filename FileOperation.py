import shutil
import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content

print(read_file("sample.txt"))

def edit_text_file(file_path, new_content):
    with open(file_path, 'a') as file:
        file.write(" " + new_content)

edit_text_file("sample.txt", "Additional line added for operations")

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully!")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

create_folder("Files")

shutil.move('sample.txt', 'Files')

def rename_file(current_name, new_name):
    try:
        os.rename(current_name, new_name)
        print(f"File '{current_name}' has been renamed to '{new_name}'.")
    except FileNotFoundError:
        print("File not found. Please check the file name or path.")
    except FileExistsError:
        print(f"A file with the name '{new_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

rename_file("file1.txt", "renamed_file.txt")

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' has been deleted.")
    except FileNotFoundError:
        print("File not found. Please check the file name or path.")
    except Exception as e:
        print(f"An error occurred: {e}")

delete_file("file2.txt")

def list_files(folder_path):
    try:
        files = os.listdir(folder_path)
        
        if not files:
            print("No files found in the folder.")
        else:
            print(f"Files in '{folder_path}':")
            for file in files:
                print(file)
    except FileNotFoundError:
        print("Folder not found. Please check the folder path.")
    except Exception as e:
        print(f"An error occurred: {e}")

list_files("Files")

shutil.make_archive('my_archive', 'zip', 'directory_to_archive')