import os
import subprocess

def subprocess_function(input_file, name, ext):
    
    output_path = "audio"
    input_path = os.path.join("audio", input_file)
    #os.path.join joins an element to the pathname
    new_path = os.path.join("audio", f"{name}.mp3")
    subprocess.run([
    "ffmpeg",
    "-i", input_path,
    "-ar", "44100",
    "-ac", "2",
    "-b:a", "192K",
    f"{output_path}/{name}.mp3"
    ],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.STDOUT)
    #these two remove the logs from the subprocess
    if os.path.exists(new_path) == True:
        os.remove(input_path)
        print(f"{name+ext}: converted to {name}.mp3")
    else:
        print("not a file")

def sound_tag_generator(name):
    return f"[sound:{name}.mp3]"

def sentence_or_word_audio(name):
    if name.startswith("yomitan_audio_"):
        return "WordAudio"
    else:
        return "SentenceAudio"

audio_extensions = (".ogg",".opus",".oga")
#this is a tuple, its contents won't ever change essentially

input_folder = os.listdir("audio")
#turns the folder into an array
files_to_convert = 0

with open("log.txt", "w", encoding="utf-8") as log:
    for input_file in input_folder:
        if not input_file.endswith(audio_extensions):
            continue
        name, ext = os.path.splitext(input_file)
        #whitelists what i actually need
        subprocess_function(input_file, name, ext)
        files_to_convert+=1
        sound_tag = sound_tag_generator(name)
        type_check = sentence_or_word_audio(name)
        log.write(f"{type_check}|{input_file}|{name}.mp3\n")
        dictionary = {
            "soundtype": f"{type_check}",
            "original_file": f"{input_file}",
            "new_file": f"{name}.mp3"
        }
        log.write(f"{dictionary}\n")
print(f"converted files: {files_to_convert}")



#5687 files currently in the ANKI FOLDER


