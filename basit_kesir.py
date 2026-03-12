import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Sayfa Yapılandırması
st.set_page_config(page_title="Pizza Kesirleri", layout="wide")

st.title("🍕 Pizza Kesir Karşılaştırıcı")
st.write("Paylar aynı (yenen dilim sayısı), ama pizzayı kaç parçaya bölersek dilimler küçülür?")

# --- GİRİŞ ALANI ---
pay = st.number_input("Kaç dilim yiyeceğiz? (Pay)", min_value=1, max_value=12, value=3)

st.divider()

col1, col2 = st.columns(2)

def pizza_ciz(p, pd, baslik, renk):
    """
    Pizza dilimlerini görselleştiren fonksiyon.
    p: Pay (Yenen dilim)
    pd: Payda (Toplam dilim)
    """
    try:
        # Dilimlerin açısını hesapla
        sizes = [1] * pd
        # Renkleri belirle: İlk 'p' kadar dilim renkli, gerisi gri
        colors = [renk if i < p else '#f0f2f6' for i in range(pd)]
        # Dilimlerin arasındaki çizgiler (patlama efekti yok, bitişik)
        explode = [0.05 if i < p else 0 for i in range(pd)]

        fig, ax = plt.subplots(figsize=(5, 5))
        
        # Pasta grafiği ile pizza dilimi oluşturma
        patches, texts = ax.pie(
            sizes, 
            colors=colors, 
            explode=explode, 
            startangle=90, 
            counterclock=False,
            wedgeprops={"edgecolor": "black", 'linewidth': 1, 'antialiased': True}
        )
        
        ax.set_title(baslik, fontsize=16, fontweight='bold', pad=20)
        return fig
    except Exception as e:
        st.error(f"Grafik çizilemedi: {e}")
        return None

with col1:
    st.subheader("1. Seçenek")
    payda1 = st.slider("Pizzayı kaça bölelim? (Payda)", pay, 12, 4, key="s1")
    st.write(f"Kesir: :blue[{pay}] / :red[{payda1}]")
    
    fig1 = pizza_ciz(pay, payda1, f"{payda1} Dilimli Pizza", "#3498db")
    if fig1:
        st.pyplot(fig1)
    st.info(f"Burada 1 dilim, pizzanın **{100/payda1:.0f}%** kadarı.")

with col2:
    st.subheader("2. Seçenek")
    payda2 = st.slider("Pizzayı kaça bölelim? (Payda)", pay, 12, 10, key="s2")
    st.write(f"Kesir: :blue[{pay}] / :red[{payda2}]")
    
    fig2 = pizza_ciz(pay, payda2, f"{payda2} Dilimli Pizza", "#e67e22")
    if fig2:
        st.pyplot(fig2)
    st.info(f"Burada 1 dilim, pizzanın **{100/payda2:.0f}%** kadarı.")

# --- MANTIKSAL SONUÇ ---
st.divider()
if payda1 < payda2:
    st.success(f"🏆 **{pay}/{payda1}** daha BÜYÜKTÜR! Çünkü dilimler daha geniş.")
elif payda1 > payda2:
    st.success(f"🏆 **{pay}/{payda2}** daha BÜYÜKTÜR! Çünkü dilimler daha geniş.")
else:
    st.warning("İki pizza da özdeş!")
