import os


# def countdown(t): 
    
#     while t: 
#         mins, secs = divmod(t, 60) 
#         timer = '{:02d}:{:02d}'.format(mins, secs) 
#         print(timer, end="\r") 
#         time.sleep(1) 
#         t -= 1

# def scriptchange():
# 	os.system('python3.8 /home/anirudh/Desktop/2nd_year_project/ai_progect_face_recognition.py')
# 	sys.exit("NO MASK FACE DETECTED!!")







# 	t=5
# 	if withoutMask:
# 		countdown(int(t))
# 		scriptchange()
# 	else:
# 		continue





# 	tuple = ((1,2),(2.3))


os.execv("usr/bin/python3", "/home/anirudh/Desktop/2nd_year_project/detect_mask_video.py")