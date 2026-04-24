import os
import subprocess

def subprocess_function(input_file):
    
    output_path = "audio"
    input_path = os.path.join("audio", input_file)
    #os.path.join joins an element to the pathname
    file_name = os.path.splitext(input_file)
    subprocess.run([
    "ffmpeg",
    "-i", input_path,
    "-ar", "44100",
    "-ac", "2",
    "-b:a", "192K",
    f"{output_path}/{file_name[0]}.mp3"
    ],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.STDOUT)
    #these two remove the logs from the subprocess
    if os.path.exists(output_path) == True:
        os.remove(input_path)
        print(f"{file_name[0]+file_name[1]}: converted to {file_name[0]}.mp3")

    else:
        print("not a file")


audio_extensions = (".ogg",".opus")
#this is a tuple, its contents won't ever change essentially

input_folder = os.listdir("audio")
#turns the folder into an array
files_to_convert = 0
for input_file in input_folder:
    print()
    if not input_file.endswith(audio_extensions):
        continue
    #whitelists what i actually need
    subprocess_function(input_file)
    files_to_convert+=1
print(f"converted files: {files_to_convert}")

#5687 files currently in the ANKI FOLDER


