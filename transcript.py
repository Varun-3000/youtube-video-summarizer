import yt_dlp
import os
import uuid

from faster_whisper import WhisperModel

TEMP_FOLDER = "temp"

model = WhisperModel(
    "tiny",
    device="cpu",
    compute_type="int8"
)


def download_audio(youtube_url):

    if not os.path.exists(TEMP_FOLDER):
        os.makedirs(TEMP_FOLDER)

    unique_id = str(uuid.uuid4())

    output_path = os.path.join(
        TEMP_FOLDER,
        f"{unique_id}.%(ext)s"
    )

    ydl_opts = {
        'format': 'worstaudio',
        'outtmpl': output_path,
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    for file in os.listdir(TEMP_FOLDER):
        if file.startswith(unique_id):
            return os.path.join(TEMP_FOLDER, file)

    return None


def transcribe_audio(audio_path):

    segments, info = model.transcribe(audio_path)

    transcript = ""

    for segment in segments:
        transcript += segment.text + " "

    if os.path.exists(audio_path):
        os.remove(audio_path)

    return transcript


def get_transcript(youtube_url):

    audio_path = download_audio(youtube_url)

    transcript = transcribe_audio(audio_path)

    return transcript