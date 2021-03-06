
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_video import EditVideo
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils

# 全部大寫示意內容不變
CHANNEL_ID = 'UCk55DOnuAgOiFnBj-0XXwGQ'
# UCLQJGvzJiYGhGAGvwodRL4A
# UCKSVUHI9rbbkXhvAXK-2uxA

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'impossible',
        'limit': 20,
    }
    # incredible
    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        # ReadCaption(),
        # Search(),
        # DownloadVideos(),
        # EditVideo(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
