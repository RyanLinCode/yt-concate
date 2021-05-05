import os

from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_DIR

# 越少參數傳遞越好(設計上/易讀性上/效能上)
# 身上屬性
class YT:
    def __init__(self, url):
        # 先從最初程式找 get video list 最初parameter 範圍就是 url
        self.url = url
        self.id = self.get_video_id_from_url(self.url)
        # 字幕影片位置
        self.caption_filepath = self.get_caption_filepath()
        self.video_filepath = self.get_video_filepath()
        # 儲存字幕
        self.captions = None

    # 擷取影片id
    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    # caption
    def get_caption_filepath(self):
        return os.path.join(CAPTIONS_DIR, self.id + '.txt')

    # video
    def get_video_filepath(self):
        return os.path.join(VIDEOS_DIR, self.id + '.mp4')

    def __str__(self):
        return '<YT(' + self.id + ')>'

    def __repr__(self):
        # join 合併字串 中間會有  :
        content = ' : '.join([
            'id=' + str(self.id),
            'caption_filepath=' + str(self.caption_filepath),
            'video_filepath=' + str(self.video_filepath)
        ])
        return '<YT('+ content + '>'