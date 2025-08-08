import os
from google.genai import types


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

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the given contents to the specified file, creating it if necessary.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The file path to write contents to.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The string to write to the file path.",
            ),
        },
    ),
)
