import os
import sys
import argparse

from data.aggregator import GetFiles
from model.converterFormats import ConverterFormatsSupported
from model.presets import Presets
from model.defaultFormats import DefaultFormats

VERSION = 'v1.0'


def run_function(input_dir, file_pattern, format_to_be_converted_to, size='same', bitrate='normal'):
    files = GetFiles(input_dir, file_pattern).crawl_dir()
    for file in files:
        generate_command(file, format_to_be_converted_to, size, bitrate)


def get_system_platform():
    ffmpeg_path = ""
    if sys.platform == "darwin":
        ffmpeg_path = os.path.join(os.path.abspath('ffmpeg\\osx'), 'ffmpeg')
    elif sys.platform == "win32":
        ffmpeg_path = os.path.join(os.path.abspath('ffmpeg\\windows'), 'ffmpeg.exe')
    elif sys.platform == "linux" or sys.platform == "linux2":
        ffmpeg_path = os.path.join(os.path.abspath('ffmpeg\\linux'), 'ffmpeg')
    return ffmpeg_path


def generate_command(item, av_format, frame_size='same', bitrate='normal'):
    av_formats = ConverterFormatsSupported.video_formats
    default_video_presets = Presets.default_video_presets

    command = get_system_platform() + " -threads 4  -i " + "\"" + item + "\"" + " "

    if av_format.lower() == 'mp3':
        command += av_formats[av_format]['more_options']
    else:
        command += "-vcodec " + av_formats[av_format]['vcodec'] + " " if 'vcodec' in av_formats[av_format] else ''
        command += "-s " + default_video_presets[frame_size]['size'] + " " if frame_size != 'same' else ''
        # if frame_size != "same":Convert
        #     command += "-s " + default_video_presets[frame_size]['size'] + " "
        if bitrate in ("high", "normal", "low"):
            command += "-b:v " + default_video_presets[frame_size]['v_bitrate'][bitrate] + " " if frame_size != 'same' else ''
        else:
            command += "-b:v " + bitrate + " "

        command += "-acodec " + av_formats[av_format]['acodec'] + " " if 'acodec' in av_formats[av_format] else ''
        # command += "-ab " + default_video_presets[frame_size]['ab'] + " "
        command += "-ar 48000 -ac 2 "
        command += av_formats[av_format]['more_options'] + " "

    head, tail = os.path.split(item)
    op_string = os.path.join(head, os.path.splitext(os.path.basename(item))[0] + '.' + av_format)
    command += "\"" + op_string + "\""
    print(command)
    os.system(command)


argparser = argparse.ArgumentParser(description='Convert videos to common formats. Output will be stored in the same directory as the input. Read more here:  ', prog='thetechfreak')
argparser.add_argument('-i', '--input_directory', metavar='input_directory', nargs='?', default='.', help='input directory of audio/video files to be converted')
argparser.add_argument('-p', '--pattern', dest='file_pattern', default='|'.join(DefaultFormats.default_video_formats), help='input file filter, regex-style (e.g: ".mov|.avi")')
argparser.add_argument('-f', '--format', dest='output_format', choices=['mp4', 'webm', 'mp3'], default='mp4', help='video output format')
argparser.add_argument('-s', '--size', dest='size', choices=Presets.default_video_presets.keys(), default='same', help='video frame size')
argparser.add_argument('-b', '--bitrate', dest='bitrate', default='normal', help='video bitrate adjustment')
argparser.add_argument('-r', '--recursive', dest='recursive', action='store_true', default=False, help='recursively traverse the subtree')
argparser.add_argument('-v', '--version', action='version', version='%(prog)s ' + VERSION)
args = argparser.parse_args()

run_function(args.input_directory, args.file_pattern, args.output_format, args.size, args.bitrate)
