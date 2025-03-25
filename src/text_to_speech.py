import soundfile as sf



print("✅ File converted successfully: ref_fixed.wav (22050 Hz, Mono)")


file_path = "ref20.wav"

try:
    with sf.SoundFile(file_path) as f:
        print(f"✅ File loaded successfully: {file_path}")
        print(f"Sample Rate: {f.samplerate} Hz")
        print(f"Channels: {f.channels}")
        print(f"Format: {f.format}, Subtype: {f.subtype}")
except Exception as e:
    print(f"❌ Error: {e}")
