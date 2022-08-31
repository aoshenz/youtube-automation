# Set up
FOLDER = "intelligence"

BACKGROUND_VIDEO = "background.mov"

# Content
URL = "https://www.reddit.com/r/AskReddit/comments/wlr2od/people_of_reddit_who_survive_on_less_than_8_hours/"

TITLE = ["What is incorrectly perceived as a sign of intelligence?"]

# Seperate each new "screenshot" with 2 spaces i.e. \n\n
TEXT = """
Being in charge
Always maintain a healthy skepticism for anyone claiming to be authority, at least till they prove themselves capable.

if someone’s in an authoritative position, it should be others that praise them and say how good they are, not themselves.

“I’m the best commenter that’s ever been. People always tell me, they say “VPman, that’s what they call me, they say VP, you always leave the best comments. They say that. Ask anyone, they’ll tell you. That’s why I’m happy to announce that I’m running for comment president again 2024. Let’s make comments great again, again.”

Arrogance portrayed as confidence
A truly intelligent person knows that there's things they don't know, and keeps trying to learn.
An idiot refuses to acknowledge that there's anything they don't know, and fears doing anything that might prove it.
"""

TEXT = TEXT.split("\n\n")
TEXT = [i.replace("\n", " ") for i in TEXT]

TEXTS = TITLE + TEXT
