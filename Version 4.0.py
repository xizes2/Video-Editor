from os import listdir
from video_editor_functions import fast_edit_functions

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












