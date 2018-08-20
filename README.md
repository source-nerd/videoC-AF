## VideoC-AF : Python based Video Converter

VideoC-Af is a simple Python based video converter based on top of [FFMpeg Multimedia Framework](http://ffmpeg.org/ "FFMPEF.org") for converting video files from one format to another.

VideoC-AF can take videos of any file format and can convert it to multiple / different formats.

Currently is under early development so only MP4, WEBM & MP3 are supported.

### Features:
1. Can take video of any format and convert it in the above mentioned formats.
2. Loss less mode supported - (In Dev)
3. Supported frame resolutions: same, 240p, 360p, 480p, 720p, 1080p, 1444p, 2160p, 4320p - (May add support for more advanced resolutions in future)
4. You can specify the audio and video bitrates explicitly
5. Custom output file directory 

### Working:
You can either provide a video file path or can provide a folder.
The script walks through the complete folder directory provided and takes all the video files that can be converted.


### Installation:
1. Install Python 3.x
2. Clone this repo
3. Initialize the project with virtual environment
4. Install the project dependencies by running ```pip install -r requirements.txt```


### Examples:
1. To convert `Any Video File to MP3`
    ```commandline
    python converter.py -i INPUT_DIR_HERE -p * -f mp3 
    ```
    Here, all the video files in that above provided folder will be converted to mp3 format and the output will be stored in the same folder as of the input.
    
    If you want to provide a custom output directory then add an extra argument `-o` which stands for output:
    ```commandline
    python converter.py -i INPUT_DIR_HERE -p * -f mp3 -o OUTPUT_DIR_HERE
    ```

2. To Convert any video file to .MP4 or .WEBM:
    ```commandline
    python converter.py -i INPUT_DIR_HERE -p * -f mp4 -s 720p -b normal -o OUTPUT_DIR_HERE
    ```
    The above command reads any video input file and converts it to MP4 format of 720p while preserving the authenticity of audio and video. The Video conversion preset is small and other tweaking parameters are introduced to have better and stable video. But again you are free to optimize and test your own version.
    -o parameter which is for custom output directory is optional. Not passing -o parameter will lead to saving of converted videos in the same input directory of the original video.


### Usage:
```git
usage: videoc-af [-h] [-i [input_directory]] [-p FILE_PATTERN]
                    [-f {mp4,webm,mp3}]
                    [-s {same,4320p,2160p,1440p,1080p,720p,480p,360p,240p}]
                    [-b BITRATE] [-o OUTPUT] [-v]

optional arguments:

  -h, --help            show this help message and exit
  -i [input_directory], --input_directory [input_directory]
                        input directory of audio/video files to be converted
  -p FILE_PATTERN, --pattern FILE_PATTERN
                        input file filter, regex-style (e.g: ".mov|.avi")
  -f {mp4,webm,mp3}, --format {mp4,webm,mp3}
                        video output format
  -s {same,4320p,2160p,1440p,1080p,720p,480p,360p,240p}, --size {same,4320p,2160p,1440p,1080p,720p,480p,360p,240p}
                        video frame size
  -b BITRATE, --bitrate BITRATE
                        video bitrate adjustment
  -o OUTPUT, --output OUTPUT
                        Output Folder Path
  -v, --version         show program's version number and exit
```

### FeedBack:
Again, since I developed it for my own internal use but found out that any people need similar stuff for some or the other day to day activities for their media, I thought of open sourcing it.

Its not very optimized, so any find of bug fixes, feature requests, pull requests, feedback, etc., are welcome...


### License:
VideoC-AF is released under the GPL v3 and the bundled ffmpeg is LGPL/GPL v2.1.
If you’re in a country which recognizes software patents, it’s up to you to ensure you’re complying with the patent laws. Please read the FFMpeg Legal FAQ for more information.