import logging

from gtts import gTTS
from moviepy.editor import (CompositeVideoClip, TextClip, VideoFileClip,
                            concatenate_videoclips)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)




# text to speech
text = 'The quick brown fox jumped over the lazy dog.'

def tts(text, output):
    language = 'en'
    domain = 'com'
    output_path = f"files/{output}.mp3"

    logging.info(f"Creating audio.")

    audio = gTTS(text=text, tld=domain, lang=language, slow=False)
    audio.save(output_path)

    logging.info(f"Audio saved in {output_path}")

# tts(text, 'test')


# movie py

def movie():
    logging.info(f"Creating video.")

    clip1 = VideoFileClip("files/Grass.mp4").subclip(0, 2)
    clip2 = VideoFileClip("files/Grass.mp4").subclip(10, 13)
    combine = concatenate_videoclips([clip1, clip2])

    # add text
    txt = TextClip('Hello everyone!', font='Arial', fontsize=120, color='white', bg_color='gray35')
    txt = txt.set_position(('center', 'center'), relative=True)
    txt = txt.set_start((0,0)) # (min, s)
    txt = txt.set_duration(4)
    txt = txt.crossfadein(0.5)
    txt = txt.crossfadeout(0.5)

    combine = CompositeVideoClip([combine, txt])

    combine.write_videofile("files/video.mp4")

    logging.info(f"Saved video.")

movie()