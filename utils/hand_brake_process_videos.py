import os
import subprocess

# TODO: get input from user or config file
directory = "."

# TODO: get input from user or config file
processed_dir = os.path.join(directory, "processed")
os.makedirs(processed_dir, exist_ok=True)

command_template = [
    "HandBrakeCLI",
    "--preset-import-file",
    "PhoneVideoPreset.json",
    "-Z",
    "Phone Videos for Plex Server",
    "-i",
    None,  # input file placeholder
    "-o",
    None  # output file placeholder
]

command = command_template.copy()

for filename in os.listdir(directory):
    if filename.endswith(".mp4"):
        source_file = os.path.join(directory, filename)
        dest_file = os.path.join(directory, "processed", filename)

        command[6] = source_file
        command[8] = dest_file

        subprocess.run(command)
