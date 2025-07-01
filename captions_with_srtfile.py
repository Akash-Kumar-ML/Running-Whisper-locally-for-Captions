import whisper

model = whisper.load_model("base")

result = model.transcribe("1234audio.wav")  

def write_srt(segments, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(segments, start=1):
            start = segment["start"]
            end = segment["end"]
            text = segment["text"].strip()

            def format_time(t):
                hours = int(t // 3600)
                minutes = int((t % 3600) // 60)
                seconds = int(t % 60)
                milliseconds = int((t * 1000) % 1000)
                return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

            f.write(f"{i}\n")
            f.write(f"{format_time(start)} --> {format_time(end)}\n")
            f.write(f"{text}\n\n")

write_srt(result["segments"], "output555.srt")
