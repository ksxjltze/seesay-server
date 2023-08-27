import os
import openai
import replicate
from gtts import gTTS
import webbrowser

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

    # translate the reply
    language = 'zh'
    language_dictionary = {
        "zh": "Chinese",
        "en": "English",
        "ms": "Malay",
        "hi": "Hindi",
        "pt": "Portuguese"
    }
    if (language != "en"):
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Translate the following into " + language_dictionary[language] + " without extraneous words: " + output}])
        output = completion.choices[0].message.content

    print("Translated Explanation:")
    print(output)

    # text to speech
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("welcome.mp3")

    # play audio
    webbrowser.open("welcome.mp3")

    return output
