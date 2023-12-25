from utils.transfer_videos_off_phone import transfer_files
from utils.convert_file_names import FileNameConverter
# from utils.hand_brake_process_videos import HBVideoProcessor
from utils.get_user_data import get_user_config
from utils.file_ops import create_clean_working_dir

WORKING_DIR = "temp"


create_clean_working_dir(WORKING_DIR)
# transfer_files(src, dest, types)

# obj = FileNameConverter("something")

config_data = get_user_config()

print(config_data)

# transfer_files(config_data["phone_video_directory"], working_dir, config_data["file_types"])