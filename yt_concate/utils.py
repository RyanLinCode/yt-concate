# utilities
import os.path

from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR


class Utils:
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)  # exist_ok 如果資料夾已經存在是沒問題
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    # 檢查 channel_id 是否存在
    def video_list_file_exist(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    # 擷取影片id
    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    # 路徑組合
    def get_caption_filepath(self, url):
        return os.path.join(CAPTIONS_DIR, self.get_video_id_from_url(url) + '.txt')

    # 檢查url資料是否存在
    def caption_file_exist(self, url):
        path = self.get_caption_filepath(url)
        # 檔案目錄是否存在 os.path.exists
        return os.path.exists(path) and os.path.getsize(path) > 0

