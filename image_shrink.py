import os.path
import glob
from PIL import Image

SRC_DIR = '/Users/rosemead/Developer/Personal_Projects/Em_Trent_images/images'
TARG_DIR = '/Users/rosemead/Developer/Personal_Projects/Em_Trent_images/resized_images'

# File needs to contain a '-' and be a jpg
GLOB_PARMS = "[0-9]*-[0-9]*.jpg"

def create_folder ():
    if not os.path.exists(TARG_DIR):
        os.makedirs(TARG_DIR)

def save_resized_image ():
    for file in glob.glob(os.path.join(SRC_DIR, GLOB_PARMS)):
        if file not in glob.glob(os.path.join(TARG_DIR, GLOB_PARMS)):
            print(file)
            img = Image.open(file)
           
            file_name = os.path.split(file)[1]

            file_path = os.path.join( TARG_DIR, file_name) 
            img.save(file_path, quality=50)

        else:
            print("{} exists in {}".format(
                file,os.path.join(os.path.split(TARG_DIR)[-2:])))


create_folder()
save_resized_image()



