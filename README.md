# 📌 Mon Dashboard Perso — déploiement (privé)

## 1) Lancer en local
```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

## 2) Secrets requis (sécurité)
Sur **Streamlit Cloud** (Settings → Secrets) :
```
MASTER_PASSWORD="ton_pin_fort"
FERNET_KEY="ta_clé_fernet_base64"
```
> Générez `FERNET_KEY` une fois (localement) :
```python
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
```

## 3) Déploiement depuis un repo **privé**
- Connecte Streamlit Cloud à ton GitHub et autorise l'accès aux **repos privés**.
- Sélectionne ton repo privé, la branche et le fichier principal `dashboard.py`.
- Renseigne les **Secrets** (ci-dessus). Si tu ne mets pas `FERNET_KEY`, le déchiffrement échouera.
- Par défaut, ton app est **non indexée** et tu peux **inviter des viewers** par email.

> Si quota atteint / pas d’accès aux repos privés :  
> - Rends le repo **public** le temps du déploiement (puis re-privatise), ou  
> - Utilise **Render** (Web Service, Python) et définis `MASTER_PASSWORD` et `FERNET_KEY` comme **Environment Variables**.

## 4) Structure du repo
```
dashboard.py
requirements.txt
data.json           # (facultatif; l'app crée un défaut sinon)
```

## 5) Points d’attention
- Ne commit **jamais** des mots de passe en clair. Les champs sont chiffrés via `FERNET_KEY`.
- En local, un fichier `key.key` peut être créé automatiquement si `FERNET_KEY` est absent. Sur le cloud, **toujours** fournir `FERNET_KEY` via secrets.
- Si l’app “bloque” après login, vérifie :
  - que `MASTER_PASSWORD` lu par l’app est bien celui que tu saisis ;
  - que `FERNET_KEY` n’a pas changé (sinon les secrets déjà chiffrés seront illisibles) ;
  - qu’il n’y a pas de `st.stop()` avant le rendu des pages ;
  - que `data.json` est lisible (sinon supprimer et relancer).

## 6) Alternatives d’hébergement (si repo privé bloqué)
- **Render.com** (gratuit de base) : service web Python, spécifie `streamlit run dashboard.py` comme commande, expose le port via Render (auto).
- **Hugging Face Spaces** (Gradio/Streamlit) : privé = payant ; public = gratuit.
- **Railway / Fly.io / Deta Space** : variables d’environnement + build Python.

Bon déploiement !