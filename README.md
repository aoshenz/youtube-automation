# YouTube Automation

## Intro
This script automates YouTube/TikTok/Instagram Reels videos by using Google's text-to-speech and overlaying images on a video background. See an example video output [here](https://github.com/aoshenz/youtube-automation/blob/main/files_example/example_video/example_video.mp4).

Note: in it's current state, there are still a bunch of manual steps as you'll see below.
## How to use

### Set up
1. Rename `\files_example` to `\files`.
2. Add your background clips in `\files\bg_clips`. The script will randomly choose background clips from this folder.
3. Run `pipenv install`.
4. Set up a Google cloud text-to-speech account [here](https://cloud.google.com/text-to-speech). Save your credentials in `secret/credentials.json`.
### Creating videos

See `\files\example_video` for an example of an example video folder structure.

1. For each video you need to:
    - Create a folder in `\files`. For example `\files\minecraft_speedrun`.
    - Create a `img` folder within this. For example `\files\minecraft_speedrun\img`. Your image clips (or screenshots) for the video goes here. Make sure they are in the same alphabetical order as you would like them to appear in your video.
    - Make a copy of the `\files\info.py` and paste it into your folder. For example `files\minecraft_speedrun\info.py`. Fill in text that will be spoken aloud by the text to speech bot. Note here that each new 'paragraph' of text is how this script determines when to show the next image.
2. Repeat step 1 for each new video.
3. Open `config.py` and add each new video folder name to `TO_PROCESS` list. This allows you to queue the creation of multiple videos on the same code run.
4. Run `pipenv run python main.py`.

## Areas of improvement
- [ ] Connect to Reddit's API to extract text.
- [ ] Connect to video platform's (for example, YouTube) API to automate the upload.
- [ ] Automate grabbing images/screenshot.