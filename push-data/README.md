# Push Data
## Build
#### podman build -t push-data .
## Run
#### podman run -d --pod report-pod --volume /Users/kemori/dev/demo/mount/push-data/data:/app/data -e URL_PUSH_DATA="localhost:8089/api/test_result" --name push-data push-data
