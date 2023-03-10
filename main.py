__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Imports
import os
import shutil
from zipfile import ZipFile

base_path = os.getcwd()
cache_path = os.path.join(base_path, "cache")
data_path = os.path.join(base_path, "data.zip")

# part 1
def clean_cache():
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)
    os.mkdir("cache")

# part 2
def cache_zip(zip, cache):
    with ZipFile(zip, "r") as zipObj:
        zipObj.extractall(cache)

# part 3
def cached_files():
    cached_files_list = []
    for path in os.listdir(cache_path):
        full_path = os.path.join(cache_path, path)
        cached_files_list.append(full_path)
    return cached_files_list

# part 4
def find_password(list_of_files):
    for file in list_of_files:
        with open(file) as f:
            for line in f:
                if "password" in line:
                    #The function splits the line into two parts using the split method with the argument " " (a space character) as the separator. This creates a list of two elements, where the first element is everything before the first space in the line, and the second element is everything after the first space.
                    split_password = line.split(" ", 1)
                    #The function then returns the second element of the list, which should be the password. However, it first removes the newline character ("\n") from the end of the password string using the replace method, with the argument "\n" as the string to be replaced and an empty string ("") as the replacement string.
                    return split_password[1].replace("\n", "")

# calling the output
if __name__ == "__main__":
    clean_cache()
    cache_zip(data_path, cache_path)
    cached_files()
    print(find_password(cached_files()))
