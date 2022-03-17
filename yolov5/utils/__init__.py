# import sys
# from pathlib import Path
#
# import torch
# from PIL import ImageFont
#
# FILE = Path(__file__).resolve()
# ROOT = FILE.parents[1]  # yolov5/ dir
# if str(ROOT) not in sys.path:
#     sys.path.append(str(ROOT))  # add ROOT to PATH
#
# # Check YOLOv5 Annotator font
# font = 'Arial.ttf'
# try:
#     ImageFont.truetype(font)
# except Exception as e:  # download if missing
#     url = "https://ultralytics.com/assets/" + font
#     print(f'Downloading {url} to {ROOT / font}...')
#     torch.hub.download_url_to_file(url, str(ROOT / font))
# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
"""
utils/initialization
"""


def notebook_init(verbose=True):
    # Check system software and hardware
    print('Checking setup...')

    import os
    import shutil

    from utils.general import check_requirements, emojis, is_colab
    from utils.torch_utils import select_device  # imports

    check_requirements(('psutil', 'IPython'))
    import psutil
    from IPython import display  # to display images and clear console output

    if is_colab():
        shutil.rmtree('/content/sample_data', ignore_errors=True)  # remove colab /sample_data directory

    if verbose:
        # System info
        # gb = 1 / 1000 ** 3  # bytes to GB
        gib = 1 / 1024 ** 3  # bytes to GiB
        ram = psutil.virtual_memory().total
        total, used, free = shutil.disk_usage("/")
        display.clear_output()
        s = f'({os.cpu_count()} CPUs, {ram * gib:.1f} GB RAM, {(total - free) * gib:.1f}/{total * gib:.1f} GB disk)'
    else:
        s = ''

    select_device(newline=False)
    print(emojis(f'Setup complete ✅ {s}'))
    return display
