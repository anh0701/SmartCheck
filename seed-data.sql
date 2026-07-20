INSERT INTO inspection_stage(code, name)
VALUES
('PRE_PROCESS', 'Pre-process Inspection'),
('POST_PROCESS', 'Post-process Inspection');

INSERT INTO product(code, name, description)
VALUES
(
'LAPTOP_A',
'Laptop Model A',
'15 inch Office Laptop'
),
(
'DESKTOP_B',
'Desktop Model B',
'Office Desktop Computer'
);

INSERT INTO detection_class(name)
VALUES
    ('PCB'),
    ('CPU'),
    ('RAM'),
    ('SSD'),
    ('Battery'),
    ('Fan'),
    ('Laptop'),
    ('Monitor'),
    ('Keyboard'),
    ('Mouse');

INSERT INTO inspection_standard
    (product_id, stage_id, class_id, required_quantity)
VALUES
    -- PCB
    (1,1,1,1),
    -- CPU
    (1,1,2,1),
    -- RAM
    (1,1,3,2),
    -- SSD
    (1,1,4,1),
    -- Battery
    (1,1,5,1),
    -- Fan
    (1,1,6,1);

INSERT INTO inspection_standard
    (product_id, stage_id, class_id, required_quantity)
VALUES
    (1,2,7,1),
    (1,2,8,1),
    (1,2,9,1),
    (1,2,10,1);

INSERT INTO inspection_standard
    (product_id, stage_id, class_id, required_quantity)
VALUES
    (2,1,1,1),
    (2,1,2,1),
    (2,1,3,2),
    (2,1,4,1),
    (2,1,6,2);

INSERT INTO inspection_standard
    (product_id, stage_id, class_id, required_quantity)
VALUES
    (2,2,8,1),
    (2,2,9,1),
    (2,2,10,1);

INSERT INTO inspection
(
    product_id,
    stage_id,
    image_path,
    processing_time_ms
)
VALUES
(
    1,
    1,
    'images/pre001.jpg',
    42
);

INSERT INTO detection_result
(
    inspection_id,
    class_id,
    confidence,
    x_min,
    y_min,
    x_max,
    y_max
)
VALUES
    (1,1,0.98,10,20,80,90),
    (1,2,0.99,90,25,160,95),
    (1,3,0.97,170,40,220,90),
    (1,3,0.96,240,40,290,90),
    (1,4,0.99,310,40,390,100),
    (1,5,0.98,410,30,470,100),
    (1,6,0.96,490,40,560,100);

INSERT INTO inspection_summary
(
    inspection_id,
    class_id,
    expected_quantity,
    detected_quantity,
    result
)
VALUES
    (1,1,1,1,'PASS'),
    (1,2,1,1,'PASS'),
    (1,3,2,2,'PASS'),
    (1,4,1,1,'PASS'),
    (1,5,1,1,'PASS'),
    (1,6,1,1,'PASS');

INSERT INTO inspection
(
    product_id,
    stage_id,
    image_path,
    processing_time_ms
)
VALUES
(
    1,
    1,
    'images/pre002.jpg',
    37
);

INSERT INTO detection_result
(
    inspection_id,
    class_id,
    confidence,
    x_min,
    y_min,
    x_max,
    y_max
)
VALUES
    (2,1,0.98,10,20,80,90),
    (2,2,0.98,90,25,160,95),
    (2,3,0.96,170,40,220,90),
    -- chỉ detect được 1 RAM
    (2,4,0.97,300,30,380,90),
    (2,6,0.96,420,40,500,90);

INSERT INTO inspection_summary
(
    inspection_id,
    class_id,
    expected_quantity,
    detected_quantity,
    result
)
VALUES
    (2,1,1,1,'PASS'),
    (2,2,1,1,'PASS'),
    (2,3,2,1,'FAIL'),
    (2,4,1,1,'PASS'),
    (2,5,1,0,'FAIL'),
    (2,6,1,1,'PASS');
