# NotebookLM Skill

NotebookLM integration for AI skills with persistent auth, notebook/source management, sync flows, and structured query exports.

## Highlights

- Persistent browser profile auth with named profiles (`--profile work`, `--profile personal`)
- Local notebook library (`library.json`) and source hash state (`source_state.json`)
- Single ask, batch ask, and cross-notebook comparison ask
- Remote notebook and source operations (create/list/add/delete/sync)
- Hash dedupe for file uploads (skip unchanged sources)
- Source filtering controls (`--include-ext`, `--exclude`, `--max-size`, `--modified-since`)
- `--dry-run` support for destructive/bulk operations
- Retry + diagnostics (`--retries`, screenshot/HTML artifact capture)
- Optional JSON/Markdown exports to notes folder for auditing

By default, operations run silently/headless in the background.
Use `--show-browser` only for debugging selectors or behavior.

## Requirements

- Python 3.9+
- Playwright

Install dependencies:

```bash
pip install -r requirements.txt
```

Install browser once:

```bash
python -m playwright install chromium
```

## Scripts

### Authentication (Profile-Aware)

```bash
# Check default profile auth
python scripts/auth_manager.py status

# Setup auth for a named profile
python scripts/auth_manager.py setup --profile work

# Re-auth profile
python scripts/auth_manager.py reauth --profile work

# Clear one profile or all profiles
python scripts/auth_manager.py clear --profile work
python scripts/auth_manager.py clear --all-profiles

# List known profiles
python scripts/auth_manager.py profiles
```

### Notebook Library

```bash
python scripts/notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "My Docs" \
  --description "Internal documentation notebook" \
  --topics "api,architecture,runbooks"

python scripts/notebook_manager.py list
python scripts/notebook_manager.py activate --id my-docs
python scripts/notebook_manager.py search --query api
python scripts/notebook_manager.py stats
```

### Ask Questions

```bash
# Single question (active notebook)
python scripts/ask_question.py --question "How does auth work?"

# Single question by URL/profile
python scripts/ask_question.py \
  --question "What topics are covered?" \
  --notebook-url "https://notebooklm.google.com/notebook/..." \
  --profile work

# Batch ask in one notebook
python scripts/ask_question.py \
  --questions "summarize architecture||list security controls||what are risks" \
  --notebook-id my-docs

# Batch from file
python scripts/ask_question.py --questions-file ./questions.txt --notebook-id my-docs

# Compare same question across multiple notebooks
python scripts/ask_question.py \
  --question "What is the deployment process?" \
  --compare-notebook-ids "ops-docs,eng-docs"

# Export result as markdown under notes/
python scripts/ask_question.py \
  --question "Summarize key takeaways" \
  --notebook-id my-docs \
  --export-format markdown \
  --save-notes
```

### Remote Notebook Operations

```bash
# List visible account notebooks
python scripts/remote_manager.py list-remote --profile work

# Create notebook remotely and save to local library
python scripts/remote_manager.py create-remote \
  --name "My New Notebook" \
  --description "Notebook scope and purpose" \
  --topics "topic1,topic2" \
  --profile work

# Dry-run notebook creation
python scripts/remote_manager.py create-remote --name "My New Notebook" --dry-run
```

### Source Operations

```bash
# List sources
python scripts/remote_manager.py list-sources --notebook-id my-docs

# Add copied text
python scripts/remote_manager.py add-source \
  --notebook-id my-docs \
  --text "My source text"

# Add URL source
python scripts/remote_manager.py add-source \
  --notebook-id my-docs \
  --url "https://example.com"

# Upload files from folder recursively with filters
python scripts/remote_manager.py add-source \
  --notebook-id my-docs \
  --dir "/path/to/source-folder" \
  --recursive \
  --include-ext "md,txt,pdf" \
  --exclude "*.tmp" \
  --max-size "10MB" \
  --modified-since "14d"

# Upload through temporary copy workflow
python scripts/remote_manager.py add-source \
  --notebook-id my-docs \
  --dir "/path/to/source-folder" \
  --copy-to-temp

# Dry-run delete
python scripts/remote_manager.py delete-source \
  --notebook-id my-docs \
  --source-title "draft" \
  --contains --all-matches --dry-run

# Delete for real
python scripts/remote_manager.py delete-source \
  --notebook-id my-docs \
  --source-title "draft" \
  --contains --all-matches
```

### Source Sync (Desired State)

```bash
# Sync folder to notebook, add/update only
python scripts/remote_manager.py sync-sources \
  --notebook-id my-docs \
  --dir "/path/to/source-folder" \
  --recursive

# Full sync including remote deletions for missing local files
python scripts/remote_manager.py sync-sources \
  --notebook-id my-docs \
  --dir "/path/to/source-folder" \
  --recursive \
  --delete-missing

# Sync using manifest + dry-run preview
python scripts/remote_manager.py sync-sources \
  --notebook-id my-docs \
  --manifest ./source-manifest.json \
  --dry-run
```

## Reliability Controls

Use on `ask_question.py` and `remote_manager.py` commands:

```bash
--retries 3
--artifacts-dir /tmp/notebooklm-artifacts
--profile work
--show-browser
```

On retryable failures, screenshots and HTML dumps are captured for debugging.

## Tests

```bash
# Unit tests
pytest -q skills/notebooklm/tests

# Live smoke test (requires authenticated profile)
NOTEBOOKLM_E2E=1 NOTEBOOKLM_SMOKE_PROFILE=work pytest -q skills/notebooklm/tests -m smoke
```

## Data Location

By default, local data is stored at:

`~/.config/claude/notebooklm-skill/`

- `chrome_profile/` - default persistent browser profile
- `profiles/<name>/` - named profile browser data
- `library.json` - local notebook metadata
- `source_state.json` - source hash state for dedupe/sync
- `artifacts/` - screenshots/HTML from failed attempts
- `notes/` - exported JSON/Markdown outputs

Override base data dir with:

```bash
export NOTEBOOKLM_DATA_DIR=/custom/path
```
