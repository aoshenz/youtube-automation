import logging
import pathlib
import random
from gtts import gTTS

from moviepy.editor import (
    CompositeVideoClip,
    TextClip,
    VideoFileClip,
    concatenate_videoclips,
    ImageClip,
    ImageSequenceClip,
    AudioFileClip,
    CompositeAudioClip,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


class Movie:
    def __init__(self, folder: str, bg_video: str = 'background.mp4'):
        self.folder = folder
        self.bg_video = bg_video

    def tts(self, text: list):
        """
        Create text-to-speech audio files for each iteration in list.
        """
        language = "en"
        domain = "com"

        pathlib.Path(f"files/{self.folder}/audio").mkdir(parents=True, exist_ok=True)
        output_folder = f"files/{self.folder}/audio"

        logging.info(f"Creating {len(text)} audio clips.")

        for i in range(len(text)):
            audio = gTTS(text=text[i], tld=domain, lang=language, slow=False)

            output_file = f"{output_folder}/audio_{i}.mp3"
            audio.save(output_file)

        logging.info(f"Audio clips saved in {output_folder}")

        self.num_audio = len(text)

    def append_audio(self):
        """Append all text to speech audio and record duration of each clip."""

        logging.info("Appending audio clips.")

        audio_files = [
            f"files/{self.folder}/audio/audio_{i}.mp3" for i in range(self.num_audio)
        ]

        audio_duration = {}
        audio_sound = []
        for i in range(len(audio_files)):

            if i == 0:
                start = 0
            else:
                start = sum(audio_duration.values())

            audio_i = AudioFileClip(audio_files[i]).set_start(start)

            audio_duration[i] = audio_i.duration
            audio_sound.append(audio_i)

        self.audio = CompositeAudioClip(audio_sound)
        self.audio_duration = audio_duration
        self.audio_total_duration = sum(self.audio_duration.values())

    def create_movie(self):
        """Overlay text screenshots on background video."""

        logging.info("Overlaying text screenshots on background video.")

        background = VideoFileClip(f"files/{self.folder}/{self.bg_video}", audio=False)

        img_path = pathlib.Path(f"files/{self.folder}/img").glob('**/*png')
        files = [str(p) for p in img_path]
        files.sort()

        text_clips = []
        start_time = 0
        for f in range(len(files)):

            clip_duration = self.audio_total_duration - start_time
            x_pos = random.uniform(0.05, 0.3)
            y_pos = random.uniform(0.05, 0.6)

            img = (
                ImageClip(files[f])
                .set_start(start_time)
                .set_duration(clip_duration)
                .resize(0.6)
                .set_position((x_pos, y_pos), "relative")
            )

            start_time = start_time + self.audio_duration[f]

            text_clips.append(img)

        movie = CompositeVideoClip([background] + text_clips)
        self.movie = movie.set_audio(self.audio)

    def output_movie(self):
        """Output movie."""

        logging.info(f"Outputting movie.")

        self.movie.write_videofile(
            f"files/{self.folder}/movie.mp4",
            codec="libx264",
            audio_codec="aac",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
        )

        self.movie.close()
        self.audio.close()
