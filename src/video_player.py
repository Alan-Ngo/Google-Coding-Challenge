"""A video player class."""

from src import video
from .video_library import VideoLibrary
import random
import math

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playing = ""
        self._pause = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        videos = sorted(videos, key=lambda x: x._title)
        for video in videos:
            tags = []
            for tag in video._tags:
                tags.append(tag)

            print(video._title + " (" + video._video_id + ") " +  "["+ ",".join(tags) + "]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        for video in self._video_library.get_all_videos():
            if(video._video_id == video_id):
                if(self._playing!=""):
                    print("Stopping video: " + self._playing._title)
                self._playing = video
                print("Playing video: " + self._playing._title)
                return
        
        print("Cannot play video: Video does not exist")
        

    def stop_video(self):
        """Stops the current video."""
        if(type(self._playing) is not type("")):
            print("Stopping video: " + self._playing._title)
            self._playing = ""
            self._pause == False
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        vidInd = math.ceil(random.random() * len(self._video_library.get_all_videos()))
        
        if(type(self._playing) is not type("")):
            print("Stopping video: " + self._playing._title)
            self._playing = ""
            
        self._playing = self._video_library.get_all_videos()[vidInd-1]
        print("Playing video: " + self._playing._title)

    def pause_video(self):
        """Pauses the current video."""
        if(self._pause == False and type(self._playing) is not type("")):
            self._pause = True
            print("Pausing video: " + self._playing._title)
        elif(self._pause == True and type(self._playing) is not type("")):
            print("Video already paused: " + self._playing._title)
            self._pause == False
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if(self._pause == True and type(self._playing) is not type("")):
             print("Continuing video: " + self._playing._title)
             self._pause = False
        elif(self._pause == False and type(self._playing) is not type("")):
            print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        #print("Currently playing: " + self._playing._title)

        tags = []
        for tag in self._playing._tags:
            tags.append(tag)

        if(self._pause):
            print("Currently playing: " + self._playing._title + " (" + self._playing._video_id + ") " +  "["+ ",".join(tags) + "]")
        else:
            print("Currently playing: " + self._playing._title + " (" + self._playing._video_id + ") " +  "["+ ",".join(tags) + "] - PAUSED")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
