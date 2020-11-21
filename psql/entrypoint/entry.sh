#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	\set pg_ro `echo "$POSTGRES_RO_USER"`
	\set pg_ro_pass `echo "$POSTGRES_RO_PWD"`
	\set pg_db `echo "$POSTGRES_DB"`
	CREATE USER :pg_ro WITH PASSWORD :'pg_ro_pass';
	GRANT CONNECT ON DATABASE grafana TO :pg_ro;
	ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO :pg_ro;
	CREATE TABLE host_resources(
		namespace TEXT NOT NULL,
		dt TIMESTAMP DEFAULT (now() at time zone 'utc'),
		hostname TEXT NOT NULL,
		data JSON NOT NULL
	);
EOSQL
