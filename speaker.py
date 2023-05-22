from gtts import gTTS
import os
import pygame

def TextToSpeech(text):
    # Create gTTS object
    tts = gTTS(text)

    # Save the audio file
    output_file = "output.mp3"
    tts.save(output_file)

    # Initialize the mixer module
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load(output_file)

    # Play the audio file
    pygame.mixer.music.play()

    # Wait until playback is finished
    while pygame.mixer.music.get_busy():
        continue

    # Delete the output file
    os.remove(output_file)
