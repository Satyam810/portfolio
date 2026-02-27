# Satyam Kumar Portfolio - FIXED VERSION

## IMPORTANT: Stop the old Flask server first!
Press Ctrl+C in your terminal to stop the old server.
Then delete the old folder completely.
Then run this new version.

## Run locally with Flask:
```
pip install flask gunicorn
python app.py
```
Open: http://127.0.0.1:5000

## Deploy to Vercel (free, 5 minutes):
1. Go to github.com -> New repository -> name: "portfolio"
2. Upload ALL files from this folder
3. Go to vercel.com -> New Project -> Import the repo -> Deploy
4. Done!

## Files:
- index.html  = Complete portfolio (all sections, photo, animations)
- app.py       = Flask backend
- vercel.json  = Vercel config
- requirements.txt = Python packages
- Procfile     = For Render/Heroku
