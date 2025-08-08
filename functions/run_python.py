import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file):
        return f'Error: File "{file_path}" not found.'

    try:
        completed_process = subprocess.run(
            ["python", target_file] + args,
            capture_output=True,
            cwd=working_directory,
            timeout=30,
            text=True,
        )

        print(f"STDOUT: {completed_process.stdout}")
        print(f"STDERR: {completed_process.stderr}")
        if completed_process.returncode != 0:
            print(f"Process exited with code: {completed_process.returncode}")
        if completed_process.stdout is None and completed_process.stderr is None:
            return "No output produced"
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a given file in the working directory. Includes command line\
        arguments, if any.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
