# import the library we just installed
from simple_image_download import simple_image_download as simp

# create a new class instance
response = simp.simple_image_download

# the images you want to download from google
keywords = ["airplans","dogs","cats"]

# for each key word  download  images
for kw in keywords:
	response().download(kw, 200)