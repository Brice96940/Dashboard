# dashboard.py
import os
import streamlit as st

# ─────────── Sécurité très simple (pas de crypto) ───────────
# Dans Streamlit Cloud > Settings > Secrets, ajoute par ex.:
# APP_CODE = "mon-code-super-secret"
APP_CODE = os.getenv("APP_CODE") or st.secrets.get("APP_CODE", "")

# État d'authentification en session
if "auth" not in st.session_state:
    st.session_state.auth = False

def login_view():
    st.write("🔑 Entrez votre code secret :")
    code = st.text_input("Code", type="password")
    if code:
        if code.strip() == APP_CODE and APP_CODE:
            st.session_state.auth = True
            st.success("Accès autorisé ✅")
        else:
            st.error("Accès refusé 🚫 (code incorrect)")
    st.stop()  # bloque le reste tant que non authentifié

# Affiche l'écran de login si non connecté
if not st.session_state.auth:
    login_view()

# ─────────── App une fois connecté ───────────
st.title("📌 Mon Dashboard Perso")

menu = st.sidebar.radio("Navigation", ["Liens", "Objectifs", "Coffre-fort"])

# ===== Liens =====
if menu == "Liens":
    st.subheader("🌍 Liens importants")
    links = {
        "MOOC Python": "https://www.coursera.org/learn/python",
        "LinkedIn": "https://www.linkedin.com",
        "GitHub": "https://github.com",
    }
    for name, url in links.items():
        st.markdown(f"- [{name}]({url})")

# ===== Objectifs =====
elif menu == "Objectifs":
    st.subheader("🎯 Objectifs")
    objectifs = {
        "Projet SmartWeigh": 70,
        "Cours MOOC Élec": 40,
        "CV/LinkedIn": 90,
    }
    for obj, val in objectifs.items():
        st.write(f"**{obj}** : {val}%")
        st.progress(val)

# ===== Coffre-fort (démo sans chiffrement) =====
elif menu == "Coffre-fort":
    st.subheader("🔐 Coffre-fort (démo)")
    st.info("⚠️ Démo uniquement : pas de chiffrement, données stockées en mémoire de session.")

    if "vault" not in st.session_state:
        st.session_state.vault = {
            "Gmail": "monemail@gmail.com | password123",
            "Ynov": "brice | monmdp",
        }

    with st.form("add_secret"):
        site  = st.text_input("Site / Service", placeholder="Ex: Github")
        ident = st.text_input("Identifiant", placeholder="email ou login")
        mdp   = st.text_input("Mot de passe", type="password")
        add   = st.form_submit_button("Ajouter")
        if add:
            if site and ident and mdp:
                st.session_state.vault[site] = f"{ident} | {mdp}"
                st.success("Ajouté ✅")
            else:
                st.error("Tous les champs sont requis.")

    st.markdown("---")
    for site, cred in st.session_state.vault.items():
        with st.expander(f"🔑 {site}", expanded=False):
            st.code(cred)

# Bouton de déconnexion
st.sidebar.button("Se déconnecter", on_click=lambda: st.session_state.update(auth=False))
