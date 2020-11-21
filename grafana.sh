docker network create -d bridge grafana
docker run --restart always -d -p 3000:3000 --network grafana --name grafana grafana/grafana
