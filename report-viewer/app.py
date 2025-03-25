# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
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
@app.route("/")
def index():
    test_results = Test_result.query.order_by(Test_result.test_result_seq.desc()).all()
    return render_template('index.html', test_results=test_results)

@app.route("/report")
def report():
    if request.args.get('test_result_seq') is not None:
        # Query Parameter Exists
        query_test_result_seq = request.args.get('test_result_seq')
        test_result = Test_result.query.get(query_test_result_seq)
        test_pipeline_summarys = Test_pipeline_summary.query.order_by(Test_pipeline_summary.test_pipeline_summary_seq).filter(Test_pipeline_summary.test_result_seq == query_test_result_seq)
        test_version_runs = Test_version_run.query.order_by(Test_version_run.test_version_run_seq).filter(Test_version_run.test_result_seq == query_test_result_seq)
        return render_template('report.html', test_result=test_result, test_pipeline_summarys=test_pipeline_summarys, test_version_runs=test_version_runs)
    else:
        # Query Parameter Not Exists
        test_results = Test_result.query.order_by(Test_result.test_result_seq.desc()).all()
        return render_template('index.html', test_results=test_results)

@app.route("/detail")
def detail():
    if request.args.get('test_result_seq') is not None:
        # Query Parameter Exists
        query_test_result_seq = request.args.get('test_result_seq')
        query_test_pipeline_summary_seq = request.args.get('test_pipeline_summary_seq')
        test_result = Test_result.query.get(query_test_result_seq)
        test_pipeline_summary = Test_pipeline_summary.query.get(query_test_pipeline_summary_seq)
        test_task_runs = Test_task_run.query.order_by(Test_task_run.test_task_run_seq).filter(Test_task_run.test_result_seq == query_test_result_seq, Test_task_run.test_group == test_pipeline_summary.test_group, Test_task_run.test_pipeline == test_pipeline_summary.test_pipeline, Test_task_run.simulation_date == test_pipeline_summary.simulation_date)
        return render_template('detail.html', test_result=test_result, test_pipeline_summary=test_pipeline_summary, test_task_runs=test_task_runs)
    else:
        # Query Parameter Not Exists
        test_results = Test_result.query.order_by(Test_result.test_result_seq.desc()).all()
        return render_template('index.html', test_results=test_results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088, debug=True)
