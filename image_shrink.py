import os.path
import os
import glob
from PIL import Image
import sys

DIR  = str(sys.argv[1])

SRC_DIR = f'{DIR}'
TARG_DIR = f'{DIR}/resized_images'

# File needs to contain a '-' and be a jpg
GLOB_PARMS = "*-*.jpg"

def save_resized_image ():
    for file in glob.glob(os.path.join(SRC_DIR, GLOB_PARMS)):
        # check that the file hasn't already been copied into the retention directory, and that the file is larger than 2 MB, then proceed to copy and resize in place
        file_name = os.path.split(file)[1]
        print(file_name)
        print(glob.glob(os.path.join(TARG_DIR, GLOB_PARMS))) # TODO: compare with arrays subcontents
        if file not in glob.glob(os.path.join(TARG_DIR, GLOB_PARMS)) and os.stat(file).st_size > 2097152:
            img=Image.open(file)
            file_path_copy = os.path.join(TARG_DIR, file_name)
            # create a copy of the original image into the subdirectory for retention
            img.save(file_path_copy)
            
            file_path_original = os.path.join(SRC_DIR, file_name)
            print(file_path_original, os.stat(file).st_size)
            img.save(file_path_original, quality=25)
        else:
            print("file has already been copied, or is smaller than 2 MB")
            # .format(
            #    file,os.path.join(os.path.split(TARG_DIR)[-2:]))

save_resized_image()



