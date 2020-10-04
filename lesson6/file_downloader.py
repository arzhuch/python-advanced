"""
2) Создать функцию, которая будет скачивать файл из интернета по
ссылке, повесить на неё декоратор, который будет запускать целевую
функцию каждый раз в отдельном потоке. Создать список из 10
ссылок, по которым будет происходить скачивание. Каждый поток
должен сигнализировать, о том, что, он начал работу и по какой
ссылке он работает, так же должен сообщать когда скачивание
закончится.
"""


from requests import get
from mimetypes import guess_extension
from threading_decoraion import separate_thread


links_list = [
    "https://s3.eu-central-1.amazonaws.com/img.hromadske.ua/posts/197932/depositphotos370239808xl-2015jpg/large.jpg",
    "http://www.africau.edu/images/default/sample.pdf",
    "https://file-examples-com.github.io/uploads/2017/11/file_example_WAV_1MG.wav",
    "http://25.io/toau/audio/sample.txt",
    "https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2019-financial-year-provisional/Download-data/annual-enterprise-survey-2019-financial-year-provisional-csv.csv",
    "https://file-examples-com.github.io/uploads/2017/02/file-sample_100kB.doc",
    "https://sample-videos.com/video312/mp4/720/big_buck_bunny_720p_1mb.mp4",
    "https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_700KB.mp3",
    "https://support.spinetix.com/w/images/7/7c/Interactive_travel_sample.7z",
    "https://www.cardbox.com/download/samples1.exe",
]


@separate_thread
def downloader(link):

    print(f"Started downloading from {link}...")

    response = get(url=link)
    name = response.headers["ETag"][1:-1]
    ext = guess_extension(response.headers['content-type'])
    with open(f"{name}{ext}", "wb") as f:
        f.write(response.content)

    print(f"Finished download from {link}!")


for i in range(len(links_list)):
    downloader(links_list[i])
