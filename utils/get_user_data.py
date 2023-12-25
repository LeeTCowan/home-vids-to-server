import json

def get_user_config():
    f = open('./user_data/config_template.json', 'r')

    data = json.load(f)

    phone_video_directory = data["phone_video_directory"]

    file_types = data["file_types"]

    server = data["server"]

    return data