from vvclient import Client
import asyncio

async def audio_generation(sentence):
    character_id = 2
    async with Client() as client:
        audio_query = await client.create_audio_query(
            sentence, speaker=character_id
        )
        with open(f"{sentence}.wav", "wb") as f:
            f.write(await audio_query.synthesis(speaker=character_id))

async def main():
    sentence = input("enter a sentence to text generate it: ")
    audio_generation(sentence)
    #id of chosen speaker in this case its zundamon

if __name__ == "__main__":
    asyncio.run(main())