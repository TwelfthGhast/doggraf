#!/bin/sh

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' grafana-psql
