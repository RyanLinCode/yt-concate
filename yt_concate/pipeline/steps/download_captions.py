import time
import concurrent.futures
from multiprocessing import Process

from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        processes = []

        for i in range(4):
            processes.append(Process(target=self.downcaptions, args=(data[i::4], inputs, utils)))
            # 以某種規律選擇清單中的網址，達到分割清單目的，讓 process 不會撞車
        for process in processes:
            process.start()
        for process in processes:
            process.join()

        end = time.time()
        print('took', end - start, 'seconds')

        return data

    def downcaptions(self, data, inputs, utils):
        # download the package by:  pip install pytube
        for yt in data:
            print('download caption for', yt.id)
            if utils.caption_file_exist(yt):
                print('found existing caption file')
                continue
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')  # a 代表自動產生
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except AttributeError:
                print('No subtitle, AttributeError when downloading caption for', yt.url)
                continue

            text_file = open(yt.get_caption_filepath(), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
