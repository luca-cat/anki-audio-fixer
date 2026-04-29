import requests

def convert_audio(value):
    if not value:
        return value
    #if value is empty it returns the original empty value
    if ".mp3" in value:
        return value
    #if .mp3 already present it returns the original value
    print(f"converting {value}")
    return value.replace(".ogg", ".mp3").replace(".opus", ".mp3").replace(".oga", ".mp3")
    #any other cases will cause this return function to run

def anki(action, params):
    try:
        response = requests.post(url, json={
            "action": action,
            "version":6,
            "params": params
        })
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Is Anki Open?")
        exit()
#turns the response request into a function named anki

url = "http://localhost:8765"

deck_name = input("input deck name: ")

note_ids = anki("findNotes", {"query": f"deck:{deck_name}"})["result"]

choice = input("would you like to proceed? ").lower()
if choice == "yes":

    for note_id in note_ids:
        
        notes = anki("notesInfo", {"notes": [note_id]})
        fields = notes["result"][0]["fields"]
        sentence_audio = fields["SentenceAudio"]["value"]
        word_audio = fields["WordAudio"]["value"]
        
        new_sentence_audio = convert_audio(sentence_audio)
        new_word_audio = convert_audio(word_audio)

        if word_audio != new_word_audio or sentence_audio != new_sentence_audio:

            anki("updateNoteFields", {
                "note": {
                    "id": note_id,
                    "fields": {
                        "WordAudio":new_word_audio,
                        "SentenceAudio":new_sentence_audio
                    }
                }
            })
elif choice == "no":
    pass
else:
    print("not a choice")