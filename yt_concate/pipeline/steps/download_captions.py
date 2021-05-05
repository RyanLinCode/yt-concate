import time

from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        # download the package by:  pip install pytube
        for yt in data:
            print('download caption for', yt.id)
            if utils.caption_file_exist(yt):
                print('found existing caption file')
                continue
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en') # a 代表自動產生
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except AttributeError:
                print('No subtitle, AttributeError when downloading caption for', yt.url)
                continue

            text_file = open(utils.get_caption_filepath(yt.url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', end - start, 'seconds')

        return data

