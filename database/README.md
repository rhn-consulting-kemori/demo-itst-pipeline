# Postgresql set up
## Podman
#### podman pod create --name db-pod -p 5432:5432
#### podman run --name postgres-srv --pod db-pod -e POSTGRES_PASSWORD=postgres -d postgres:16
#### podman exec -it postgres-srv bash
#### psql -U postgres