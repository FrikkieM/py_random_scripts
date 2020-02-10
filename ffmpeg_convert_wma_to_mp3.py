import subprocess
import os, glob

input_files = glob.glob('./*.wma')

def spawnChildProcess(cmds=[]):
    subprocess.Popen(cmds)

def convertWMAToMP3(audio_input, audio_output):
    cmds = ['ffmpeg', '-i', audio_input, '-ab', '192k', '-f', 'mp3', audio_output]
    spawnChildProcess(cmds)

def runProgram():
    for input_file in input_files:
        output_file = os.path.splitext(input_file)[0] + '.mp3'
        if os.path.exists(output_file):
            pass
        else:
            convertWMAToMP3(input_file,output_file)
        #os.remove(input_file)

print('Converting files. This may take a few minutes. Please wait...')

runProgram()