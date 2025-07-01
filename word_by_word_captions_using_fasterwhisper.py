import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from faster_whisper import WhisperModel


model_size = "large-v3"
model = WhisperModel(model_size, compute_type="int8")


segments, _ = model.transcribe("1234audio.wav", word_timestamps=True)


def format_srt_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


with open("output666.srt", "w", encoding="utf-8") as f:
    index = 1
    for segment in segments:
        for word in segment.words:
            start = word.start
            end = word.end
            text = word.word.strip()
            if text:
                f.write(f"{index}\n")
                f.write(f"{format_srt_time(start)} --> {format_srt_time(end)}\n")
                f.write(f"{text}\n\n")
                index += 1
