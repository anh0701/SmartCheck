CREATE TABLE product (
    id              SERIAL PRIMARY KEY,
    code            VARCHAR(30) UNIQUE NOT NULL,
    name            VARCHAR(100) NOT NULL,
    description     TEXT,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE detection_class (
    id              SERIAL PRIMARY KEY,
    name            VARCHAR(50) UNIQUE NOT NULL,
    description     TEXT
);

CREATE TABLE inspection_stage (
    id              SERIAL PRIMARY KEY,
    code            VARCHAR(30) UNIQUE NOT NULL,
    name            VARCHAR(100) NOT NULL
);

CREATE TABLE inspection_standard (

    id                  SERIAL PRIMARY KEY,

    product_id          INTEGER NOT NULL,

    stage_id            INTEGER NOT NULL,

    class_id            INTEGER NOT NULL,

    required_quantity   INTEGER NOT NULL CHECK(required_quantity >= 0),

    FOREIGN KEY(product_id)
        REFERENCES product(id),

    FOREIGN KEY(stage_id)
        REFERENCES inspection_stage(id),

    FOREIGN KEY(class_id)
        REFERENCES detection_class(id),

    UNIQUE(product_id, stage_id, class_id)
);

CREATE TABLE inspection (

    id                  BIGSERIAL PRIMARY KEY,

    product_id          INTEGER NOT NULL,

    stage_id            INTEGER NOT NULL,

    image_path          TEXT,

    status              VARCHAR(20) NOT NULL,

    processing_time_ms  INTEGER,

    inspected_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(product_id)
        REFERENCES product(id),

    FOREIGN KEY(stage_id)
        REFERENCES inspection_stage(id)
);

CREATE TABLE detection_result (

    id                  BIGSERIAL PRIMARY KEY,

    inspection_id       BIGINT NOT NULL,

    class_id            INTEGER NOT NULL,

    confidence          NUMERIC(5,4),

    x_min               INTEGER,

    y_min               INTEGER,

    x_max               INTEGER,

    y_max               INTEGER,

    FOREIGN KEY(inspection_id)
        REFERENCES inspection(id)
        ON DELETE CASCADE,

    FOREIGN KEY(class_id)
        REFERENCES detection_class(id)
);

CREATE TABLE inspection_summary (

    id                  BIGSERIAL PRIMARY KEY,

    inspection_id       BIGINT NOT NULL,

    class_id            INTEGER NOT NULL,

    expected_quantity   INTEGER NOT NULL,

    detected_quantity   INTEGER NOT NULL,

    result              VARCHAR(20) NOT NULL,

    FOREIGN KEY(inspection_id)
        REFERENCES inspection(id)
        ON DELETE CASCADE,

    FOREIGN KEY(class_id)
        REFERENCES detection_class(id)
);

CREATE INDEX idx_standard_product
ON inspection_standard(product_id);

CREATE INDEX idx_standard_stage
ON inspection_standard(stage_id);

CREATE INDEX idx_detection_inspection
ON detection_result(inspection_id);

CREATE INDEX idx_summary_inspection
ON inspection_summary(inspection_id);

CREATE INDEX idx_inspection_status
ON inspection(status);

CREATE INDEX idx_inspection_date
ON inspection(inspected_at);