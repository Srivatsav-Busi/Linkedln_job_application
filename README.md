# LinkedIn AI Auto Job Applier

Automates LinkedIn job applications with a local Chrome session and a lightweight UI to view applied jobs history.

## What you need to configure
Only these items are required for a generic setup:
- LinkedIn login email + password
- Job roles to search for
- Resume file path

## Quick start (bot runs locally)
1. Install Python 3.10+.
2. Install bot dependencies:
   ```bash
   pip install undetected-chromedriver pyautogui selenium
   ```
3. Create `.env` from the example:
   ```bash
   cp .env.example .env
   ```
4. Edit `.env` and set:
   - `LINKEDIN_USERNAME`
   - `LINKEDIN_PASSWORD`
   - `SEARCH_TERMS` (comma-separated)
   - `DEFAULT_RESUME_PATH`
5. Run the bot (Chrome opens on your machine):
   ```bash
   python runAiBot.py
   ```

## Optional: local overrides (no .env)
If you prefer a git-ignored local file:
1. Copy `config/local.py.example` to `config/local.py`.
2. Edit `ENV_OVERRIDES` in `config/local.py`.

## Docker: Applied Jobs UI only
The UI runs in Docker and reads history from `all excels/` on your host.
```bash
docker compose up --build
```
Then open `http://localhost:5000`.

## Troubleshooting
- Chrome opens but nothing happens: close extra Chrome tabs and retry (the bot expects a clean session).
- ChromeDriver errors: update Chrome to the latest version and rerun.
- UI shows no data: make sure `all excels/all_applied_applications_history.csv` exists and has headers.

## Notes
- The bot runs locally so Chrome can open on your system (Windows or macOS).
- Secrets are never committed; `.env` and `config/local.py` are git-ignored.
- Applied jobs history CSVs live in `all excels/`.

## License
AGPLv3. See `LICENSE`.
