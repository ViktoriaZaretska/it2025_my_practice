-- Таблиця операторів
CREATE TABLE operators (
    operator_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT,
    availability TEXT
);

-- Таблиця сенсорів
CREATE TABLE sensors (
    sensor_id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    location TEXT,
    status TEXT,
    operator_id INTEGER,
    FOREIGN KEY (operator_id) REFERENCES operators(operator_id)
);

-- Таблиця інцидентів
CREATE TABLE incidents (
    incident_id INTEGER PRIMARY KEY,
    timestamp TEXT,
    severity TEXT,
    status TEXT,
    sensor_id INTEGER,
    operator_id INTEGER,
    FOREIGN KEY (sensor_id) REFERENCES sensors(sensor_id),
    FOREIGN KEY (operator_id) REFERENCES operators(operator_id)
);

-- Таблиця ресурсів
CREATE TABLE resources (
    resource_id INTEGER PRIMARY KEY,
    type TEXT,
    location TEXT,
    status TEXT,
    incident_id INTEGER,
    FOREIGN KEY (incident_id) REFERENCES incidents(incident_id)
);
