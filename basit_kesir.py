import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Kesir Karşılaştırıcı", layout="centered")

st.title("🍕 Kesirleri Karşılaştıralım")
st.write("Paylar (yediğimiz dilim sayısı) aynı, ama dilimlerin boyu farklı!")

# --- GÜVENLİ VE BASİT GİRİŞ ---
# Sabit Pay (Mavi renk kodlaması önerisi)
pay = st.number_input("Kaç dilim yiyeceğiz? (Pay)", min_value=1, max_value=10, value=3)

st.divider()

# İki farklı kesir için kolonlar
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Pizza")
    payda1 = st.slider("Kaç parçaya bölünsün?", 1, 20, 4, key="p1")
    deger1 = pay / payda1
    
    if deger1 > 1:
        st.warning("Dilim sayısı pizza sayısını geçti!")
    else:
        # Görsel Çubuk (Progress bar basit bir görseldir)
        st.write(f"Kesir: :blue[{pay}] / :red[{payda1}]")
        st.progress(deger1)
        st.caption(f"Dilimler oldukça BÜYÜK!")

with col2:
    st.subheader("2. Pizza")
    payda2 = st.slider("Kaç parçaya bölünsün?", 1, 20, 10, key="p2")
    deger2 = pay / payda2
    
    if deger2 > 1:
        st.warning("Dilim sayısı pizza sayısını geçti!")
    else:
        st.write(f"Kesir: :blue[{pay}] / :red[{payda2}]")
        st.progress(deger2)
        st.caption(f"Dilimler çok KÜÇÜK!")

# --- MANTIKSAL ÇIKARIM ---
st.divider()

if payda1 < payda2:
    st.success(f"Sonuç: **{pay}/{payda1}** kesri daha BÜYÜKTÜR! Çünkü pizza daha az parçaya bölündü, dilimler dev gibi kaldı.")
elif payda1 > payda2:
    st.success(f"Sonuç: **{pay}/{payda2}** kesri daha KÜÇÜKTÜR! Çünkü pizza çok fazla parçaya bölündü, dilimler küçüldü.")
else:
    st.info("İki kesir birbirine eşit.")

# --- DİSKALKULİ NOTU ---
st.info("💡 **Unutma:** Alttaki sayı (payda) ne kadar büyürse, sana düşen dilim o kadar küçülür!")
