import cv2

vid = cv2.VideoCapture(0)

if(vid.isOpened() == False):
    print("Iiiih, não conseguimos ler a webcam")

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(width)
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
#print(height)
fps = int(vid.get(cv2.CAP_PROP_FPS))
#print(fps)

while(True):
    ret, frame = vid.read()

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == 32:
        break

vid.release()