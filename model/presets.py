class Presets:
    default_video_presets = {
        'same': {'size': 'same'},
        '4320p': {'size': '7680x4320', 'v_bitrate': {'high': '150000k', 'normal': '90000k', 'low': '78000k'}},
        '2160p': {'size': '3840x2160', 'v_bitrate': {'high': '50000k', 'normal': '35000k', 'low': '23000k'}},
        '1440p': {'size': '2560x1440', 'v_bitrate': {'high': '24000k', 'normal': '16000k', 'low': '10400k'}},
        '1080p': {'size': '1920x1080', 'v_bitrate': {'high': '12000k', 'normal': '8000k', 'low': '23090k'}},
        '720p': {'size': '1280x720', 'v_bitrate': {'high': '7500k', 'normal': '5000k', 'low': '1378k'}},
        '480p': {'size': '854x480', 'v_bitrate': {'high': '4000k', 'normal': '2500k', 'low': '1155k'}},
        '360p': {'size': '640x360', 'v_bitrate': {'high': '1500k', 'normal': '1000', 'low': '525k'}},
        '240p': {'size': '427x240', 'v_bitrate': {'high': '650k', 'normal': '450k', 'low': '242k'}}
    }
