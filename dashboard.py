import streamlit as st
import json
from cryptography.fernet import Fernet

# ========== CONFIG ==========
MASTER_PASSWORD = "1234"  # Ton code PIN à remplacer !
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# ========== SESSION ==========
if "auth" not in st.session_state:
    st.session_state.auth = False

# ========== LOGIN ==========
if not st.session_state.auth:
    pwd = st.text_input("🔑 Entrez votre code secret :", type="password")
    if pwd == MASTER_PASSWORD:
        st.session_state.auth = True
        st.success("Accès autorisé ✅")
    else:
        st.warning("Accès refusé 🚫")
    st.stop()

st.title("📌 Mon Dashboard Perso")

# ===== Onglets =====
menu = st.sidebar.radio("Navigation", ["Liens", "Objectifs", "Coffre-fort"])

# ===== Liens =====
if menu == "Liens":
    st.subheader("🌍 Liens importants")
    links = {
        "MOOC Python": "https://www.coursera.org/learn/python",
        "LinkedIn": "https://www.linkedin.com",
        "GitHub": "https://github.com"
    }
    for name, url in links.items():
        st.markdown(f"[{name}]({url})")

# ===== Objectifs =====
elif menu == "Objectifs":
    st.subheader("🎯 Objectifs")
    objectifs = {
        "Projet SmartWeigh": 70,
        "Cours MOOC Élec": 40,
        "CV/LinkedIn": 90
    }
    for obj, val in objectifs.items():
        st.write(f"**{obj}** : {val}%")
        st.progress(val)

# ===== Coffre-fort (mots de passe) =====
elif menu == "Coffre-fort":
    st.subheader("🔐 Coffre-fort")
    data = {
        "Gmail": "monemail@gmail.com|password123",
        "Ynov": "brice|monmdp"
    }
    for site, cred in data.items():
        enc = cipher.encrypt(cred.encode())
        dec = cipher.decrypt(enc).decode()
        with st.expander(f"🔑 {site}"):
            st.code(dec)
