import logging
import utils as utils
from utils import Movie
import config
import importlib

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":

    logging.info(f"Folders: {', '.join(config.TO_PROCESS)}")
    logging.info(f"Number of folders: {len(config.TO_PROCESS)}")

    for folder in config.TO_PROCESS:
        print("\n\n")
        logging.info(f"Working on {folder}.")

        info = importlib.import_module(f"files.{folder}.info")

        movie = Movie(folder, info.TEXTS)

        movie.checks()
        movie.tts()
        movie.append_audio()

        print(f"{movie.audio_duration}")
        print(f"{movie.audio_total_duration}")
        print(f"{round(movie.audio_total_duration / 60, 2)} mins")

        movie.create_bg_video()

        movie.create_movie()
        movie.output_movie()

    logging.info("All done!")