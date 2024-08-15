import cv2 as cv


#Esse método pega o caminho de uma figura e retorna a imagem como uma matriz de pixels

#img = cv.imread("images/cat_large.jpg")

#Esse método exibe a imagem em uma nova janela. O método possui dois parâmetros o nome da janela e a matriz de pixels.

#cv.imshow("Cat", img)


#Lendo vídeos

#Esse método captura o caminho de um vídeo ou a imagem da câmera do seu computador, para capturar a câmera você deve digitar um inteiro começando de 0 para sua webcam, 1 para uma segunda camera conectada e assim por diante.
capture = cv.VideoCapture("videos/dog.mp4")

while True:
    #Esse método retorna se a captura do frame de um vídeo foi bem sucedidade e retorna o frame atual 
    isRead, frame = capture.read()

    cv.imshow("Video", frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
