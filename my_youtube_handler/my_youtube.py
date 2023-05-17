from pytube import Playlist
from pytube import YouTube

class my_PlaylistDownloader:
    def __init__(self, my_url, SAVE_FILE, OldLength = 0):
        self.my_url = my_url
        self.OldLength = OldLength
        self.broken_url = []
        self.SAVE_FILE = SAVE_FILE

    def check(self):
        p = Playlist(self.my_url)
        try:
            new_OldLength = p.length
        except ValueError:
            print(p.length)
            new_OldLength = 1
        if new_OldLength == self.OldLength:
            return False
        else:
            return True
        
    def download(self):
        p = Playlist(self.my_url)
        if len(self.broken_url) > 0:
            print("Take care !! you have some broken url\n")
        if self.check():
            NewLength = p.length
            if self.OldLength > NewLength:
                return False
            for video,url in ((videoo, urll) for videoo in p.videos[self.OldLength : NewLength] for urll in p.video_urls[self.OldLength : NewLength])  :
                try:
                    aud = video.streams.filter(only_audio=True).last().download(self.SAVE_FILE)
                except:
                    self.broken_url.append(url)
                    print("Some error")
            self.OldLength = NewLength
            return True
        else:
            return False
        
    def showAllBrokenUrl(self):
        for i in self.broken_url:
            print(i)
    
    def download_brokenUrl(self):
        for i in self.broken_url:
            y = YouTube(i)
            try:
                y.streams.filter(only_audio=True).last().download(self.SAVE_FILE)
                self.broken_url.clear(i)
            except:
                print("Still not fixed",i)

    def showAllVideos(self):
        p = Playlist(self.my_url)
        videos = p.url_generator()
        for vid in videos:
            print(vid)


