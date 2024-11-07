#!/bin/bash

# Бэкап базы данных
pg_dump -U $POSTGRES_USER -h db $POSTGRES_DB > /backups/db_backup_$(date +\%Y-\%m-\%d).sql

# Удаляем бэкапы старше 60 дней
find /backups -type f -name "*.sql" -mtime +60 -exec rm {} \;
