- Kinect V2 Setup Instructions

Install Windows 10. Required by Kinect V2 driver.
Link: https://www.microsoft.com/en-us/software-download/windows10%20
Install Python 3.7.9 (due to compatibility issue with numpy and comtypes)
open command prompt
install git: winget install --id Git.Git -e --source winget
close and reopen cmd to enable git
pip install comtypes==1.1.4
pip install git+https://github.com/Kinect/PyKinect2.git
pip install pygame
pip install opencv-python
Install Kinect for Windows SDK 2.0: https://www.microsoft.com/en-us/download/details.aspx?id=44561.
check if Kinect sensor is detected from Device Manager. May need a few times retry.


Video data from the Kinect sensor includes low-level data, such as infrared and color, as well as processed data, like depth and body (commonly referred to as skeleton). 

The DepthFrame Class represents a frame where each pixel represents the distance of the closest object seen by that pixel. The data for this frame is stored as 16-bit unsigned integers, where each value represents the distance in millimeters. The maximum depth distance is 8 meters, although reliability starts to degrade at around 4.5 meters. Developers can use the depth frame to build custom tracking algorithms in cases where the BodyFrame Class isn’t enough.

The BodyFrame Class contains all the computed real-time tracking information about people that are in view of the sensor. The computed info includes skeletal joints and orientations, hand states, and more for up to 6 people at a time.

Setup Windows Boot without Login
Go Settings -> Search Sign-in options -> Password -> leave new password empty
