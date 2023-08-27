import os
import openai
import replicate
import pyttsx3 

def describe_image(file_path, token, prompt):
    replicate_client = replicate.Client(api_token=token)
    output = replicate_client.run(
        "daanelson/minigpt-4:b96a2f33cc8e4b0aa23eacfce731b9c41a7d9466d9ed4e167375587b54db9423",
        input={"image": open(file_path, "rb"),
            "prompt": prompt}
    )
    return output

def speech_to_text(file_path, token):
    speech_path = file_path

    # get text from speech 
    openai.api_key = token
    f = open(speech_path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", f, language="en")
    return transcript["text"]

def text_to_speech(text):
    # text to speech
    engine = pyttsx3.init() # object creation
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    engine.runAndWait()

    # print output for debugging
    print(text)
