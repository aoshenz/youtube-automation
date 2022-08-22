import logging
import utils as utils
from utils import Movie


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# text to speech
# url = "https://www.reddit.com/r/AskReddit/comments/w68jfd/what_video_game_do_you_consider_a_masterpiece/"

title = ["What movie blew your mind when you finished it?"]

text = [
    "I remember walking out of the cinema thinking 'That was a waste of an evening' after watching The Others, only to spend the next week constantly thinking about it and going back the following weekend to watch it again. It was a very very slow blowing of my mind.",
    "The matrix. Saw in in the theatre and walked out thinking, am I a battery?",
    "The Prestige",
    "Memento",
    "Interstellar and Arrival.",
    "The Sixth Sense",
    "Shutter Island",
    "The Truman show",
    "I watched Blade Runner 2049 recently and haven't been able to stop thinking about it.",
    "The Mist. Watched it only once in 2012 and every few months since, I'll suddenly remember that ending and feel strong emotions",
    "The usual suspects.",
    "Se7en",
    "12 Monkeys. There were twists, yes, but it was also put together in a way I hadn’t seen experienced before.",
    "Fight Club",
    "Dark City",
    "Eternal sunshine of the spotless mind",
    "The Game"
]

texts = title + text


def main():

    movie = Movie("What movie blew your mind when you finished it")

    movie.tts(texts)
    movie.append_audio()

    print(movie.audio_duration)
    print(movie.audio_total_duration)

    movie.create_movie()
    movie.output_movie()


if __name__ == "__main__":

    main()
