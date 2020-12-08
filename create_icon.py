import os, sys
from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".png"
    try:
        with Image.open(infile) as im:
            im=im.resize((100,100))
            im.save(outfile)
    except OSError:
        print("cannot convert", infile)