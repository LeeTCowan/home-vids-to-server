import os
import paramiko
import glob
import json

class FileUploader:
    def __init__(self, server_data, file_types, processed_video_directory):
        self.server_ip = server_data.get("ip", "")
        self.username = server_data.get("username", "")
        self.private_key_path = server_data.get("private_key_path", "")
        self.remote_directory = server_data.get("processed_video_directory", "")
        self.processed_video_directory = processed_video_directory
        self.file_types = file_types
        self.skip_all = False
        self.ssh = self.create_ssh_client()

    def create_ssh_client(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        mykey = paramiko.RSAKey(filename=self.private_key_path)
        ssh.connect(self.server_ip, username=self.username, pkey=mykey)
        return ssh

    def get_existing_files(self):
        sftp = self.ssh.open_sftp()
        existing_files = sftp.listdir(self.remote_directory)
        sftp.close()
        return existing_files

    def handle_existing_file(self, file):
        while True:
            if self.skip_all:
                return None

            action = input(f"{file} already exists. Overwrite (O), Rename (R), Skip this file (S), or Skip all matching (A)? ").upper()

            if action not in ['O', 'R', 'S', 'A']:
                print("Invalid action. Please choose either O, R, S or A.")
                continue

            if action == 'O':
                return file
            elif action == 'R':
                new_name = input("Enter new file name: ")
                return new_name
            elif action == 'S':
                return None
            else:  # action == 'A'
                self.skip_all = True
                return None

    def upload_files(self):
        os.chdir(self.processed_video_directory)
        existing_files = self.get_existing_files()

        for extension in self.file_types:
            files = glob.glob(f'*.{extension}')

            for file in files:
                if file in existing_files:
                    file = self.handle_existing_file(file)
                    if file is None:
                        continue  # skip this file

                local_file_path = file
                remote_file_path = os.path.join(self.remote_directory, file)

                sftp = self.ssh.open_sftp()
                print(f"Uploading {local_file_path}...")
                sftp.put(local_file_path, remote_file_path)
                print(f"Completed uploading {local_file_path}.")
                sftp.close()

        self.skip_all = False  # reset skip_all after uploading all files

    def close_ssh_connection(self):
        self.ssh.close()


def load_config(filename):
    with open(filename, "r") as f:
        data = json.load(f)

        phone_video_directory = data.get("phone_video_directory", "")
        file_types = data.get("file_types", [])
        server_data = data.get("server", {})

        return phone_video_directory, file_types, server_data

def main():
    phone_video_directory, file_types, server_data = load_config("config.json")

    processed_video_directory = "processed"

    uploader = FileUploader(server_data, file_types, processed_video_directory)
    uploader.upload_files()
    uploader.close_ssh_connection()

if __name__ == "__main__":
    main()
