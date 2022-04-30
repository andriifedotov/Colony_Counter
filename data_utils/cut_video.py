import cv2
vidcap = cv2.VideoCapture('/home/andrii/data/colony_dataset/videos/video_2.mp4')
success,image = vidcap.read()
count = 67
success = True
while success:
  success,image = vidcap.read()
  cv2.imwrite(f"/home/andrii/data/colony_dataset/images/frame_{count}.jpg", image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1
