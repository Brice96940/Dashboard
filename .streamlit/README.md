# 📌 Dashboard Perso – Streamlit

Un tableau de bord **personnel et sécurisé** développé avec **Streamlit**, permettant de :

- 🌍 Gérer des **liens rapides**
- 🎯 Suivre ses **objectifs**
- 🔐 Enregistrer des données sensibles (coffre-fort démo)
- 👤 Gérer son **compte** (identifiant et mot de passe)

## 🚀 Fonctionnalités

- **Login sécurisé** avec identifiant et mot de passe stockés en **local** (`local_auth.json`).
- **Fallback par défaut** → si le fichier n’existe pas, il est créé avec :
  - Identifiant : `brice`
  - Mot de passe : `1234@`
- **Formulaire de changement de mot de passe** directement dans l’app.
- **Option de sauvegarde** : écriture d’une copie du mot de passe en clair dans `password_backup.txt` (⚠️ seulement si activé).
- **Stockage ignoré par Git** → tes secrets ne seront jamais poussés en ligne.

---

## 🛠️ Installation

### 1) Cloner le projet

```bash
git clone <ton_repo>
cd <ton_repo>
```

### 2) Créer un environnement virtuel

```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

### 3) Installer les dépendances

```bash
pip install streamlit pandas
```

---

## ▶️ Lancer l’application

```bash
python -m streamlit run dashboard.py
```

Ouvre ensuite l’URL locale affichée (souvent `http://localhost:8501/`).

---

## 🔑 Authentification

### Première utilisation

- Identifiant : **brice**
- Mot de passe : **1234@**

*(le fichier `local_auth.json` est créé automatiquement au premier lancement)*

### Changer son mot de passe

- Va dans l’onglet **Compte**
- Saisis ton **mot de passe actuel**
- Choisis un **nouveau mot de passe**
- Optionnel : coche *“Écrire une copie en clair”* → sauvegarde dans `password_backup.txt`

---

## 📂 Structure des fichiers

```
dashboard.py          # Code principal Streamlit
local_auth.json       # Stocke identifiant et mot de passe hashé (SHA-256)
password_backup.txt   # (optionnel) copie en clair du mot de passe
.venv/                # Environnement virtuel Python
.gitignore            # Empêche de pousser tes secrets
```

---

## ⚠️ Sécurité

- `local_auth.json` contient uniquement le **hash du mot de passe** (pas le mot de passe en clair).
- `password_backup.txt` n’est créé que si tu coches l’option → sinon inutile.
- Les deux fichiers sont **exclus de Git** via `.gitignore`.

---

## 📌 Exemple `.gitignore`

```gitignore
# Secrets locaux
local_auth.json
password_backup.txt

# Streamlit local secrets (si tu utilises)
.streamlit/secrets.toml

# Python / venv
.venv/
__pycache__/
*.pyc
```

---

## 🎯 Roadmap (évolution possible)

- Ajouter un chiffrement réel pour le coffre-fort (AES/Fernet).
- Connecter l’auth locale avec ton grand dashboard **Pipeline & KPI**.
- Support multi-utilisateurs avec rôles.
