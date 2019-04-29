import cv2
import numpy as np

def auto_canny(image, sigma=0.33):
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    return edged
metodo = cv2.THRESH_BINARY+cv2.THRESH_OTSU
imagem = cv2.imread("images (3).jpeg")
classificador = cv2.CascadeClassifier("PlacaMercoSul.xml")
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

PlacasDetectadas= classificador.detectMultiScale(imagemCinza,scaleFactor=1.2,minNeighbors=5)
print(PlacasDetectadas)
print("Placas Detectadas: ", len(PlacasDetectadas))
for (x, y, l, a) in PlacasDetectadas:
    cv2.rectangle(imagem, (x - 5, y +5), (x + l + 5, y + a - 4 ), (0, 255, 0), 1)
    corte = imagem[(y + 5):y + a -4 , (x - 5):x + l+ 5]
#img = cv2.cvtColor(corte,cv2.COLOR_BGR2GRAY)
#imgFiltrada = cv2.GaussianBlur(img,(3,3),0)
#_,imgThrs = cv2.threshold(imgFiltrada,0,255,metodo)
#imgCanny = auto_canny(imgThrs)
#cv2.imshow("Detector haar", imgCanny)
cv2.imshow('img original',corte)
cv2.waitKey(0)

cv2.destroyAllWindows()
