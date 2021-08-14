# 2nd_year_project
Our 2nd year project
pip3 install-r requirements.txt

![image](https://user-images.githubusercontent.com/51525299/129456948-b9259911-6e87-45c4-acf0-4d34a7906000.png)

Figure shows the entire workflow for the working porotype model which includes the importing of the dataset, the OpenCV module kicks in to start the video stream, next the program detects faces in the video stream, the face mask classifier is applied to the face ROI to determine “mask” or “no mask”, the results are shown in a highlighted box around the face ROI. If a mask is detected, then the program searches for nearby faces, If a mask is not present, the person identification model starts and tries to identify the person. 
