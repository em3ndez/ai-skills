# AI Agent Skills

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/sanjay3290/ai-skills)

A collection of portable skills for AI coding assistants. Works with all major AI clients that support the [Agent Skills Standard](https://agentskills.io).

## Supported AI Clients

<p align="center">
  <a href="#claude-code"><img src="https://img.shields.io/badge/Claude_Code-D97757?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code" /></a>
  <a href="#gemini-cli"><img src="https://img.shields.io/badge/Gemini_CLI-8E75B2?style=for-the-badge&logo=google&logoColor=white" alt="Gemini CLI" /></a>
  <a href="#google-antigravity"><img src="https://img.shields.io/badge/Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Antigravity" /></a>
  <a href="#cursor"><img src="https://img.shields.io/badge/Cursor-000000?style=for-the-badge&logo=cursor&logoColor=white" alt="Cursor" /></a>
  <a href="#openai-codex-cli"><img src="https://img.shields.io/badge/OpenAI_Codex-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI Codex" /></a>
  <a href="#goose"><img src="https://img.shields.io/badge/Goose-FF6B35?style=for-the-badge&logo=go&logoColor=white" alt="Goose" /></a>
</p>

| Client | Skills Directory | Documentation |
|--------|-----------------|---------------|
| **Claude Code** | `~/.claude/skills/` or `.claude/skills/` | [docs](https://docs.anthropic.com/en/docs/claude-code/skills) |
| **Gemini CLI** | `~/.gemini/skills/` or `.gemini/skills/` | [docs](https://geminicli.com/docs/cli/skills/) |
| **Google Antigravity** | `~/.gemini/antigravity/skills/` or `.agent/skills/` | [docs](https://antigravity.google/docs/skills) |
| **Cursor** | `~/.cursor/skills/` or `.cursor/skills/` | [docs](https://cursor.com/docs/context/skills) |
| **OpenAI Codex CLI** | `~/.codex/skills/` or `.codex/skills/` | [docs](https://developers.openai.com/codex/skills/) |
| **Goose** | `~/.config/goose/skills/` or `.goose/skills/` | [docs](https://block.github.io/goose/docs/guides/context-engineering/using-skills/) |

## Available Skills

| Skill | Description |
|-------|-------------|
| [postgres](skills/postgres/) | Read-only PostgreSQL queries with defense-in-depth security |
| [imagen](skills/imagen/) | AI image generation using Google Gemini (cross-platform) |
| [deep-research](skills/deep-research/) | Autonomous multi-step research using Gemini Deep Research Agent |
| [outline](skills/outline/) | Search, read, and manage Outline wiki documents |
| [jules](skills/jules/) | Delegate coding tasks to Google Jules AI agent (async bug fixes, docs, tests, features) |

### Google Workspace Skills

Lightweight alternatives to the full [Google Workspace MCP server](https://github.com/gemini-cli-extensions/workspace). Each skill has standalone OAuth authentication with cross-platform token storage via keyring.

> **⚠️ Requires Google Workspace account.** Personal Gmail accounts are not supported. These skills use the same OAuth infrastructure as the official Google Workspace MCP.

| Skill | Description |
|-------|-------------|
| [google-chat](skills/google-chat/) | List spaces, send messages, DMs, create spaces |
| [google-docs](skills/google-docs/) | Create, read, edit Google Docs |
| [google-sheets](skills/google-sheets/) | Read spreadsheets, get ranges, find sheets |
| [google-slides](skills/google-slides/) | Read presentations, get text and metadata |
| [google-drive](skills/google-drive/) | Search files, list folders, download files |
| [google-calendar](skills/google-calendar/) | Events, scheduling, free time lookup |
| [gmail](skills/gmail/) | Search, read, send emails, manage labels |

## Installation

### Option 1: Clone entire repository

```bash
# Clone to your preferred skills directory
git clone https://github.com/sanjay3290/ai-skills.git ~/.claude/skills/ai-skills

# Or for other clients:
# git clone https://github.com/sanjay3290/ai-skills.git ~/.gemini/skills/ai-skills
# git clone https://github.com/sanjay3290/ai-skills.git ~/.gemini/antigravity/skills/ai-skills
# git clone https://github.com/sanjay3290/ai-skills.git ~/.cursor/skills/ai-skills
# git clone https://github.com/sanjay3290/ai-skills.git ~/.codex/skills/ai-skills
# git clone https://github.com/sanjay3290/ai-skills.git ~/.config/goose/skills/ai-skills
```

### Option 2: Copy individual skills

```bash
# Example: Install just the postgres skill
cp -r skills/postgres ~/.claude/skills/
```

### Option 3: Symlink for development

```bash
# Symlink skills for easy updates
ln -s /path/to/ai-skills/skills/postgres ~/.claude/skills/postgres
ln -s /path/to/ai-skills/skills/imagen ~/.claude/skills/imagen
```

### Client-Specific Installation

#### Claude Code
```bash
# Global installation
cp -r skills/* ~/.claude/skills/

# Or project-level
cp -r skills/* .claude/skills/
```

#### Gemini CLI
```bash
# Global installation
cp -r skills/* ~/.gemini/skills/

# Or workspace-level
cp -r skills/* .gemini/skills/
```

#### Google Antigravity
```bash
# Global installation
cp -r skills/* ~/.gemini/antigravity/skills/

# Or workspace-level
cp -r skills/* .agent/skills/
```

#### Cursor
```bash
# Global installation
cp -r skills/* ~/.cursor/skills/

# Or project-level
cp -r skills/* .cursor/skills/
```

#### OpenAI Codex CLI
```bash
# Global installation
cp -r skills/* ~/.codex/skills/

# Or repository-level
cp -r skills/* .codex/skills/
```

#### Goose
```bash
# Global installation
cp -r skills/* ~/.config/goose/skills/

# Or project-level
cp -r skills/* .goose/skills/
```

## Skill Setup

Each skill may require additional configuration:

### Postgres
Create `connections.json` in the skill directory with your database credentials. See [postgres/README.md](skills/postgres/README.md).

### Imagen & Deep Research
```bash
export GEMINI_API_KEY=your-api-key
```
Get a free key at [Google AI Studio](https://aistudio.google.com/).

> **Note:** Deep Research tasks take 2-10 minutes and cost $2-5 per query.

### Outline
```bash
export OUTLINE_API_KEY=your-api-key
export OUTLINE_API_URL=https://your-wiki.example.com/api  # Optional
```
Get your API key from your Outline wiki settings.

### Jules
```bash
# Install CLI (one-time)
npm install -g @google/jules

# Authenticate (opens browser)
jules login
```
Connect your GitHub repos at [jules.google.com](https://jules.google.com). Jules works asynchronously - create a task, it runs in the background, then pull results when complete.

### Google Workspace Skills
Each Google Workspace skill requires the `keyring` library and first-time authentication:
```bash
# Install dependency (one-time)
pip install keyring

# Authenticate for the skill you need (opens browser)
python ~/.claude/skills/ai-skills/skills/google-chat/scripts/auth.py login
python ~/.claude/skills/ai-skills/skills/google-docs/scripts/auth.py login
python ~/.claude/skills/ai-skills/skills/google-sheets/scripts/auth.py login
python ~/.claude/skills/ai-skills/skills/google-slides/scripts/auth.py login
python ~/.claude/skills/ai-skills/skills/google-drive/scripts/auth.py login
python ~/.claude/skills/ai-skills/skills/google-calendar/scripts/auth.py login
python ~/.claude/skills/ai-skills/skills/gmail/scripts/auth.py login
```
Tokens stored securely via system keyring:
- **macOS**: Keychain
- **Windows**: Windows Credential Locker
- **Linux**: Secret Service API (GNOME Keyring, KDE Wallet, etc.)

## Usage

Once installed, skills activate automatically based on your requests. Just ask naturally:

### Postgres
- "Query my production database for active users"
- "Show me the schema of the orders table"
- "How many signups last week?"

### Imagen
- "Generate an image of a sunset over mountains"
- "Create an app icon for my weather app"
- "I need a hero image for my landing page"

### Deep Research
- "Research the competitive landscape of EV batteries"
- "Compare React, Vue, and Angular frameworks"
- "What are the latest developments in Kubernetes?"

### Outline
- "Search the wiki for deployment guide"
- "Read the onboarding documentation"
- "Create a new wiki page for the API spec"

### Jules
- "Have Jules fix the authentication bug in src/auth.js"
- "Delegate adding unit tests to Jules"
- "Ask Jules to add documentation to the API module"
- "Check my Jules sessions" / "Pull the results from Jules"

### Google Workspace
- "List my Google Chat spaces" / "Send a message to Project Alpha"
- "Create a new Google Doc about the project proposal"
- "Get the content of my Q4 Budget spreadsheet"
- "What's on my calendar tomorrow?"
- "Search my Gmail for invoices from last month"
- "Find files named 'report' in my Drive"

## Skill Structure

All skills follow the [Agent Skills Standard](https://agentskills.io):

```
skill-name/
├── SKILL.md              # Required: Instructions for the AI agent
├── README.md             # Human documentation
├── requirements.txt      # Dependencies (if any)
├── .env.example          # Environment variable template
└── scripts/              # Executable scripts
    └── main.py
```

The `SKILL.md` file uses YAML frontmatter:

```yaml
---
name: skill-name
description: "When to use this skill"
---

# Instructions for the AI agent
```

## Contributing

1. Fork this repository
2. Create a new skill in `skills/your-skill-name/`
3. Include `SKILL.md` with proper frontmatter
4. Add documentation in `README.md`
5. Submit a pull request

## Credits

- **Google Workspace Skills** - Based on the official [Google Workspace MCP server](https://github.com/gemini-cli-extensions/workspace) by the Gemini CLI team. Uses their OAuth cloud function for authentication.

## License

Apache-2.0

<!--
## Awesome Lists (for PR submissions when adding new skills)

| Repository | Fork | Notes |
|------------|------|-------|
| github.com/BehiSecc/awesome-claude-skills | sanjay3290/awesome-claude-skills-1 | Active, PRs merge quickly |
| github.com/travisvn/awesome-claude-skills | sanjay3290/awesome-claude-skills-3 | Uses table format for Individual Skills |
| github.com/Prat011/awesome-llm-skills | sanjay3290/awesome-llm-skills | Multi-LLM focus (Claude, Codex, Gemini, etc.) |
| github.com/ComposioHQ/awesome-claude-skills | sanjay3290/awesome-claude-skills | Composio-maintained, has connect-apps plugin |

Skill placement by category:
- postgres: Data & Analysis
- imagen: Creative & Media
- deep-research: Data & Analysis / Scientific & Research
- outline: Collaboration & Project Management
- jules: Development & Automation
- google-*: Collaboration & Project Management (all Google Workspace skills)
- gmail: Collaboration & Project Management
-->
