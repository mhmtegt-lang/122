import streamlit as st

st.set_page_config(page_title="Kesir Modeli", layout="wide")

st.title("🍕 Kesirleri Sayarak Öğrenelim")
st.write("Paylar aynı (mavi kutular), ama payda büyüdükçe kutular küçülüyor!")

# --- GİRİŞ ALANI ---
pay = st.number_input("Kaç dilim yiyeceğiz? (Pay)", min_value=1, max_value=10, value=3)

st.divider()

col1, col2 = st.columns(2)

def kesir_ciz(p, pd, renk):
    """
    Her bir paydayı bir kutu olarak çizen görsel fonksiyon.
    Diskalkuli dostu: Parçalar tek tek sayılabilir.
    """
    st.write(f"### Kesir: :blue[{p}] / :red[{pd}]")
    
    # Kutuları yan yana dizmek için dinamik kolonlar oluşturuyoruz
    cols = st.columns(pd)
    for i in range(pd):
        with cols[i]:
            if i < p:
                # Yenen (seçilen) dilimler renkli
                st.markdown(f"""<div style="background-color:{renk}; height:50px; border:2px solid black; border-radius:5px; text-align:center; color:white; font-weight:bold; padding-top:10px;">{i+1}</div>""", unsafe_allow_html=True)
            else:
                # Kalan dilimler boş/gri
                st.markdown(f"""<div style="background-color:#f0f2f6; height:50px; border:1px dashed #ced4da; border-radius:5px;"></div>""", unsafe_allow_html=True)

with col1:
    st.info("1. SEÇENEK")
    payda1 = st.slider("Pizza kaç parçaya bölünsün?", 1, 12, 4, key="s1")
    kesir_ciz(pay, payda1, "#3498db") # Mavi kutular
    if payda1 < 5:
        st.caption("Dilimler kocaman! Karnın doyar.")

with col2:
    st.info("2. SEÇENEK")
    payda2 = st.slider("Pizza kaç parçaya bölünsün?", 1, 12, 10, key="s2")
    kesir_ciz(pay, payda2, "#e67e22") # Turuncu kutular
    if payda2 > 8:
        st.caption("Dilimler minicik kaldı...")

# --- MANTIKSAL SONUÇ ---
st.divider()
if payda1 < payda2:
    st.success(f"🏆 **{pay}/{payda1}** daha büyüktür! Çünkü kutular daha geniş.")
elif payda1 > payda2:
    st.success(f"🏆 **{pay}/{payda2}** daha büyüktür! Çünkü kutular daha geniş.")
else:
    st.warning("İkisi de eşit boyda.")
