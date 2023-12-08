import os
import subprocess
import sys
import shutil
import threading

threads = []

def create_sub(file):
    os.system("SubtitleEdit /convert \""+file+"\" srt")

def vid_sub(source_folder):
    for filename in os.listdir(source_folder):
        if filename.endswith(".mkv") or filename.endswith(".mp4"):
            threads.append(threading.Thread(target=create_sub, args=(os.path.join(source_folder,filename),)))

def vid_sub_wrapper(series_folder):
    for filename in os.listdir(series_folder):
        if os.path.isdir(os.path.join(series_folder,filename)):
            vid_sub(os.path.join(series_folder, filename))


            
            

if __name__ == "__main__":
    print(sys.argv[1])
    vid_sub_wrapper(sys.argv[1])
    jobs_complete = 0
    for i in threads:
        i.start()
        i.join()
