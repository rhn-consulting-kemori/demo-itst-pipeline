# Report Viewer
## Build
#### podman build -t result-manager .
## Run
#### podman run -d --pod report-pod --name result-manager result-manager

## VENV
#### source /Users/kemori/dev/python/py3-13-2/bin/activate
#### deactivate

## Data
curl -X POST -H "Content-Type: application/json" -d '{"test_id": "ST-E001-00000003", "test_name": "追加テスト", "test_description": "Insertテストの確認"}' http://127.0.0.1:8089/api/test_result

curl -X POST -H "Content-Type: application/json" -d '{"test_result_seq":4, "test_id": "ST-E001-00000003", "test_group": "環境立上", "test_pipeline": "環境構築", "test_task": "NameSpace作成","simulation_date": "", "start_time": "2025-03-24 00:25:00", "end_time": "2025-03-24 00:26:00", "test_result": "OK", "evidence_link": "-", "sw_category": "", "sw_id": "", "sw_name": "", "sw_version": ""}' http://127.0.0.1:8089/api/test_task

curl -X POST -H "Content-Type: application/json" -d '{"test_result_seq":4, "test_id": "ST-E001-00000003", "test_group": "テストシナリオ", "test_pipeline": "オンライン立上", "test_task": "売上受付","simulation_date": "2025-03-12", "start_time": "2025-03-24 00:25:00", "end_time": "2025-03-24 00:26:00", "test_result": "OK", "evidence_link": "-", "sw_category": "オンライン", "sw_id": "ON000001", "sw_name": "売上受付", "sw_version": "1.0.0"}' http://127.0.0.1:8089/api/test_task

curl -X POST -H "Content-Type: application/json" -d '{"test_result_seq": 4, "test_id": "ST-E001-00000003", "test_group": "環境立上", "test_pipeline": "環境構築", "simulation_date": ""}' http://127.0.0.1:8089/api/pipeline_summary

curl -X POST -H "Content-Type: application/json" -d '{"test_result_seq": 4, "test_id": "ST-E001-00000003", "test_group": "テストシナリオ", "test_pipeline": "オンライン立上", "simulation_date": "2025-03-12"}' http://127.0.0.1:8089/api/pipeline_summary
