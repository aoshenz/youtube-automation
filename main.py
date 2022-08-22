import logging
import utils as utils
from utils import Movie
import config

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":

    movie = Movie(config.FOLDER, config.BACKGROUND_VIDEO)

    movie.tts(config.TEXTS)
    movie.append_audio()

    print(movie.audio_duration)
    print("\n")
    print(movie.audio_total_duration)

    movie.create_movie()
    movie.output_movie()
