# test_app_code.py
import os, sys
from pathlib import Path

def read_text_file(path: str) -> str:
    try:
        p = Path(path)
        if p.exists():
            return p.read_text(encoding="utf-8").strip()
    except Exception:
        pass
    return ""

def main():
    # env direct
    env_val = os.getenv("APP_CODE")
    if env_val:
        print("APP_CODE via ENV :", repr(env_val))
        sys.exit(0)

    # secrets (si streamlit installé et fichier présent)
    try:
        import streamlit as st
        sec_val = st.secrets.get("APP_CODE", None)
        if sec_val:
            print("APP_CODE via st.secrets :", repr(sec_val))
            sys.exit(0)
    except Exception as e:
        print("st.secrets indisponible :", e.__class__.__name__)

    # APP_CODE_PATH (env ou secrets)
    path = os.getenv("APP_CODE_PATH", "")
    if not path:
        try:
            import streamlit as st
            path = st.secrets.get("APP_CODE_PATH", "")
        except Exception:
            path = ""
    if path:
        print("APP_CODE_PATH utilisé :", path)
        v = read_text_file(path)
        if v:
            print("APP_CODE via fichier :", repr(v))
            sys.exit(0)

    # app_code.txt local
    if Path("app_code.txt").exists():
        v = read_text_file("app_code.txt")
        if v:
            print("APP_CODE via app_code.txt :", repr(v))
            sys.exit(0)

    print("APP_CODE non trouvé ❌")
    sys.exit(1)

if __name__ == "__main__":
    main()
