import subprocess
import os, glob

wav_files = glob.glob('./*.wav')

def spawnChildProcess(cmds=[]):
    subprocess.Popen(cmds)

def convertWavToMP3(audio_input, audio_output):
    cmds = ['ffmpeg', '-i', audio_input,'-ac','1', '-ab', '192k', '-f', 'mp3', audio_output]
    spawnChildProcess(cmds)

def runProgram():
    for wav_file in wav_files:
        mp3_file = os.path.splitext(wav_file)[0] + '.mp3'
        if os.path.exists(mp3_file):
            pass
        else:
            convertWavToMP3(wav_file,mp3_file)
        #os.remove(wav_file)

print('Converting WAV files in current folder to MP3 MONO. This may take a few minutes. Please wait...')

runProgram()