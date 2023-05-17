import pickle

SAVE_FILE = "D:\_Study_A\my_refresh_music"
MY_URL = "https://www.youtube.com/playlist?list=PLqU9jKopJpR45-N9Obwy1TdDWikKOBWC_"


from my_youtube_handler.my_youtube import my_PlaylistDownloader

if __name__ == '__main__':

    p = my_PlaylistDownloader(MY_URL, SAVE_FILE)

    with open('data.pickle', 'rb') as file:
        p : my_PlaylistDownloader = pickle.load(file)

    p.download()

    with open('data.pickle', 'wb') as file:
        pickle.dump(p, file)
