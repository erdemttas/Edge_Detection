import cv2   #Gerekli Kütüphaneler İmport Edilir.
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktarma, 0 Diyerek Siyah beyaz aktarılır.
img = cv2.imread("london.jpg",0)

#Color Map siyah ve beyazın tonları olsun ve görselleştirilsin.
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off")

#Canny algoritması sayesinde threshold yani eşik değerlerini ayarlayarak kenarları daha iyi tespit ediyoruz.
edges = cv2.Canny(image = img, threshold1 = 0, threshold2 = 255)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off")

# resmimizin medyan değerini buluyoruz
med_val = np.median(img)
print(med_val)

#resmimizin Alt ve üst threshold değerini bulma.
low = int(max(0, (1 - 0.33)*med_val))
high = int(min(255, (1 + 0.33)*med_val))

print(low)
print(high)

#resmimizin medyan değerine göre bulduğumuz threshold değerlerine göre yeniden görselleştirme yapıyoruz.
edges = cv2.Canny(image = img, threshold1 = low, threshold2 = high)
plt.figure(), plt.imshow(edges, cmap = "gray"), plt.axis("off")

# Resimdeki su kısımını daha az belirgin yapmak için blur yöntemini kullanıyoruz.
blurred_img = cv2.blur(img, ksize =(5,5))
plt.figure(), plt.imshow(blurred_img, cmap="gray"), plt.axis("off")

med_val = np.median(blurred_img)
print(med_val)

# Blur laştırılmış görsele göre yeniden medyan değeri belirliyoruz.
med_val = np.median(blurred_img)
print(med_val)

# alt ve üst threshold değerleri belirliyoruz yeniden.
low = int(max(0, (1 - 0.33)*med_val))
high = int(min(255, (1 + 0.33)*med_val))

print(low)
print(high)

# ve en son olarak yeni değerlerle resmimizi görselleştiriyoruz.
edges = cv2.Canny(image = blurred_img, threshold1 = low, threshold2 = high)
plt.figure(), plt.imshow(edges, cmap = "gray"), plt.axis("off")




















