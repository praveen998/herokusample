from gtts import gTTS
from pydub import AudioSegment

# Define the text you want to convert to speech
def google_text_sound(text):
    #text = "Hello, Praveen,hello world"
    # Create a gTTS object
    print(text)
    tts = gTTS(text=text, lang='en')
    # Save the speech to a file in MP3 format
    mp3_filename = "testtospeech.mp3"
    tts.save(mp3_filename)
    # Convert the MP3 file to WAV format
    wav_filename = "testtospeech.wav"
    sound = AudioSegment.from_mp3(mp3_filename)
    sound.export(wav_filename, format="wav")
    print("Conversion to WAV format completed!")
    