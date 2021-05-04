import os
from pprint import pprint

from .step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            # 字典裝載內容
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                time_line = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        # 存時間
                        time = line
                        continue
                    if time_line:
                        # 存字幕
                        caption = line
                        # for loop iterater key 直接拿到字幕
                        captions[caption] = time
                        time_line = False
                        # Key檔名       Value
            data[caption_file] = captions

        pprint(data)
        return data




