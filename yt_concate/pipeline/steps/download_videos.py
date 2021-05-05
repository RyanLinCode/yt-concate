from pytube import YouTube

from .step import Step
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        # 去除重複影片
        yt_set = set([found.yt for found in data])
        print('videos to download=', len(yt_set))
        for yt in yt_set:
            url = yt.url

            # 跳過已下載影片
            if utils.video_file_exist(yt):
                print(f'found existing video file for {url}, skipping')
                continue

            print('downloading', url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)

        return data
