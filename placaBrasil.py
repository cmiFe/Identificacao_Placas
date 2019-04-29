import cv2
import numpy as np


imagem = cv2.imread("images (3).jpeg")
classificador = cv2.CascadeClassifier("PlacaMercoSul.xml")
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

PlacasDetectadas= classificador.detectMultiScale(imagemCinza,scaleFactor=1.2,minNeighbors=5)
print(PlacasDetectadas)
print("Placas Detectadas: ", len(PlacasDetectadas))
for (x, y, l, a) in PlacasDetectadas:
    cv2.rectangle(imagem, (x - 5, y +5), (x + l + 5, y + a - 4 ), (0, 255, 0), 1)
    corte = imagem[(y + 5):y + a -4 , (x - 5):x + l+ 5]
    
cv2.imshow('img original',corte)
cv2.waitKey(0)

cv2.destroyAllWindows()
