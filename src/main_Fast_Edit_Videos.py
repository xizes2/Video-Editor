#Main program to chronologicaly order, convert, resize everything to the same size, cut and assemble everything in one video.

#Import OS to manage the folder used to hold the videos
#Import the custom made module functions to manage the tasks needed to assemble the final video
from os import listdir
from video_editor_functions import fast_edit_functions

#Loop through the video files in the folder selected to process each video and make the final assemble.
while True:
    path = 'D:\Fernando\Programming\Personal Projects\Editor_de_Videos\Videos'
    dir = listdir(path)
    if len(dir) == 0:
        print('There´s no videos on the directory.')
        break
    else:
        a = fast_edit_functions.OrderVideosF()
        b = fast_edit_functions.VideoConverterF(a)
        c = fast_edit_functions.ResizeF(b)
        d = fast_edit_functions.VariousVideosCutF(c)
        fast_edit_functions.FinalClipsAssemblyF(d)
    break












