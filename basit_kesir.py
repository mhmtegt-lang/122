import matplotlib.pyplot as plt

def kesir_karsilastir(pay, payda1, payda2):
    """
    Payları aynı olan iki kesri yan yana çizer.
    Mavi: Sabit pay (yenen miktar)
    Gri: Kalan miktar
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # 1. Kesir Çizimi
    ax1.barh(['Kesir 1'], [1], color='lightgrey') # Bütün
    ax1.barh(['Kesir 1'], [pay/payda1], color='skyblue') # Yenen kısım
    ax1.set_title(f"Payda: {payda1} (Dilimler Büyük)")
    ax1.set_xlim(0, 1)

    # 2. Kesir Çizimi
    ax2.barh(['Kesir 2'], [1], color='lightgrey') # Bütün
    ax2.barh(['Kesir 2'], [pay/payda2], color='salmon') # Yenen kısım
    ax2.set_title(f"Payda: {payda2} (Dilimler Küçük)")
    ax2.set_xlim(0, 1)

    plt.suptitle(f"Paylar Aynı: {pay} Parça", fontsize=16)
    plt.show()

# TEST: 3/4 mü büyük, 3/10 mu?
# Çalıştırınca görsel olarak 3/4'ün çok daha uzun olduğunu göreceksin.
try:
    kesir_karsilastir(3, 4, 10)
except Exception as e:
    print(f"Hata oluştu: {e}")
