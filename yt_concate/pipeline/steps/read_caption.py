from .step import Step


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            # 檢查字幕是否存在
            if not utils.caption_file_exist(yt):
                continue
            captions = {}
            with open(yt.caption_filepath, 'r') as f:
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
            yt.captions = captions

        return data




