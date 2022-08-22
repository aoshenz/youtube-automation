import logging
import pathlib
import random

from moviepy.editor import (
    CompositeVideoClip,
    TextClip,
    VideoFileClip,
    concatenate_videoclips,
    ImageClip,
    ImageSequenceClip,
    AudioFileClip
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def practice():
    logging.info(f"Creating video.")

    clip1 = VideoFileClip("files/Grass.mp4").subclip(0, 2)
    clip2 = VideoFileClip("files/Grass.mp4").subclip(10, 13)
    combine = concatenate_videoclips([clip1, clip2])

    # add text
    txt = TextClip(
        "Hello everyone!", font="Arial", fontsize=120, color="white", bg_color="gray35"
    )
    txt = txt.set_position(("center", "center"), relative=True)
    txt = txt.set_start((0, 0))  # (min, s)
    txt = txt.set_duration(4)
    txt = txt.crossfadein(0.5)
    txt = txt.crossfadeout(0.5)

    combine = CompositeVideoClip([combine, txt])

    combine.write_videofile("files/video.mp4")

    logging.info(f"Saved video.")




logging.info(f"Creating video.")



# movie = ImageClip('files/test/screen_0.png')
# movie = movie.set_duration(10)

# audio = AudioFileClip('files/test/audio_0.mp3')
# audio = audio.set_start(0)

# movie.audio = audio
# movie.write_videofile('files/test/movie.mp4', fps=24)

# logging.info(f"Saved video.")

files = [f"files/test/img/screen_{i}.png" for i in range(9)]


background = VideoFileClip("files/skyscraper.mp4").subclip(0, 3)

# frames = []
# for f in files:
#     img = ImageClip(f).set_duration(1).set_position((0.4, 0.6), relative=True)
#     frames.append(img)

text_clips = []
for f in range(len(files)):

    total_duration = len(files)
    clip_duration = total_duration - f
    x_pos = random.uniform(0.1,0.7)
    y_pos = random.uniform(0.1,0.7)

    img = (ImageClip(files[f])
            .set_start(f)
            .set_duration(clip_duration)
            .resize(0.5)
            .set_position((x_pos, y_pos), 'relative'))

    text_clips.append(img)

background = CompositeVideoClip([background] + text_clips)


# clip = concatenate_videoclips(frames, method="chain")

# movie = CompositeVideoClip([background, clip])

background.write_videofile('files/test/movie.mp4')
background.close()