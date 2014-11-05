__author__ = 'MarkJan'

#imports
import json
import os
from os.path import basename

def open_library(path):
    #returns dictionary which contains references to tagfiles

    library_file = open(path, "r") #open libraryfile
    library = json.load(library_file) #convert json to dict
    library_file.close() #close libraryfile

    return library #return the dictionary

def generate_library(rootdir):
    #generates new library


    new_lib = {} # create new library dict

    # loop trough directory to get music files
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.mp3'): #for every music file, write tag file
                writeTagFile(os.path.join(subdir, file))
                new_lib[basename(os.path.splitext(file)[0])] = "output\\tag_files\\" + basename(os.path.splitext(file)[0] + ".txt") #add new tagfile to library


    library_file_name = "output\library_files\\" + basename(os.path.splitext(rootdir)[0] + ".txt") #create file name for library

    library_file = open(library_file_name, "w") #open libraryfile
    json.dump(new_lib, library_file) #convert dict into json and write to file
    library_file.close() #close libraryfile

def writeTagFile(path, genre = None, song_title = None, artist = None, album = None, year = None, bpm = None, key = None, info = None):
    #create files that contains information about music file

    file_extension = os.path.splitext(path)[1] #get file extension
    tag_file_name = "output\\tag_files\\" + basename(os.path.splitext(path)[0] + ".txt") #create file name

    #create dictionairy that contains all info
    data_dict = {'Path'       : path,
                 'Extension'  : file_extension,
                 'Genre'      : genre,
                 'Song Title' : song_title,
                 'Artist'     : artist,
                 'Album'      : album,
                 'Year'       : year,
                 'BPM'        : bpm,
                 'Key'        : key,
                 'Info'       : info}

    tag_file = open(tag_file_name, "w") #open tagfile
    json.dump(data_dict, tag_file) #convert dict into json and write to file
    tag_file.close() #close tagfile

    print "Wrote file:", tag_file_name

def readTagFile(tag_file_name):
    #read tag file and return dict with data

    tag_file = open(tag_file_name, "r")
    tag_file_data = json.load(tag_file)
    tag_file.close()

    return tag_file_data

def edit_tags(file, tag, new_data):
    #edit the tag file

    tag_file_data = readTagFile(file)
    tag_file_data[tag] = new_data

    tag_file = open(file, "w")
    json.dump(tag_file_data, tag_file)
    tag_file.close()


