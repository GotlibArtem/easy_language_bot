#!/bin/bash

# ����� ���� ������
pg_dump -U $POSTGRES_USER -h db $POSTGRES_DB > /backups/db_backup_$(date +\%Y-\%m-\%d).sql

# ������� ������ ������ 60 ����
find /backups -type f -name "*.sql" -mtime +60 -exec rm {} \;
