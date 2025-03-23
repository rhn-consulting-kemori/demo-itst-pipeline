CREATE TABLE test_result(  
    test_result_seq int NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    test_id VARCHAR NOT NULL,
    test_name VARCHAR(255),
    test_description VARCHAR(255),
    run_count int,
    ok_count int,
    ng_count int,
    create_time timestamp
);

CREATE TABLE test_pipeline_summary(  
    test_pipeline_summary_seq int NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    test_result_seq int NOT NULL,
    test_id VARCHAR NOT NULL,
    test_group VARCHAR(255),
    test_pipeline VARCHAR(255),
    simulation_date DATE,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    run_count int,
    ok_count int,
    ng_count int,
    create_time TIMESTAMP
);

CREATE TABLE test_task_run(  
    test_task_run_seq int NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    test_result_seq int NOT NULL,
    test_id VARCHAR NOT NULL,
    test_group VARCHAR(255),
    test_pipeline VARCHAR(255),
    test_task VARCHAR(255),
    simulation_date DATE,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    test_result VARCHAR NOT NULL,
    evidence_link VARCHAR,
    create_time TIMESTAMP
);

CREATE TABLE test_version_run(
    test_version_run_seq int NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    test_result_seq int NOT NULL,
    test_id VARCHAR NOT NULL,
    sw_category VARCHAR,
    sw_id VARCHAR,
    sw_name VARCHAR(255),
    sw_version VARCHAR,
    create_time TIMESTAMP
);
