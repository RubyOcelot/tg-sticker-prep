from PIL import Image
import sys
import os


input_path=sys.argv[1]+"/input/"
output_path=sys.argv[1]+"/output/"
infiles=os.listdir(input_path)
if not os.path.exists(output_path):
    os.makedirs(output_path)
for infile in infiles:
    try:
        with Image.open(input_path+infile) as im:
            print(infile, im.format, f"{im.size}x{im.mode}")
            outfile="sticker_"+infile
            if im.format=='JPEG':
                im=im.convert('RGB')
                f, e = os.path.splitext(outfile)
                outfile=f+'.png'
            elif im.format!='PNG':
                continue

            (width,height)=im.size
            if width>height:
                new_size=(512,int(512*height/width))
            else:
                new_size=(int(512*width/height),512)
            im=im.resize(new_size)
            im.save(output_path+outfile)
    except OSError:
        pass
