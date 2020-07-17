from PIL import Image
import numpy as np

#im_frame = Image.open(r'test-images\0\test1.png')
im_frame = Image.open(r'test-images\1\test3.png')
#im_frame = Image.open(r'training-images\0\im9963.png')
np_frame = np.array(im_frame.getdata())
print(np_frame)
