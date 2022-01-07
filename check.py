from PIL import Image
import sys
import os

input_path=sys.argv[1]
for infile in os.listdir(sys.argv[1]):
    try:
        with Image.open(input_path+'/'+infile) as im:
            print(infile, im.format, f"{im.size}x{im.mode}")
    except OSError:
        pass
