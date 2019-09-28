import numpy as np
import cv2
from skimage.io import imsave
import imutils

class Detection:
    def _init__():
        pass

    def detect(self,img):
        (h,b,c)=img.shape
        # Make a copy of the image
        image_copy = np.copy(img)

        # Change color to RGB (from BGR)
        image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

        ##TO DO: Define the color selection boundaries in RGB values
        # play around with these values until you isolate the blue background
        lower_blue = np.array([0,0,200]) 
        upper_blue = np.array([250,250,255])

        # Define the masked area
        mask = cv2.inRange(image_copy, lower_blue, upper_blue)

        masked_image = np.copy(image_copy)

        masked_image[mask != 0] = [0, 0, 0]
        imsave("img1.png", masked_image)

        return imutils.resize(masked_image, height=650)

    def background_add(self,img,img1):

        (h,b,c)=img.shape
        # Make a copy of the image
        image_copy = np.copy(img)

        # Change color to RGB (from BGR)
        image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

        ##TO DO: Define the color selection boundaries in RGB values
        # play around with these values until you isolate the blue background
        lower_blue = np.array([0,0,200]) 
        upper_blue = np.array([250,250,255])

        # Define the masked area
        mask = cv2.inRange(image_copy, lower_blue, upper_blue)

        masked_image = np.copy(image_copy)
        # Load in a background image, and convert it to RGB 
        
        background_image = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

        # Crop it to the right size (514x816)
        crop_background = background_image[0:514, 0:816]

        lower_blue = np.array([0,0,200])
        upper_blue = np.array([250,250,255])
        mask = cv2.inRange(image_copy, lower_blue, upper_blue)

        # Mask the cropped background so that the pizza area is blocked
        crop_background[mask == 0] = [0, 0, 0]

        # Add the two images together to create a complete image!
        complete_image = masked_image + crop_background

        imsave("img2.png", complete_image)

        #return none


if __name__ == '__main__':
    ob=Detection()
    img = cv2.imread('images/pizza_bluescreen.jpg')
    background_image = cv2.imread('images/space_background.jpg')
    ob.detect(img)
    ob.background_add(img,background_image)

