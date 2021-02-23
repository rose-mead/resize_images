import os.path
import os
import glob
from PIL import Image
import sys

DIR  = str(sys.argv[1])

SRC_DIR = f'{DIR}'
TARG_DIR = f'{DIR}/original_images'

# File needs to contain a '-' and be a jpg
GLOB_PARMS = "*-*.jpg"

src_dir_files = glob.glob(os.path.join(SRC_DIR, GLOB_PARMS))
target_dir_files = glob.glob(os.path.join(TARG_DIR, GLOB_PARMS))

def save_resized_image ():
    for file in src_dir_files:
        # check that the file hasn't already been copied into the retention directory, and that the file is larger than 2 MB, then proceed to copy and resize in place
        file_name = os.path.split(file)[1]
        target_file_name = f'{DIR}/original_images/{file_name}'

        # if file not in target_dir_files:
        if target_file_name not in target_dir_files and os.stat(file).st_size > 2097152:

        # TODO: compare with arrays subcontents
            img=Image.open(file)

            # create a copy of the original image into the subdirectory for retention
            img.save(target_file_name, quality=98)
            print(file_name + " saved in original_images directory")

            # save resized image in the 'emma' folder, overwriting the original
        #    print(file_path_original, os.stat(file).st_size)
            file_path_original = os.path.join(SRC_DIR, file_name)
            img.save(file_path_original, quality=25)
        # else:
            # print(file_name + " file has already been copied, or is smaller than 2 MB")
            # .format(
            #    file,os.path.join(os.path.split(TARG_DIR)[-2:]))

save_resized_image()



