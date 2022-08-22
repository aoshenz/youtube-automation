# Set up

FOLDER = "What companies can go fuck themselves"

BACKGROUND_VIDEO = "background.mov"

# Content
# url = "https://www.reddit.com/r/AskReddit/comments/w68jfd/what_video_game_do_you_consider_a_masterpiece/"

TITLE = ["What companies can go fuck themselves?"]

# Seperate each new "screenshot" with 2 spaces i.e. \n\n
TEXT = """
Ticketmaster
If the words “Convenience Charge” don’t fill you with rage, you’re part of the problem.

FIFA, unbelievably corrupt, I don't even know where to start.
I think FIFA, in this thread, is the definition of monopoly. I love football and so much about the energy of World Cup. But I 100% agree

Black Rock and any other companies currently trying to buy as many single-family homes as possible so that they manipulate housing prices and raise rents while being shit landlords.

Nestlé, horrible practices
The worst thing is, if you want to boycott them, you need a fucking flowchart because they own so many food companies.

Canadian chiming in, Bell/Bell Media. Liars and thieves.
Once got an email Tuesday morning about how sad and difficult it is to lose coworkers (hundreds) due to layoffs.
Got an email Wednesday morning touting how Q4 profits were through the roof as they congratulated executive

Spectrum communications.
Spectrum thinks I am just some dumb hick. They said that to me at a dinner.

fleshlight would make the most sense I suppose
These are the type of comments I joined Reddit for tbh.

John Deere. People tend to think of Apple as the biggest opponent to the Right To Repair movement. Nah. Apple's got nothing on John Deere.

United healthcare, LabCorps, Quest diagnostics,
Blue cross of anything
Can you tell I am in the medical billing environment?

Nestle. because of what they do in africa, and also the fact that they manipulate parents that can't or dont want to breastfeed, into using their terrible alternative. pretty sure half of it is sugar. oh, and the CEO said that water isn't a human right.
r/FuckNestle

Any MLM company
Watching people you know turn into walking advertisements is sickening.
Do you feel sick? I’m sure I have some oils to help you.

Deutsche Bank. Shamelessly invest in pretty much every evil project or person they possibly can.
arent they notorious for money laundering for drug cartels and terrorist organizations
"""

TEXT = TEXT.split("\n\n")
TEXT = [i.replace('\n', ' ') for i in TEXT]

TEXTS = TITLE + TEXT