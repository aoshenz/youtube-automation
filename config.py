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

If you’re the smartest person in the room, you’re in the wrong room!
I’ll remember this when I lie alone in bed tonight

I’m living in China right now and everyone keeps calling me intelligent as I’m bald and left handed.
Apparently bald = intelligent now

The heat that smart people's brains give off burns off the hair
Damn, no wonder I've got a full head of hair at 52.
The self-burn humblebrag. Nicely executed!

Cornering people in arguments with bullying tactics and acting like it means they "won".
The people that say "Ohhh sweety" in an arguement...

Or "do your research"
"I'm not going to spoon feed it to you"
(when someone makes a pretty spectacular claim and you ask them to back it up with a source)

I hate this line of thought so much. You see it constantly on reddit with people like this. I once asked a dude in 3 separate comments to please link their source after I linked 5 sources refuting their claim. Each time I was told my sources were bad and they never provided one themselves

Silence. I’ve been told so many times that I’m thoughtful and a deep thinker but really I can’t figure out what to say lol
My girlfriend thinks my silence is me thinking hard or letting her sort her emotions out but it’s really me trying to think of anything to say but I’m a dumbass

Scoring an A when I was 14.
Scoring an E when I was 24, and at a rave.

Having money
I know someone who is fairly wealthy. He has worked with several billionaires and other wealthy people. He told me that luck is a much more important factor than people realize. Of course some people work hard but most are just exceptionally lucky. Also, 9/10 times they are assholes.

solving a rubiks cube
True, I learnt how to do it quite fast once I looked on Google. It’s just consistent practice until you memorise it

Strong opinions, held with confidence.
80% of podcasts just screamed out in unison

A cromulent vocabulary.
This embiggens me.
I chortled gleefully at this riposte.

Having an opinion on literally everything. Especially having the need to share the opinions with everyone they encounter.
One of my biggest pet peeves. And on the flip side, immediate respect goes out to anyone who is able to say they don't know enough about the topic to have a solid opinion.
"""

TEXT = TEXT.split("\n\n")
TEXT = [i.replace('\n', ' ') for i in TEXT]

TEXTS = TITLE + TEXT
