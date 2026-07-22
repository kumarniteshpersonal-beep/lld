# Interface segregation principle - states that clients should not be forced to depend on interfaces they do not use.
from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def play_audio(self, file):
        pass

    @abstractmethod
    def play_video(self, file):
        pass

class AudioPlayer(MediaPlayer):
    def play_audio(self, file):
        print(f"Playing audio file: {file}")

    # MediaPlayer interface is forcing me to implement play_video method which I don't need, this violates the Interface Segregation Principle
    def play_video(self, file):
        raise NotImplementedError("AudioPlayer cannot play video files")

class VideoPlayer(MediaPlayer):
    # MediaPlayer interface is forcing me to implement play_audio method which I don't need, this violates the Interface Segregation Principle
    def play_audio(self, file):
        raise NotImplementedError("VideoPlayer cannot play audio files")

    def play_video(self, file):
        print(f"Playing video file: {file}")

# problems:
# 1. The MediaPlayer interface is forcing the AudioPlayer and VideoPlayer classes to implement methods that they do not need, which violates the Interface Segregation Principle. 


