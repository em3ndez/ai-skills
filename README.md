# ai-skills

Collection of agent skills for AI coding assistants.

## Installation

### Step 1: Add the marketplace
```bash
/plugin marketplace add sanjay3290/ai-skills
```

### Step 2: Install a skill
```bash
/plugin install postgres@ai-skills
/plugin install imagen@ai-skills
```

### Verify installation
```bash
/plugin list
```

## Available Skills

| Skill | Description |
|-------|-------------|
| [postgres](skills/postgres/) | Read-only PostgreSQL queries with defense-in-depth security |
| [imagen](skills/imagen/) | AI image generation using Google Gemini (cross-platform) |

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

**Note:** Imagen requires a `GEMINI_API_KEY` environment variable. Get a free key at [Google AI Studio](https://aistudio.google.com/).

## License

Apache-2.0
