#All the functions on this module are made to be used with the fast edition functionality, where you put
# all the videos in one folder and the program will return a final video combining all these videos.

#All imports needed to accomplish the tasks in each step
import time
import os
from moviepy.editor import *
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate

#Order videos by creation date.
def OrderVideosF(path='C:/Users/hp/PycharmProjects/Editor_de_Videos/Videos/'):
    dir = os.listdir(path)
    clips_dt = []
    ordered_dt = []
    ordered_clips = []

    #1st part - order the creation date of the videos in a new list.
    for vids in dir:
        try:
            creation_date = os.stat(f'C:/Users/hp/PycharmProjects/Editor_de_Videos/Videos/{vids}').st_mtime
            clips_dt.append(creation_date)
        except:
            print('There´s no more videos in the folder.')

    ordered_dt = sorted(clips_dt)

    #2nd part - order the videos in a new list comparing the previously created list and the original folder.
    while len(ordered_clips) < len(dir):
        #As I´ll be comparing 2 lists ("ordered_dt" and "dir") I have to use two "for" loops, in order to compare each
        # element of the first list with each element of the second list.
        for v in ordered_dt:
            for vids in dir:
                #In this line we compare the creation dates of the videos in the folder
                # with the creation dates that we have on the list "ordered_dt".
                # If the creation date mach on both it´ll append this video to the list
                # "ordered_clips" in chronological order.
                if time.ctime(os.stat(f'C:/Users/hp/PycharmProjects/Editor_de_Videos/Videos/{vids}').st_mtime) == time.ctime(v):
                    ordered_clips.append(vids)
                else:
                    pass
    print(ordered_clips)
    return ordered_clips


#Convert videos to MoviePy object.
def VideoConverterF(ordered_clips, path='C:/Users/hp/PycharmProjects/Editor_de_Videos/Videos/'):
    clips_converted = []
    print('Your videos are being converted...')
    for clip in ordered_clips:
        clip = VideoFileClip(path + clip)
        clips_converted.append(clip)
    print(clips_converted)
    return clips_converted


#Rotate videos that were recorded upside down.
def Rotate180(path='C:/Users/hp/PycharmProjects/Editor_de_Videos/Videos Invertidos/'):
    print('Your videos are being rotated...')
    directory = os.listdir(path)
    for clip in directory:
        vid_file = VideoFileClip(path + clip)
        rotate(vid_file, 180).write_videofile(clip)


#Resize all videos to 720p, so there´s no incompatibility on the final assembly.
def ResizeF(clips_converted):
    clips_resized = []
    print('Your videos are being resized to 720p...')
    for clip in clips_converted:
        clip = resize(clip, height=720)
        clips_resized.append(clip)
    print(clips_resized)
    return clips_resized


#Cut each video with the same criteria.
#Obs.: Obviously cutting the video like this won´t necessarily obtain the best parts.
def VariousVideosCutF(clips_resized):
    final_clips = []
    print('Your videos are being automatically cuted...')
    for clip in clips_resized:
        #Here we are using a subjective inicial time cut of 20% of the total time of the video
        t_ini = clip.duration * 0.20
        #Here we are using a subjective final time cut of 50% of the total time of the video
        t_fim = clip.duration * 0.50
        clip = clip.subclip(t_ini, t_fim)
        final_clips.append(clip)
    print(final_clips)
    return final_clips


#Final assembly of all ordered and treated videos and naming of the compilation output video.
def FinalClipsAssemblyF(final_clips, clip_name='Result Clip'):
    clip_name = input('Enter the name of your video:')
    print('We are assembling your final video...')
    result_clip = concatenate_videoclips(final_clips)
    result_clip.write_videofile(clip_name + '.mp4')