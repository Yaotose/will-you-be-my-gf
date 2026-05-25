import streamlit as st

no_messages = [
    ("Eh, salah klik kali?", "Coba lagi deh..."),
    ("Masa sih? Yakin?", "Tombol 'Mau' lebih bagus lho..."),
    ("Hiks... oke deh", "Tapi aku bakal nanya lagi kok ehe"),
    ("Kamu jahat tau ga?", "Tombol Mau ada di atas tuh!!!"),
    ("Gapapa, aku sabar orangnya", "...tapi serius deh, pilih Mau"),
    ("Oke aku nangis nih sekarang", ":( tolong pilih Mau..."),
    ("Kamu kuat banget bisa nolak aku", "Tapi coba sekali lagi gimana?"),
    ("Aku udah nanya berkali-kali lho...", "Kapan capeknya???"),
    ("Aku ga akan nyerah!", "Cintaku sebesar galaksi bimasakti"),
    ("Oke aku panggil bala bantuan", "...semua teman kamu udah setuju kita jadian"),
    ("Mungkin kamu belum sadar aja", "Bahwa kita emang jodoh <3"),
    ("Di parallel universe lain", "Kamu udah bilang iya dari tadi"),
    ("Dokter bilang nolak aku itu ga sehat", "Jadi demi kesehatan... pilih Mau Dong"),
    ("Aku udah nanya banyak banget", "Harga diri udah abis, tinggal cinta"),
    ("Oke deal, aku kasi es krim deh", "Nah kan mau sekarang?"),
]

bears = ["(^·ω·^)", "(;-;)", "(T_T)", "(>_<)", "(ง'̀-'́)ง", "(*^3^)", "(:3)", "(´；ω；`)"]

st.set_page_config(page_title="Mau ga jadi pacarku?", page_icon="❤️", layout="centered")

if "no_count" not in st.session_state:
    st.session_state.no_count = 0

no_count = st.session_state.no_count
bear = bears[min(no_count, len(bears) - 1)]

st.markdown(f"<h1 style='text-align: center;'>{bear}</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Mau ga jadi pacar aku?</h2>", unsafe_allow_html=True)

if no_count > 0:
    st.info(f"💔 Sudah ditolak **{no_count} kali**...")

idx = min(no_count - 1, len(no_messages) - 1) if no_count > 0 else 0
question, sub = no_messages[idx] if no_count > 0 else ("Pikir baik-baik ya...", "")

st.write(f"**{question}**")
st.write(sub)

col1, col2 = st.columns([3, 2])

with col1:
    if st.button("**MAU BANGET!!! ❤️**", type="primary", use_container_width=True):
        st.balloons()
        st.success("YEAYYY!!! Makasih banyak ❤️ Kamu bikin aku bahagia banget!")
        st.markdown("<h3 style='text-align: center; color: #ff4b4b;'>(^///^) <3 <3 <3</h3>", unsafe_allow_html=True)
        st.stop()

with col2:
    if st.button("Tidak...", use_container_width=True):
        st.session_state.no_count += 1
        st.rerun()
