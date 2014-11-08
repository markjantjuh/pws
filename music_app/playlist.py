__author__ = 'MarkJan'
import json, os

def createPlaylist(name):
    new_playlist = {'name' : name}

    playlist_name = "output\playlist_files\\" + name + ".txt"#create file name for playlist

    playlist_file = open(playlist_name, "w") #open playlistfile
    json.dump(new_playlist, playlist_file) #convert dict into json and write to file
    playlist_file.close() #close playlistfile

def getPlaylist(playlist_path):
    playlist_file = open(playlist_path, 'r')
    playlist_data = json.load(playlist_file)
    playlist_file.close()

    return playlist_data

def editPlaylist(playlist_path, music_file_path):
    playlist_data = getPlaylist(playlist_path)
    music_file_name = os.path.splitext(music_file_path)[0]

    playlist_data[music_file_name] = music_file_path

    playlist_file = open(playlist_path, "w") #open playlistfile
    json.dump(playlist_data, playlist_file) #convert dict into json and write to file
    playlist_file.close() #close playlistfile


