#Imports
from PIL import Image


class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''       

        # Write your code here
        self.dimension = output_size

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
       
        # Write your code here
        if isinstance(self.dimension, int):
            self.w, self.h = image.size
            if self.w<self.h:
                print("hello")
                self.dimension2 = self.dimension*self.h//self.w
                im1 = image.resize((self.dimension, self.dimension2))
                #im1.show()
            else: 
                print("helo")
                self.dimension2 = self.dimension*self.w//self.h
                im1 = image.resize((self.dimension2, self.dimension))
                #im1.show()
        else:
            im1 = image.resize(self.dimension)
            #im1.show()

        return im1

# s = Image.open('C:/CS29006_SW_Lab_Spr2022-master/Python_DS_Assignment/data/imgs/0.jpg')
# r = RescaleImage((800,800))
# if type((200,200))==tuple:
#     print("hi")
# r(s)
        
