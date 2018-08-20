import os
import re


class GetFiles:
    def __init__(self, search_dir, file_pattern):
        self.search_dir = search_dir
        self.file_pattern = file_pattern

    def crawl_dir(self):
        files = []
        for root, dirs, file_names in os.walk(self.search_dir):
            for file in file_names:
                if self.file_pattern is not "*":
                    if bool(re.search(self.file_pattern, file, re.IGNORECASE)):
                        files.append(os.path.join(root, file))
                else:
                    files.append(os.path.join(root, file))
        return files
