import random
import matplotlib.pyplot as plt

# Bernoulli dagilimi icin rastgele sayi ureten bir fonksiyon
olaylar = ["6", "6 gelmeme durumu"]
alti_gelme_durumu = 0
alti_gelmeme_durumu = 0

for i in range(100):
    olay = random.random()
    if olay <= 0.6:
        alti_gelme_durumu += 1
    else:
        alti_gelmeme_durumu += 1

sonuclar = [alti_gelme_durumu/1000, alti_gelmeme_durumu/1000] 
plt.bar(olaylar, sonuclar)
plt.title("Sonuç Listesi")
plt.show()