import os
import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import wavio as wv
import constants
import openai
import replicate
import pyttsx3 
import cv2


cam_port = 0
cam = cv2.VideoCapture(cam_port)
  
cv2.namedWindow("test")

img_counter = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "captured.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

# get image
image_path = os.path.dirname(__file__) +  "/captured.png"

# record speech
sampling_frequency = 44100
duration = 10
recording = sd.rec(int(duration * sampling_frequency),
                    samplerate=sampling_frequency,
                    channels=1)  # Adjust channels as needed (1 or 2)
print("Starting: Speak now!")
sd.wait()
print("finished")
write("recording0.wav", sampling_frequency, recording)

speech_path = os.path.dirname(__file__) + "/recording0.wav"

# get text from speech 
openai.api_key = constants.OPENAI_API_KEY
f = open(speech_path, "rb")
transcript = openai.Audio.transcribe("whisper-1", f, language="en")

# explain image
replicate_client = replicate.Client(api_token=constants.REPLICATE_API_KEY)
output = replicate_client.run(
    "daanelson/minigpt-4:b96a2f33cc8e4b0aa23eacfce731b9c41a7d9466d9ed4e167375587b54db9423",
    input={"image": open(image_path, "rb"),
           "prompt": transcript["text"]}
)
print(output)
# text to speech
engine = pyttsx3.init() # object creation
engine.say(output)
engine.runAndWait()
engine.stop()
engine.runAndWait()

# print output for debugging
print(output)