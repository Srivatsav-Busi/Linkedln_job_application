# LinkedIn AI Auto Job Applier

Automates LinkedIn job applications with a local Chrome session and a lightweight UI to view applied jobs history.

## What you need to configure
Only these items are required for a generic setup:
- LinkedIn login email + password
- Job roles to search for
- Resume file path

## Quick start (bot runs locally)
### Windows
1. Install Python 3.10+ from python.org and ensure it is added to PATH.
2. Install Google Chrome (stable).
3. Install Python packages (bot + UI + optional AI features):
   ```powershell
   py -m pip install --upgrade pip
   py -m pip install -r requirements.txt
   ```
4. Create `.env` from the example:
   ```powershell
   copy .env.example .env
   ```
5. Edit `.env` and set:
   - `LINKEDIN_USERNAME`
   - `LINKEDIN_PASSWORD`
   - `SEARCH_TERMS` (comma-separated)
   - `DEFAULT_RESUME_PATH`
6. Run the bot (Chrome opens on your machine):
   ```powershell
   py runAiBot.py
   ```

### macOS
1. Install Python 3.10+ (python.org or Homebrew).
2. Install Google Chrome (stable).
3. Install Python packages (bot + UI + optional AI features):
   ```bash
   python3 -m pip install --upgrade pip
   python3 -m pip install -r requirements.txt
   ```
4. Create `.env` from the example:
   ```bash
   cp .env.example .env
   ```
5. Edit `.env` and set:
   - `LINKEDIN_USERNAME`
   - `LINKEDIN_PASSWORD`
   - `SEARCH_TERMS` (comma-separated)
   - `DEFAULT_RESUME_PATH`
6. Run the bot (Chrome opens on your machine):
   ```bash
   python3 runAiBot.py
   ```

## Optional: local overrides (no .env)
If you prefer a git-ignored local file:
1. Copy `config/local.py.example` to `config/local.py`.
2. Edit `ENV_OVERRIDES` in `config/local.py`.

## Applied Jobs UI (Docker or local)
The UI runs in Docker and reads history from `all excels/` on your host.
```bash
docker compose up --build
```
Then open `http://localhost:5000`.

You can also run the UI locally:
```bash
python app.py
```

## Troubleshooting
- Chrome opens but nothing happens: close extra Chrome tabs and retry (the bot expects a clean session).
- ChromeDriver errors: update Chrome to the latest version and rerun.
- UI shows no data: make sure `all excels/all_applied_applications_history.csv` exists and has headers.
- macOS permissions: if clicks/typing don’t work, grant Terminal (or your IDE) Accessibility + Screen Recording in System Settings.
- Windows permissions: if clicks/typing don’t work, run the terminal as Administrator.

## Notes
- The bot runs locally so Chrome can open on your system (Windows or macOS).
- Secrets are never committed; `.env` and `config/local.py` are git-ignored.
- Applied jobs history CSVs live in `all excels/`.
- `undetected-chromedriver` downloads a compatible driver automatically on both Windows and macOS.

## Required files and folders (don’t skip)
- `.env` (create from `.env.example`)
- `config/secrets.py` (LinkedIn creds via env, AI provider + keys if used)
- `config/personals.py` (your profile details)
- `config/questions.py` (answers + `default_resume_path`)
- `config/search.py` (search terms/location, filters)
- `config/settings.py` (runtime behavior)
- `config/local.py` (optional overrides from `config/local.py.example`)
- `all resumes/` (store your resume files, match `DEFAULT_RESUME_PATH`)
- `all excels/all_applied_applications_history.csv` (created/updated by the bot)

## License
AGPLv3. See `LICENSE`.
