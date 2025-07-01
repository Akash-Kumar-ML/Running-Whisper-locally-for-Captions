import whisper

model = whisper.load_model("large")

audio_path = "1234audio.wav"  

result = model.transcribe(audio_path, verbose=True)

whisper.utils.write_srt(result["segments"], open("output555.srt", "w", encoding="utf-8"))

print("Transcription complete")
