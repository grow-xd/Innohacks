from gtts import gTTS
import os
from datetime import datetime
import pygame
import time

# Get the current date and time
current_datetime = datetime.now()

# Format the date and time to create a unique file name
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

# Create the file name
file_name = f"output_{formatted_datetime}.mp3"

def convert_text_to_speech(text, lang='hi', output_file=file_name):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_file)
    return output_file

def play_mp3(mp3_filename):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    text_to_convert = "आपका स्वागत है! यह एक हिंदी टेक्स्ट-टू-स्पीच कनवर्टर है।"
    
    # Convert text to speech and save it to an audio file
    audio_file_path = convert_text_to_speech(text_to_convert)

    # Play the created MP3 file
    play_mp3(audio_file_path)