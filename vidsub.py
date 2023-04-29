import os
import subprocess
import sys
import shutil

def vid_sub(source_folder):
    subs_folder = source_folder+"\\Subs"
    for filename in os.listdir(source_folder):
        if filename.endswith(".mp4"):
            print(filename)
            subsFile=subs_folder+"\\"+filename[:-4]+"\\4_English.srt"
            backup_sub=subs_folder+"\\"+filename[:-4]+"\\3_English.srt"
            backup_backup_sub=subs_folder+"\\"+filename[:-4]+"\\2_English.srt"
            backup_backup_backup_sub=subs_folder+"\\"+filename[:-4]+"\\5_English.srt"
            subFileCopy=source_folder+"\\"+filename[:-4]+".srt"
            print(subsFile)
            print(subFileCopy)
            try:
                try:
                    shutil.copy(subsFile,subFileCopy)
                except:
                    shutil.copy(backup_sub,subFileCopy)
            except:
                try:
                    shutil.copy(backup_backup_sub,subFileCopy)
                except:
                    shutil.copy(backup_backup_backup_sub,subFileCopy)

def vid_sub_wrapper(series_folder):
    for filename in os.listdir(series_folder):
        if os.path.isdir(os.path.join(series_folder,filename)):
            vid_sub(os.path.join(series_folder, filename))


            
            

if __name__ == "__main__":
    print(sys.argv[1])
    vid_sub_wrapper(sys.argv[1])