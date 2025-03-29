# Report Viewer
## Build
#### podman build -t report-viewer .
## Run
#### podman run -d --pod report-pod --name report-viewer report-viewer

## VENV
#### source /Users/kemori/dev/python/py3-13-2/bin/activate
#### deactivate

oc new-app https://github.com/rhn-consulting-kemori/demo-itst-pipeline.git --context-dir=report-viewer -e DB_HOST=postgresql.demo-report.svc.cluster.local --name=report-viewer
