### [2025-08-15] Node/npm not recognized after install (Type: Bug)
- Context: Installed Node.js LTS on Windows to initialize the React frontend (`frontend/web`).
- Symptom: `node -v` and `npm -v` worked in a native Windows PowerShell window but not in the editor's integrated terminal for the project.
- Root cause: The integrated terminal inherited an outdated PATH from before the Node.js installation.
- Resolution: Closed Cursor and all integrated PowerShell terminals, then reopened the editor and terminals. `node`/`npm` became available.
- Commands/Links: `node -v`, `npm -v`, `where.exe node`, `where.exe npm`
- Prevention: After installing system-wide tools (Node, Git, etc.), restart the editor/integrated terminals to refresh environment variables (PATH).

### [2025-08-15] DomainClassifier return key confusion (Type: Bug)
- Context: Using `DomainClassifier.classify(project_data)` to get the predicted industry/domain.
- Symptom: Uncertainty about which key in the returned dictionary contained the classification result.
- Root cause: The `crew.kickoff()` call returns JSON with keys `industry`, `confidence`, and `reasoning`, but downstream code expected a different key (e.g., `domain`).
- Resolution: Standardized on reading the `industry` key from `result.raw` (parsed to dict) and updated references accordingly (tests and any calling code).
- Commands/Links: Reviewed `src/core/domain_classifier.py` and `tests/core/test_domain_classifier.py`.
- Prevention: Document function return shapes in docstrings and enforce via tests; keep a single source of truth for output schema.

### [2025-08-15] Virtual environment activation path issue (Type: Bug)
- Context: Trying to activate Python virtual environment (`.venv`) from subfolders within the project.
- Symptom: `.\venv\Scripts\Activate.ps1` command failed with "not recognized" error when run from `frontend/web` subdirectory.
- Root cause: Virtual environment activation scripts must be run from the directory level where the `.venv` folder is located (project root).
- Resolution: Navigated to the main project directory (`Business Impact Simulator`) and ran `.\.venv\Scripts\Activate.ps1` from there.
- Commands/Links: `cd "C:\Users\emmak\Desktop\Projects\PythonStuff\Business Impact Simulator"`, `.\.venv\Scripts\Activate.ps1`
- Prevention: Always activate virtual environments from the directory containing the `.venv` folder; use absolute paths or navigate to the correct directory first.

### [2025-08-15] 0.0.0.0 vs localhost access issue (Type: Bug)
- Context: FastAPI server started with `host="0.0.0.0"` on port 8001.
- Symptom: Browser could not open `http://0.0.0.0:8001/docs` ("can’t reach this page").
- Root cause: `0.0.0.0` is a listen address for the server, not a routable hostname for the browser.
- Resolution: Used `http://localhost:8001/docs` (or `http://127.0.0.1:8001/docs`) to access the API docs.
- Prevention: When servers log `0.0.0.0`, use `localhost` (or the machine’s IP) in the browser; keep `0.0.0.0` for binding to all interfaces.

### [2025-08-15] CORS preflight blocked POST from React (Type: Bug)
- Context: React app (http://localhost:5173) POSTing JSON to FastAPI (http://localhost:8001/api/process-project).
- Symptom: Browser console showed CORS error: preflight (OPTIONS) failed with no `Access-Control-Allow-Origin` header; POST net::ERR_FAILED.
- Root cause: CORSMiddleware misconfiguration (duplicate `allow_methods`, missing `allow_headers`).
- Resolution: Added proper CORS middleware:
  - `allow_origins=["http://localhost:5173"]`
  - `allow_methods=["*"]`
  - `allow_headers=["*"]`
  Restarted FastAPI server.
- Prevention: Always configure CORS before testing cross-origin requests and verify via Network tab that preflight receives the expected headers.

### [2025-08-15] Git line ending warnings on virtual environment files (Type: Bug)
- Context: Running `git add .` at project root with `.venv/` directory present.
- Symptom: Repeated warnings: "LF will be replaced by CRLF the next time Git touches it" for every file in `.venv/Lib/site-packages/`.
- Root cause: Virtual environment files should not be committed to version control; Git was trying to process thousands of dependency files.
- Resolution: Added `.venv/` to `.gitignore`, then ran `git reset` to unstage everything, followed by `git add .` to re-stage only tracked files.
- Prevention: Always add virtual environment directories (`.venv/`, `node_modules/`, etc.) to `.gitignore` before first commit.
