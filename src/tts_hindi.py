import os
import torch
from TTS.api import TTS

# Ensure TTS license agreement is set
os.environ["COQUI_TOS_AGREED"] = "1"

def text_to_speech(text, output_file="output.wav", speaker_audio=None):
    """
    Converts text into Hindi speech using an open-source TTS model.
    
    Parameters:
    - text (str): The input text to be converted to speech.
    - output_file (str): The filename to save the output audio.
    - speaker_audio (str, optional): Path to a reference speaker audio file for voice cloning.

    Returns:
    - output_file (str): The path to the saved audio file.
    """
    print("🔄 Loading TTS model...")
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cpu")

    print("✅ Model loaded successfully!")

    print(f"🔄 Generating speech for: {text}")
    tts.tts_to_file(
        text=text,
        file_path=output_file,
        speaker_wav=speaker_audio,  # ✅ Use reference audio for voice cloning
        language="hi"
    )

    print(f"✅ Speech saved successfully at: {output_file}")
    return output_file

# Example usage
if __name__ == "__main__":
    sample_text = "hi how are you!"
    speaker_audio = "D:/AI-Project/news-sentiment-tts/src/sample_speaker.wav"  # Use a valid .wav file
    text_to_speech(sample_text, "hindi_speech.wav", speaker_audio)
