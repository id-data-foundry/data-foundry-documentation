---
layout: default
title: Database Settings
parent: Configuration
nav_order: 1
---

# Database Settings

Data Foundry uses a relational database to store user information, project metadata, and dataset configurations.

## Database Types

*   **Development (H2):** By default, in development mode, Data Foundry uses an in-memory H2 database. This is fast but volatile; data is lost when the server stops unless configured to persist to a file.
    ```hocon
    db.default.url="jdbc:h2:mem:play;DB_CLOSE_DELAY=-1"
    ```

*   **Production (PostgreSQL):** For production environments, we strongly recommend using PostgreSQL. This is configured in the `DF-production.yaml` Docker Compose file.

## Backup and Restore

Data preservation is critical.

### Automated Backups
If running via Docker Compose, ensure the database volume (e.g., `postgres-data`) is backed up regularly. You can use standard tools like `pg_dump` to create SQL dumps of the database container.

```bash
docker exec -t <db-container-name> pg_dumpall -c -U dfuser > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
```

### Restore
To restore, you would pipe the dump file back into the `psql` command of the container.

```bash
cat your_dump.sql | docker exec -i <db-container-name> psql -U dfuser
```
