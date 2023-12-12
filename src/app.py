import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import pygame
import sys
import os
import logging
from pydub import AudioSegment

# Initialize logging
logging.basicConfig(level=logging.INFO)

def speech_to_text(audio_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text
    except Exception as e:
        logging.error(f"Error in speech recognition: {e}")
        sys.exit(1)

def translate_text(text, target_lang='en'):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_lang)
        return translation.text
    except Exception as e:
        logging.error(f"Error in translation: {e}")
        sys.exit(1)

def text_to_speech(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        filename = 'translated_speech.mp3'
        tts.save(filename)
        return filename
    except Exception as e:
        logging.error(f"Error in text-to-speech: {e}")
        sys.exit(1)

def play_audio(file_path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        logging.error(f"Error in playing audio: {e}")
        sys.exit(1)

def convert_audio_format(audio_path, target_format="wav"):
    try:
        sound = AudioSegment.from_file(audio_path)
        converted_path = "converted_audio." + target_format
        sound.export(converted_path, format=target_format)
        return converted_path
    except Exception as e:
        logging.error(f"Error in audio format conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logging.info("Usage: python app.py <path_to_audio_file>")
        sys.exit(1)

    audio_path = sys.argv[1]
    if not os.path.exists(audio_path):
        logging.error("Audio file does not exist.")
        sys.exit(1)

    # Convert audio to a compatible format if necessary
    if not audio_path.endswith(".wav"):
        logging.info("Converting audio to a compatible format...")
        audio_path = convert_audio_format(audio_path)

    logging.info("Converting speech to text...")
    text = speech_to_text(audio_path)
    logging.info(f"Original Text: {text}")

    target_language = input(f"Translate to ({'/'.join(LANGUAGES.keys())}): ")
    logging.info("Translating text...")
    translated_text = translate_text(text, target_lang=target_language)
    logging.info(f"Translated Text: {translated_text}")

    logging.info("Converting translated text to speech...")
    speech_file = text_to_speech(translated_text, lang=target_language)

    logging.info("Playing translated speech...")
    play_audio(speech_file)
