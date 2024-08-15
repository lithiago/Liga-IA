import cv2 as cv

""" img = cv.imread("images/cat_large.jpg")

cv.imshow("Cat", img) """

def rescaleFrame(frame, scale = 0.75):
    #Usual para fotos, videos e videos ao vivo
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #Usual somente para videos ao vivo
    capture.set(3,width)
    capture.set(4,height)
capture = cv.VideoCapture("videos/dog.mp4")

while True:
    #Esse método retorna se a captura do frame de um vídeo foi bem sucedidade e retorna o frame atual 
    isRead, frame = capture.read()

    frameResized = rescaleFrame(frame)
    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frameResized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)