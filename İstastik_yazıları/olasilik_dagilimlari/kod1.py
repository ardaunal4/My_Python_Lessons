import random
import matplotlib.pyplot as plt

olaylar = ["yazı", "tura"]
yazi = 0
tura = 0
for i in range(1000):
    rastgele_secim = random.choice(olaylar)
    if rastgele_secim == "yazı":
        yazi += 1
    else:
        tura += 1
sonuclar = [yazi/1000, tura/1000] 
plt.bar(olaylar, sonuclar)
plt.title("Sonuç Listesi")
plt.show()
