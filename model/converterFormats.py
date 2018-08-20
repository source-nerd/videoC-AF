class ConverterFormatsSupported:
    video_formats = {
        'mp4': {'vcodec': 'libx264', 'acodec': 'aac', 'more_options': '-async 50 -preset slow -crf 17 '},
        'webm': {'vcodec': 'libvpx', 'acodec': 'libvorbis', 'more_options': ''},
        'mp3': {'more_options': '-b:a 320K -vn '}  # Constant Bit Rate (CBR) is 320kb/s
    }
