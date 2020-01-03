#Extracts audio from WEBM and MP4 Files to MP3 files

import subprocess
import os, glob

in_files_webm = glob.glob('./*.webm')
in_files_mp4 = glob.glob('./*.mp4')
in_files = in_files_mp4 + in_files_webm

def spawnChildProcess(cmds=[]):
    subprocess.Popen(cmds)

def extractMP3(file_input, file_output):
    cmds = ['ffmpeg', '-i', file_input, '-vn', '-ab', '192k', '-ar', '44100', '-y', file_output]
    spawnChildProcess(cmds)

def runProgram():
    for in_file in in_files:
        out_file = os.path.splitext(in_file)[0] + '.mp3'
        if os.path.exists(out_file):
            pass
        else:
            extractMP3(in_file,out_file)
            
print('Extracting MP3 files from multiple sources...')

runProgram()
