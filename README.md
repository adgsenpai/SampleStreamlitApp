# Add Two Numbers — Streamlit demo

This is a tiny Streamlit demo app that adds two numbers. It's ready to run locally and to deploy on Streamlit Cloud.

Files added
- `app.py` — Streamlit app (two number inputs, Add button, live preview)
- `requirements.txt` — contains Streamlit dependency
- `.streamlit/config.toml` — minimal server/theme config for Streamlit

Run locally (PowerShell)

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
streamlit run app.py
```

Deploy to Streamlit Cloud

1. Push this repository to GitHub.
2. Go to https://share.streamlit.io and create a new app.
3. Select your GitHub repo and branch and set the entry file to `app.py`.

Notes
- The app uses `st.number_input` so it accepts floats. Change formatting/validation in `app.py` if you prefer integers.
