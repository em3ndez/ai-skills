# agent-skills

Collection of agent skills for AI coding assistants.

## Installation

### Step 1: Add the marketplace
```bash
/plugin marketplace add sanjay3290/agent-skills
```

### Step 2: Install a skill
```bash
/plugin install postgres@agent-skills
```

### Verify installation
```bash
/plugin list
```

## Available Skills

| Skill | Description |
|-------|-------------|
| [postgres](skills/postgres/) | Read-only PostgreSQL queries with defense-in-depth security |

## Usage

Once installed, the skill activates automatically when you ask about PostgreSQL queries. Just ask naturally:

- "Query my production database for active users"
- "Show me the schema of the orders table"
- "How many signups last week?"

## License

Apache-2.0
