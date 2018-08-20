## VideoC-AF : Python based Video Converter

VideoC-Af is a simple Python based video converter based on top of [FFMpeg Multimedia Framework](http://ffmpeg.org/ "FFMPEF.org") for converting video files from one format to another.

VideoC-AF can take videos of any file format and can convert it to multiple / different formats.

Currently is under early development so only MP4 and WEBM are supported.

### Features:
1. Can take video of any format and convert it in the above mentioned formats.
2. Loss less mode supported - (In Dev)
3. Supported frame resolutions: same, 240p, 360p, 480p, 720p, 1080p, 1444p - (May add support for more advanced resolutions in future)
4. You can specify the audio and video bitrates explicitly
5. Custom output file directory

###Working:
You can either provide a video file path or can provide a folder.
The script walks through the complete folder directory provided and takes all the video files that can be converted.

###Examples:

###Installation:
1. Install Python 3.x
2. Clone this repo
3. Run ```pip install -r requirements.txt```

###Usage:


###FeedBack:
All bugs, feature requests, pull requests, feedback, etc., are welcome...

###License:
VideoC-AF is released under the GPL v3 and the bundled ffmpeg is LGPL/GPL v2.1.
If you’re in a country which recognizes software patents, it’s up to you to ensure you’re complying with the patent laws. Please read the FFMpeg Legal FAQ for more information.