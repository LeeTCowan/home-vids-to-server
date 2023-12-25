import os
import re
from datetime import datetime
from collections import defaultdict


class FileNameConverter:
    def __init__(self, directory):
        self.directory = directory
        self.file_name_counter = defaultdict(int)

    def rename_files(self):
        # TODO: add support for other video file naming conventions, currently only works with pixel 6a format
        for filename in os.listdir(self.directory):
            
            ## Pixel 6a video file name matches
            if re.match("PXL_\d{8}_\d{9}(~\d)?\.mp4", filename):
                
                date_part = filename[4:12]
                date = datetime.strptime(date_part, "%Y%m%d")
                new_name = self.format_date(date)

                self.file_name_counter[new_name] += 1
                if self.file_name_counter[new_name] > 1:
                    new_name += " - (" + str(self.file_name_counter[new_name]) + ")"

                os.rename(filename, new_name + ".mp4")

    def format_date(self, date):
        day = date.day
        formatted = date.strftime("%Y - %b ") + str(day)

        if 11 <= day <= 13:
            formatted += "th"
        elif day % 10 == 1:
            formatted += "st"
        elif day % 10 == 2:
            formatted += "nd"
        elif day % 10 == 3:
            formatted += "rd"
        else:
            formatted += "th"

        return formatted
    