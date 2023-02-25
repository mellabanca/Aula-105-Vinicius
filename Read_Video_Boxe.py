import cv2

vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if(vid.isOpened() == False):
    print("Iiiih, não conseguimos ler a webcam")

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(width)
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
#print(height)
fps = int(vid.get(cv2.CAP_PROP_FPS))
#print(fps)

newVideo = cv2.VideoWriter("Boxe slow motion.mp4",cv2.VideoWriter_fourcc(*'DIVX'), 10, (width, height))

while(True):
    ret, frame = vid.read()

    cv2.imshow("Video legal boxe", frame)

    newVideo.write(frame)

    if cv2.waitKey(100) == 32:
        break

vid.release()
newVideo.release()
vid.destroyAllWindows()