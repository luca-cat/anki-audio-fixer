import requests

def convert_audio(value):
    if not value:
        return value.strip()
    return value.replace(".ogg", ".mp3").replace(".opus", ".mp3")

url = "http://localhost:8765"

deck_name = "sentencemining"


response = requests.post(url, json={
    "action": "findNotes",
    "version": 6,
    "params": {"query": f"deck:{deck_name}"}
})

note_ids = response.json()["result"]

for note_id in note_ids:
    response_note = requests.post(url, json={
    "action": "notesInfo",
    "version":6,
    "params":{
        "notes":[note_id]
    }
    })
    fields = response_note.json()["result"][0]["fields"]
    sentence_audio = fields["SentenceAudio"]["value"]
    word_audio = fields["WordAudio"]["value"]
    
    sentence_audio = convert_audio(sentence_audio)
    word_audio = convert_audio(word_audio)

    print(sentence_audio)
    print(word_audio)
    
    response_note = requests.post(url, json={
    "action": "updateNoteFields",
    "version": 6,
    "params": {
        "note": {
            "id": note_id,
            "fields": {
                "WordAudio":word_audio,
                "SentenceAudio":sentence_audio
            }
        }
    }
})
