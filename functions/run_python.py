import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):

    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file):
        return f'Error: File "{file_path}" not found.'

    try:
        completed_process = subprocess.run(
            target_file, capture_output=True, cwd=working_directory, timeout=30, **args
        )

        print(f"STDOUT: {completed_process.stdout}")
        print(f"STDERR: {completed_process.stderr}")
        if completed_process.returncode != 0:
            print(f"Process exited with code: {completed_process.returncode}")
        if completed_process.stdout and completed_process.stderr == None:
            return f"No output produced"
    except Exception as e:
        f"Error: executing Python file: {e}"
