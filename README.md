
## Introduction

This Python application seamlessly integrates Text-to-Speech (TTS) and Speech-to-Text (STT) functionalities with text translation capabilities. It is designed to run in a terminal environment, where it takes an audio file as input, converts the speech to text, translates the text into a specified language, converts the translated text back into speech, and finally plays the translated audio.


## Installation

Install the required Python libraries using pip:
```bash
pip install -r requirements.txt
```


## Usage

### Running the Application

Execute the script from the terminal with the audio file path as an argument:
```bash
python src/app.py sample/speech.mp3
```


### Steps
1. **Speech to Text**: The application first converts the speech from the audio file into text.
2. **Translation**: The text is then translated into the language specified by the user.
3. **Text to Speech**: The translated text is converted back into speech.
4. **Play Audio**: The application plays the translated speech.


## Demo

https://youtu.be/nz-C-0dLdB0
