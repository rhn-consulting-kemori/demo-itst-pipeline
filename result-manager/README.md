# Report Manager
## Build
#### podman build -t result-manager .
## Run
#### podman run -d --pod report-pod --name result-manager result-manager

## VENV
#### source /Users/kemori/dev/python/py3-13-2/bin/activate
#### deactivate

## Data
curl -X POST -H "Content-Type: application/json" -d '{"test_id": "@", "test_name": "@", "test_description": "@"}' http://127.0.0.1:8089/api/test_result

curl -X POST -H "Content-Type: application/json" -d '{"test_result_seq":@, "test_id": "@", "test_group": "@", "test_pipeline": "@", "test_task": "@","simulation_date": "@", "start_time": "@", "end_time": "@", "test_result": "@", "evidence_link": "@", "sw_category": "@", "sw_id": "@", "sw_name": "@", "sw_version": "@"}' http://127.0.0.1:8089/api/test_task

curl -X POST -H "Content-Type: application/json" -d '{"test_result_seq": @, "test_id": "@", "test_group": "@", "test_pipeline": "@", "simulation_date": "@"}' http://127.0.0.1:8089/api/pipeline_summary

curl -X POST -H "Content-Type: application/json" -d '{"test_result_seq": 2}' http://127.0.0.1:8089/api/test_result_summary