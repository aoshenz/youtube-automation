# YouTube Automation

## Intro
This script allows you to automate YouTube/TikTok/Instagram Reels videos (to some extent).
## How to use

See `\files\example_video` for an example of an example video folder structure.

**Set up**
1. Rename `\files_example` to `\files`.
2. Add your background clips in `\files\bg_clips`. The script will randomly choose background clips from this folder.
3. Run `pipenv install`.

**Creating videos**

1. For each video you need to:
    - Create a folder in `\files`. For example `\files\minecraft_speedrun`.
    - Create a `img` folder within this. For example `\files\minecraft_speedrun\img`. Your image clips (or screenshots) for the video goes here. Make sure they are in the same alphabetical order as you would like them to appear in your video.
    - Make a copy of the `\files\info.py` and paste it into `files\minecraft_speedrun`. Here you'll need to fill in text that will be spoken aloud by the text to speech bot. Note here that each new 'chunk' of text is how this script determines when to show the next image.
2. Repeat step 1 for each new video.
3. Open `config.py` and add each new video folder to `TO_PROCESS` list. This allows the code to create multiple videos on the same code run.
4. Run `main.py`.

## Areas of improvement
- [ ] Add a connection to Reddit's API.
- [ ] Connect to video platform's (for example, YouTube) API to automate the upload.