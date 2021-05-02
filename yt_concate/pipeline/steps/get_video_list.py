import urllib.request
import json

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import API_KEY


class GetVideoList(Step):
    # 用字典打包避免一直增加參數卻只有某一個step用得到
    def process(self, data, inputs):
        channel_id = inputs['channel_id']
        base_video_url = 'https://www.youtube.com/watch?v='  # 某個影片的id
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'  # 使用api的網址
        #                           字典 Key channelId 字典value {}
        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY,
                                                                                                            channel_id)

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            # 不建議抓取所有錯誤
            except KeyError:
                break
        print(video_links)
        return video_links