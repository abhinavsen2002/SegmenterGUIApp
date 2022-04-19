####### REQUIRED IMPORTS FROM THE PREVIOUS ASSIGNMENT #######
from my_package.model import InstanceSegmentationModel
from my_package.data import Dataset
from my_package.analysis import plot_visualization
from PIL import Image

####### ADD THE ADDITIONAL IMPORTS FOR THIS ASSIGNMENT HERE #######
from tkinter import Tk, StringVar, Button, Entry, OptionMenu, filedialog, Label
from PIL import ImageTk
import os

class data:
    selected_image = None
        
# arguments, pil image you wish to display, column c in which you wish to display it
def DisplayImage(im, c):    
    for slave in root.grid_slaves(row = 1, column = 10*c):
        slave.grid_forget()
    image = ImageTk.PhotoImage(im)
    image_label = Label(root, image = image)
    image_label.image = image
    image_label.grid(row = 1, column = 10*c, columnspan = 4, padx = 100, pady = 100)    

# Define the function you want to call when the filebrowser button is clicked.
def fileClick(clicked, dataset, segmentor):
    
    # the path where the images will be stored by plot_visualise
    path2 = 'C:/Python_DS_Assignment'
	
    #get the input picture
    path = os.path.join(os.getcwd(), 'data', 'imgs').replace('\\', '/') + '/'    
    filetypes = ("jpeg files", "*.jpg"), ("all files", "*.*")    
    file_browser = filedialog.askopenfilename(initialdir=path, title="Select 1 file", filetypes=filetypes)    
    data.selected_image = Image.open(file_browser)
    
    # update the entry box
    e.delete(0, 'end')
    e.insert(0, "Image: " + file_browser.split('/')[-1])

    # get the index
    index = file_browser.split('/')[-1].split('.')[0]

    # get the data item with the corresponding index    
    d = dataset[int(index)]    
    plot_visualization(d, path2+"/analysis1/")

# `process` function definition starts from here.
# will process the output when clicked.
def process(clicked):

    if data.selected_image is None:
        label = Label(root, text = "please select an image")
        label.grid(row = 2, column = 0)
        print("Please Select an image")
        return
    DisplayImage(data.selected_image, 0)        
    
    if clicked.get()=="Segmentation":
        im = Image.open("C:/Python_DS_Assignment/analysis1/segmentation.png")        
        DisplayImage(im, 1)
    if clicked.get()=="Bounding-box":
        im = Image.open("C:/Python_DS_Assignment/analysis1/bboxes.png")
        DisplayImage(im, 1)


# `main` function definition starts from here.
if __name__ == '__main__':

    #the path from which we will get the annotation file
    path1 = "C:\\Python_DS_Assignment\\data\\annotations.jsonl"    
	####### CODE REQUIRED (START) ####### (2 lines)
	# Instantiate the root window.
	# Provide a title to the root window.    
    root = Tk()
    root.title("Image Segmentation")
	####### CODE REQUIRED (END) #######

	# Setting up the segmentor model.
    annotation_file = './data/annotations.jsonl'
    transforms = []

	# Instantiate the segmentor model.
    segmentor = InstanceSegmentationModel()
	# Instantiate the dataset.
    dataset = Dataset(annotation_file, transforms=transforms)

	# Declare the options.
    options = ["Segmentation", "Bounding-box"]
    clicked = StringVar()
    clicked.set(options[0])
    option = clicked.get()
    print(clicked.get())

    e = Entry(root, width=70)
    e.grid(row=0, column=0)

    dataset = Dataset(path1, [])
	####### CODE REQUIRED (START) #######
	# Declare the file browsing button
    browse_button = Button(root, text="Browse", command=lambda: fileClick(clicked, dataset, segmentor))
    browse_button.grid(row=0, column=1)
	####### CODE REQUIRED (END) #######

	####### CODE REQUIRED (START) #######
	# Declare the drop-down button
    dropdown_button = OptionMenu(root, clicked, *options)
    dropdown_button.grid(row = 0, column = 2)
	####### CODE REQUIRED (END) #######

	# This is a `Process` button, check out the sample video to know about its functionality
    myButton = Button(root, text="Process", command=lambda: process(clicked))
    myButton.grid(row=0, column=3)
	
	####### CODE REQUIRED (START) ####### (1 line)
	# Execute with mainloop()
    root.mainloop()
    print(clicked.get())
	####### CODE REQUIRED (END) #######
