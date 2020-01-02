#Converts MP4 Files to WMV Files with same quality
#Filenames should not contain spaces - don't have time double check naming issues...

import subprocess
import os, glob

in_files = glob.glob('./*.mp4')

def spawnChildProcess(cmds=[]):
    subprocess.Popen(cmds)

def convertMP4ToWMV(file_input, file_output):
    cmds = ['ffmpeg', '-i', file_input,'-qscale','0', file_output]
    spawnChildProcess(cmds)

def runProgram():
    for in_file in in_files:
        out_file = os.path.splitext(in_file)[0] + '.wmv'
        if os.path.exists(out_file):
            pass
        else:
            convertMP4ToWMV(in_file,out_file)
        #os.remove(wav_file)

print('Converting MP4 to WMV')

runProgram()