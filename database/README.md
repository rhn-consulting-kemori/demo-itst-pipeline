# Postgresql set up
## Podman
#### podman pod create --name report-pod -p 5432:5432,8088:8088,8089:8089
#### podman run --name postgres-srv --pod report-pod -e POSTGRES_PASSWORD=postgres -d postgres:16
#### podman exec -it postgres-srv bash
#### psql -U postgres