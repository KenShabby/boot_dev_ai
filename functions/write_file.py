import os


def write_file(working_directory, file_path, content):
    # If file_path is outsied working_directory return a string with an error:
    # f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    print(f"Now to make directory/file: {target_file}")

    try:
        with open(target_file, "w") as f:
            f.write(content)

    except Exception as e:
        return f"Error: {e}"

    return f"Write success!"
