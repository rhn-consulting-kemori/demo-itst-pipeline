# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.json.ensure_ascii = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://{user}:{password}@{host}:{port}/{dbName}'.format(
        user = os.getenv('DB_USER', 'postgres'),
        password = os.getenv('DB_PASS', 'postgres'),
        host = os.getenv('DB_HOST', '127.0.0.1'),
        port = os.getenv('DB_PORT', '5432'),
        dbName = os.getenv('DB_NAME', 'postgres')
    ) # PostgreSQL接続用のURI
db = SQLAlchemy(app)

# Database Mapping
class Test_result(db.Model):
    test_result_seq = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.String(), nullable=False)
    test_name = db.Column(db.String(255))
    test_description = db.Column(db.String(255))
    run_count = db.Column(db.Integer)
    ok_count = db.Column(db.Integer)
    ng_count = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime('%Y%m%d %H:%M:%S'))

class Test_pipeline_summary(db.Model):
    test_pipeline_summary_seq = db.Column(db.Integer, primary_key=True)
    test_result_seq = db.Column(db.Integer, nullable=False)
    test_id = db.Column(db.String(), nullable=False)
    test_group = db.Column(db.String(255))
    test_pipeline = db.Column(db.String(255))
    simulation_date = db.Column(db.Date)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    run_count = db.Column(db.Integer)
    ok_count = db.Column(db.Integer)
    ng_count = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime('%Y%m%d %H:%M:%S'))

class Test_task_run(db.Model):
    test_task_run_seq = db.Column(db.Integer, primary_key=True)
    test_result_seq = db.Column(db.Integer, nullable=False)
    test_id = db.Column(db.String(), nullable=False)
    test_group = db.Column(db.String(255))
    test_pipeline = db.Column(db.String(255))
    test_task = db.Column(db.String(255))
    simulation_date = db.Column(db.Date)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    test_result = db.Column(db.String(), nullable=False)
    evidence_link = db.Column(db.String())
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime('%Y%m%d %H:%M:%S'))

class Test_version_run(db.Model):
    test_version_run_seq = db.Column(db.Integer, primary_key=True)
    test_result_seq = db.Column(db.Integer, nullable=False)
    test_id = db.Column(db.String(), nullable=False)
    sw_category = db.Column(db.String())
    sw_id = db.Column(db.String())
    sw_name = db.Column(db.String(255))
    sw_version = db.Column(db.String())
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime('%Y%m%d %H:%M:%S'))

# Root
@app.route('/api/test_result', methods=['POST'])
def add_test_result():
    # data : { "test_id": "", "test_name": "", "test_description": "" }
    data = request.get_json()

    # timestamp
    timestamp = datetime.now().strftime('%Y%m%d %H:%M:%S')

    # Insert data set
    test_result = Test_result(
        test_id=data['test_id'],
        test_name=data['test_name'],
        test_description=data['test_description'],
        run_count=0,
        ok_count=0,
        ng_count=0,
        create_time=timestamp
    )

    # insert
    db.session.add(test_result)
    db.session.commit()

    # get result
    get_test_results = Test_result.query.filter(Test_result.test_id == data['test_id'], Test_result.create_time == timestamp)
    
    return_text = {}
    for get_test_result in get_test_results:
        # response
        return_text = {
            'test_result_seq': get_test_result.test_result_seq,
            'test_id': get_test_result.test_id,
            'test_name': get_test_result.test_name,
            'test_description': get_test_result.test_description,
            'create_time': get_test_result.create_time
        }

    # return
    return jsonify(return_text), 201

@app.route('/api/test_task', methods=['POST'])
def add_test_task():
    # data :
    # { 
    #   "test_result_seq": 9, "test_id": "", "test_group": "", "test_pipeline": "", "test_task": "", 
    #   "simulation_date": "", "start_time": "", "end_time": "", "test_result": "", "evidence_link": "", 
    #   "sw_category": "", "sw_id": "", "sw_name": "", "sw_version": ""
    # }
    data = request.get_json()

    # timestamp
    timestamp = datetime.now().strftime('%Y%m%d %H:%M:%S')

    # Insert data set
    if data['simulation_date'] is None or len(data['simulation_date']) == 0:
        test_task_run = Test_task_run(
            test_result_seq=data['test_result_seq'],
            test_id=data['test_id'],
            test_group=data['test_group'],
            test_pipeline=data['test_pipeline'],
            test_task=data['test_task'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            test_result=data['test_result'],
            evidence_link=data['evidence_link'],
            create_time=timestamp
        )
        # insert
        db.session.add(test_task_run)
        db.session.commit()
    else:
        test_task_run = Test_task_run(
            test_result_seq=data['test_result_seq'],
            test_id=data['test_id'],
            test_group=data['test_group'],
            test_pipeline=data['test_pipeline'],
            test_task=data['test_task'],
            simulation_date=data['simulation_date'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            test_result=data['test_result'],
            evidence_link=data['evidence_link'],
            create_time=timestamp
        )
        # insert
        db.session.add(test_task_run)
        db.session.commit()

    # get test_version_run
    if data['sw_category'] is None or len(data['sw_category']) == 0:
        pass
    elif data['sw_id'] is None or len(data['sw_id']) == 0:
        pass
    elif data['sw_version'] is None or len(data['sw_version']) == 0:
        pass
    else:
        get_test_version_runs = Test_version_run.query.filter(Test_version_run.test_result_seq == data['test_result_seq'], Test_version_run.sw_category == data['sw_category'], Test_version_run.sw_id == data['sw_id'], Test_version_run.sw_version == data['sw_version'])

        counter = 0
        for get_test_version_run in get_test_version_runs:
            counter = counter + 1
        
        if counter == 0:
            test_version_run = Test_version_run(
                test_result_seq=data['test_result_seq'],
                test_id=data['test_id'],
                sw_category=data['sw_category'],
                sw_id=data['sw_id'],
                sw_name=data['sw_name'],
                sw_version=data['sw_version'],
                create_time=timestamp
            )
            # insert
            db.session.add(test_version_run)
            db.session.commit()
    
    # response
    return_text = {
        'test_result_seq': data['test_result_seq'],
        'test_id': data['test_id'],
        'test_group': data['test_group'],
        'test_pipeline': data['test_pipeline'],
        'test_task': data['test_task'],
        'start_time': data['start_time'],
        'end_time': data['end_time'],
        'test_result': data['test_result'],
        'status': "created"
    }

    # return
    return jsonify(return_text), 201

@app.route('/api/pipeline_summary', methods=['POST'])
def add_test_pipeline_summary():
    # data : { "test_result_seq": 9, "test_id": "", "test_group": "", "test_pipeline": "", "simulation_date": "" }
    data = request.get_json()

    # timestamp
    timestamp = datetime.now().strftime('%Y%m%d %H:%M:%S')

    # get Test_task_run
    if data['simulation_date'] is None or len(data['simulation_date']) == 0:
        test_task_runs = Test_task_run.query.filter(Test_task_run.test_result_seq == data['test_result_seq'], Test_task_run.test_group == data['test_group'], Test_task_run.test_pipeline == data['test_pipeline'])
    else:
        test_task_runs = Test_task_run.query.filter(Test_task_run.test_result_seq == data['test_result_seq'], Test_task_run.test_group == data['test_group'], Test_task_run.test_pipeline == data['test_pipeline'], Test_task_run.simulation_date == data['simulation_date'])

    # counter
    start_time = datetime(2900, 1, 1)
    end_time = datetime(1900, 1, 1)
    run_count = 0
    ok_count = 0
    ng_count = 0

    for test_task_run in test_task_runs:
        # count
        run_count = run_count + 1
        if test_task_run.test_result == "OK":
            ok_count = ok_count + 1
        elif test_task_run.test_result == "NG":
            ng_count = ng_count + 1
        else:
            pass

        # start_time
        # datetime_start1 = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        # datetime_start2 = datetime.strptime(test_task_run.start_time, "%Y-%m-%d %H:%M:%S")
        if start_time < test_task_run.start_time:
            start_time = start_time
        else:
            start_time = test_task_run.start_time

        # end_time
        # datetime_end1 = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        # datetime_end2 = datetime.strptime(test_task_run.end_time, "%Y-%m-%d %H:%M:%S")
        if end_time > test_task_run.end_time:
            end_time = end_time
        else:
            end_time = test_task_run.end_time

    
    if data['simulation_date'] is None or len(data['simulation_date']) == 0:
        get_test_pipeline_summarys = Test_pipeline_summary.query.filter(Test_pipeline_summary.test_result_seq == data['test_result_seq'], Test_pipeline_summary.test_group == data['test_group'], Test_pipeline_summary.test_pipeline == data['test_pipeline'])
        counter = 0
        for get_test_pipeline_summary in get_test_pipeline_summarys:
            get_test_pipeline_summary.start_time = start_time
            get_test_pipeline_summary.end_time = end_time
            get_test_pipeline_summary.run_count = run_count
            get_test_pipeline_summary.ok_count = ok_count
            get_test_pipeline_summary.ng_count = ng_count
            # update
            db.session.commit()
            counter = counter + 1
        
        if counter == 0:
            test_pipeline_summary = Test_pipeline_summary(
                test_result_seq=data['test_result_seq'],
                test_id=data['test_id'],
                test_group=data['test_group'],
                test_pipeline=data['test_pipeline'],
                start_time=start_time,
                end_time=end_time,
                run_count=run_count,
                ok_count=ok_count,
                ng_count=ng_count,
                create_time=timestamp
            )
            # insert
            db.session.add(test_pipeline_summary)
            db.session.commit()

    else:
        get_test_pipeline_summarys = Test_pipeline_summary.query.filter(Test_pipeline_summary.test_result_seq == data['test_result_seq'], Test_pipeline_summary.test_group == data['test_group'], Test_pipeline_summary.test_pipeline == data['test_pipeline'], Test_pipeline_summary.simulation_date == data['simulation_date'])
        counter = 0
        for get_test_pipeline_summary in get_test_pipeline_summarys:
            get_test_pipeline_summary.start_time = start_time
            get_test_pipeline_summary.end_time = end_time
            get_test_pipeline_summary.run_count = run_count
            get_test_pipeline_summary.ok_count = ok_count
            get_test_pipeline_summary.ng_count = ng_count
            # update
            db.session.commit()
            counter = counter + 1
        
        if counter == 0:
            test_pipeline_summary = Test_pipeline_summary(
                test_result_seq=data['test_result_seq'],
                test_id=data['test_id'],
                test_group=data['test_group'],
                test_pipeline=data['test_pipeline'],
                simulation_date=data['simulation_date'],
                start_time=start_time,
                end_time=end_time,
                run_count=run_count,
                ok_count=ok_count,
                ng_count=ng_count,
                create_time=timestamp
            )
            # insert
            db.session.add(test_pipeline_summary)
            db.session.commit()
    
    # response
    if data['simulation_date'] is None or len(data['simulation_date']) == 0:
        return_text = {
            'test_result_seq': data['test_result_seq'],
            'test_id': data['test_id'],
            'test_group': data['test_group'],
            'test_pipeline': data['test_pipeline'],
            'start_time': start_time,
            'end_time': end_time,
            'run_count': run_count,
            'ok_count': ok_count,
            'ng_count': ng_count,
            'status': "success"
        }
    else:
        return_text = {
            'test_result_seq': data['test_result_seq'],
            'test_id': data['test_id'],
            'test_group': data['test_group'],
            'test_pipeline': data['test_pipeline'],
            'simulation_date': data['simulation_date'],
            'start_time': start_time,
            'end_time': end_time,
            'run_count': run_count,
            'ok_count': ok_count,
            'ng_count': ng_count,
            'status': "success"
        }

    # return
    return jsonify(return_text), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8089, debug=True)
