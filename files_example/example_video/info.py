# Content
URL = "https://www.reddit.com/r/todayilearned/comments/ujoonz/til_in_2011_a_29yearold_australian_bartender/"

TITLE = [
    "TIL in 2011, a 29-year-old Australian bartender found an ATM glitch that allowed him to withdraw way beyond his balance. In a bender that lasted four-and-half months, he managed to spend around $1.6 million of the bank’s money."
]

# Seperate each new "screenshot" with 2 line breaks i.e. \n\n
TEXT = """
"Being able to make your account balance move up into the millions by the stroke of a key was a very addictive thing; I felt like a caveman discovering fire"
basically all you need to know.

Turned himself in to the bank before they had even caught on, they called the cops who then took so long to do anything the anxiety drove him to do a media tour confessing to everything that finally got him arrested. The judge and prosecutor had no idea what he'd actually done and after pleading guilty he ended up getting one year in jail with eighteen months community service.

Reminds me of a story: in the mid-80s, I missed a train back to London (to make flight back to USA) and had to spend the night in the Gare Saint-Lazare in Paris. I did happen to have exactly enough money in pocket to fly to London next morning, but not enough for the train fare to the airport. Only reason I ever made it back is… there was a public phone in the train station that gave you back twice as much money as you put in it, for any call you made. Otherwise, I'd probably still be there.

Reminds me of the guy on wsb who found and unlimited money glitch and then lost it all on apple puts.
"""

TEXT = TEXT.split("\n\n")
TEXT = [i.replace("\n", " ") for i in TEXT]

TEXTS = TITLE + TEXT
