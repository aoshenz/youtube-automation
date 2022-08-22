import logging
import functions.texttospeech as tts
import movie as movie


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


working_folder = 'test'


# text to speech
url = 'https://www.reddit.com/r/AskReddit/comments/w68jfd/what_video_game_do_you_consider_a_masterpiece/'

title = ['What video game do you consider a masterpiece?']

text = [
    'Portal 2',
    'Age of empires 2',
    'Original Halo. Felt like you were in a movie',
    'Man i miss Valve... Their games were designed in a way many developers could only dream of, they were revolutionary in almost everything they laid their hands on.',
    'Roller Coaster Tycoon 2',
    'Zelda Ocarina of time',
    'Original bioshock',
    'Half-Life (1998)'
]

texts = title + text

tts.tts(texts, working_folder)



# movie.movie()
