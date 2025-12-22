# postgres-skill

Read-only PostgreSQL query skill. Query multiple databases safely with write protection.

## Install

```bash
/plugin marketplace add sanjay3290/postgres-skill
/plugin install postgres@postgres-skill
```

## Setup

1. Copy the example config:
```bash
cp skills/postgres/connections.example.json skills/postgres/connections.json
```

2. Edit with your database credentials:
```json
{
  "databases": [
    {
      "name": "prod",
      "description": "Production - users, orders, transactions",
      "host": "db.example.com",
      "port": 5432,
      "database": "app_prod",
      "user": "readonly",
      "password": "secret",
      "sslmode": "require"
    }
  ]
}
```

3. Secure the config:
```bash
chmod 600 skills/postgres/connections.json
```

## Usage

```bash
# List databases
python3 scripts/query.py --list

# List tables
python3 scripts/query.py --db prod --tables

# Show schema
python3 scripts/query.py --db prod --schema

# Run query
python3 scripts/query.py --db prod --query "SELECT * FROM users" --limit 100
```

## Safety

- **Read-only sessions**: Uses PostgreSQL `readonly=True` mode
- **Query validation**: Only SELECT, SHOW, EXPLAIN, WITH allowed
- **Single statement**: No multi-statement queries
- **Timeouts**: 30s query timeout, 10s connection timeout
- **Memory cap**: Max 10,000 rows per query

## Config

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| name | Yes | - | Database identifier |
| description | Yes | - | What data it contains (for auto-selection) |
| host | Yes | - | Hostname |
| port | No | 5432 | Port |
| database | Yes | - | Database name |
| user | Yes | - | Username |
| password | Yes | - | Password |
| sslmode | No | prefer | disable, allow, prefer, require, verify-ca, verify-full |

## Requirements

- Python 3.8+
- psycopg2-binary

```bash
pip install -r skills/postgres/requirements.txt
```

## License

Apache-2.0
