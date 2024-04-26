import subprocess
import os

def check_if_wav(file):
    if file.endswith(".wav"):
        return file
    else: 
        wav_file = convert_audio_to_wav(file)
        return wav_file


def convert_audio_to_wav(audio_file_path):
    wav_file_path = os.path.splitext(audio_file_path)[0] + ".wav"
    wav_file = subprocess.run(["ffmpeg", "-i", audio_file_path, "-acodec", "pcm_s16le", "-ar", "16000", wav_file_path])
    return wav_file

if __name__ == "__main__":
    audio_file_path = "" #Enter path of the file not converted to wav here

    check_if_wav(audio_file_path)
   
