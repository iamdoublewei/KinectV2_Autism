import numpy as np
import pickle
import cv2
import ctypes
import os
parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime

#REMEBER TO HAVE A KINECT CONNECTED (OR KINECT STUDIO REPLAYING A RECORDING) WHEN RUNNING, EVEN THOUGH WE ARE OPERATING OFF SAVED DATA!
def get_3D_coordinates(filename):    
    
    #load your saved depth data
    depthdatafile = open(filename + ".pickle", "rb")
    
    #Iterate over each saved frame of depth data
    depth_file_not_finished = True

    while depth_file_not_finished == True:
        try:
            depthframe = pickle.load(depthdatafile)[0] #each call loads a sucessive frame from a pickle file, so we need to do this once per frame
            #print(depthframe[2])
                                               
            cut_down_depth_frame = depthframe.astype(np.uint8)
            cut_down_depth_frame = np.reshape(cut_down_depth_frame, (424, 512))
               
            cv2.imshow('KINECT Video Stream', cut_down_depth_frame)
                    
            #code to close window if escape is pressed, doesnt do anything in this program (as we keep calling for data to be displayed in the window) but included for reference
            key = cv2.waitKey(1)
            if key == 27: 
                pass
                
       #close loop at end of file
        except EOFError:
            cv2.destroyAllWindows()
            depth_file_not_finished = False

    

if __name__ == '__main__': 
    
    #replace name below with the corresponding section of the name of your saved depth data (for reference, the full name of my saved depth data file was DEPTH.test.1.29.13.17.pickle)
    get_3D_coordinates('2024-05-20')
