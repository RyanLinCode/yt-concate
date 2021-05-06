# utilities
import os.path

from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import OUTPUT_DIR


class Utils:
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)  # exist_ok 如果資料夾已經存在是沒問題
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    # 檢查 channel_id 是否存在
    def video_list_file_exist(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    # 檢查字幕 資料是否存在
    def caption_file_exist(self, yt):
        # 檔案目錄是否存在 os.path.exists
        filepath = yt.caption_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    # 檢查影片 是否存在
    def video_file_exist(self, yt):
        # 檔案目錄是否存在 os.path.exists
        filepath = yt.video_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    # 結果檔輸出位置
    def get_output_filepath(self, channel_id, search_word):
        filename = channel_id + '_' + search_word + '.mp4'
        return os.path.join(OUTPUT_DIR, filename)
