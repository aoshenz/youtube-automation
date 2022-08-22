from gtts import gTTS
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def tts(text: list, output_folder: str):
    language = "en"
    domain = "com"
    output_folder = f"files/{output_folder}"

    logging.info(f"Creating {len(text)} audio clips.")

    for i in range(len(text)):
        audio = gTTS(text=text[i], tld=domain, lang=language, slow=False)

        output_file = f"{output_folder}/audio_{i}.mp3"
        audio.save(output_file)

    logging.info(f"Audio clips saved in {output_folder}")
