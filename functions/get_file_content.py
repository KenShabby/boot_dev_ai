import os

from .config import MAX_CHARS


def get_file_content(working_directory, file_path):
    # If file_path is outsied working_directory return a string with an error:
    # f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # If the file_path is not a file, again, return an error string:
    # f'Error: File not found or is not a regular file: "{file_path}"'
    print(target_file)
    if not os.path.isfile(target_file):
        return f'Error: "File not found or is not a regular file: "{file_path}"'

    # Read the file and return its contents as a string.
    # If the file is longer than 10000 characters, truncate it to 10000
    # characters and append this message to the end [...File "{file_path}"
    # truncated at 10000 characters].
    # Instead of hard-coding the 10000 character limit, I stored it in a config.py file.
    try:
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) >= MAX_CHARS:
            file_content_string += (
                f"[...File '{file_path}' truncated at 10000 characters]."
            )

    except Exception as e:
        return f"Error: {e}"

    return file_content_string
