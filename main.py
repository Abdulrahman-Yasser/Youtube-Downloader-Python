import pickle

SAVE_FILE = "D:\_Study_A\my_refresh_music"

from my_youtube_handler.my_youtube import my_PlaylistDownloader

if __name__ == '__main__':
    with open('data.pickle', 'rb') as file:
        p : my_PlaylistDownloader = pickle.load(file)

    p.download()

    with open('data.pickle', 'wb') as file:
        pickle.dump(p, file)
