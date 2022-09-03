import logging
import pathlib
import random
from gtts import gTTS
import shutil

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
    def __init__(self, folder: str, text: list):
        self.folder = folder
        self.text = text

    def checks(self):

        # Check number of text parts = number of screenshots
        img_path = pathlib.Path(f"files/{self.folder}/img").glob("**/*png")
        img_path = [str(p) for p in img_path]
        
        if len(img_path) == len(self.text):
            logging.info(f"Check passed: texts = images = {len(self.text)}")
        else:
            logging.error(f"ERROR: screenshots: {len(img_path)}, texts: {len(self.text)}")

    def tts(self):
        """
        Create text-to-speech audio files for each iteration in list.
        """

        self.num_audio = len(self.text)

        language = "en"
        domain = "com"

        pathlib.Path(f"files/{self.folder}/audio").mkdir(parents=True, exist_ok=True)
        output_folder = f"files/{self.folder}/audio"

        for i in range(self.num_audio):
            audio = gTTS(text=self.text[i], tld=domain, lang=language, slow=False)

            output_file = f"{output_folder}/audio_{i}.mp3"
            audio.save(output_file)

        logging.info(f"Audio clips saved in {output_folder}")

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
        self.audio_total_duration = int(sum(self.audio_duration.values()))

    def create_bg_video(self):
        """Create background video based on length of audio."""
        logging.info("Creating background video.")

        bg_clips = pathlib.Path(f"files/bg_clips/").glob("**/*mp4")
        bg_clips = [str(p) for p in bg_clips]

        logging.info(f"Number of background clips to choose from: {len(bg_clips)}")

        bg_clip_length = 0
        while bg_clip_length < self.audio_total_duration + 10:  # 10 second buffer
            random_int = random.randint(0, len(bg_clips) - 1)
            random_path = bg_clips[random_int]

            bg = VideoFileClip(random_path, audio=False)

            if bg_clip_length == 0:
                combined_bg = bg
                bg_clip_length += int(combined_bg.duration)
            else:
                combined_bg = concatenate_videoclips([combined_bg, bg])
                bg_clip_length += int(combined_bg.duration)

            logging.info(f"Current background clip length: {bg_clip_length}")

        self.bg_video = combined_bg.set_end(
            self.audio_total_duration + 10
        )  # 10 second buffer
        logging.info(f"Final background clip length: {self.bg_video.duration}")

    def create_movie(self):
        """Overlay text screenshots on background video."""

        logging.info("Overlaying text screenshots on background video.")

        # background = VideoFileClip(f"files/{self.folder}/{self.bg_video}", audio=False)

        img_path = pathlib.Path(f"files/{self.folder}/img").glob("**/*png")
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

        movie = CompositeVideoClip([self.bg_video] + text_clips)
        self.movie = movie.set_audio(self.audio)

    def output_movie(self):
        """Output movie."""

        logging.info(f"Creating movie.")

        self.movie.write_videofile(
            f"files/{self.folder}/{self.folder}.mp4",
            codec="libx264",
            audio_codec="aac",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
        )

        self.movie.close()
        self.audio.close()

        logging.info("Video saved.")

    def output_description(self):
        """Output a file that reduces manual work when uploading to YouTube."""

        pass
