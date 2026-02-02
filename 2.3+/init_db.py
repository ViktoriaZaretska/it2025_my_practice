import sqlite3

DB_NAME = "ias.db"

schema_sql = """
CREATE TABLE IF NOT EXISTS operators (
    operator_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT,
    availability TEXT
);

CREATE TABLE IF NOT EXISTS sensors (
    sensor_id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    location TEXT,
    status TEXT,
    operator_id INTEGER,
    FOREIGN KEY (operator_id) REFERENCES operators(operator_id)
);

CREATE TABLE IF NOT EXISTS incidents (
    incident_id INTEGER PRIMARY KEY,
    timestamp TEXT,
    severity TEXT,
    status TEXT,
    sensor_id INTEGER,
    operator_id INTEGER,
    FOREIGN KEY (sensor_id) REFERENCES sensors(sensor_id),
    FOREIGN KEY (operator_id) REFERENCES operators(operator_id)
);

CREATE TABLE IF NOT EXISTS resources (
    resource_id INTEGER PRIMARY KEY,
    type TEXT,
    location TEXT,
    status TEXT,
    incident_id INTEGER,
    FOREIGN KEY (incident_id) REFERENCES incidents(incident_id)
);
"""

data_sql = """
INSERT INTO operators VALUES
(1, 'Оператор_А', 'Адміністратор', 'Доступний'),
(2, 'Оператор_Б', 'Аналітик', 'Зайнятий'),
(3, 'Оператор_В', 'Черговий', 'Доступний'),
(4, 'Оператор_Г', 'Інженер', 'Доступний'),
(5, 'Оператор_Д', 'Аналітик', 'Зайнятий');

INSERT INTO sensors VALUES
(1, 'Тип_1', 'Зона_А', 'Активний', 1),
(2, 'Тип_2', 'Зона_Б', 'Активний', 1),
(3, 'Тип_1', 'Зона_В', 'Неактивний', 2),
(4, 'Тип_3', 'Зона_Г', 'Активний', 3),
(5, 'Тип_2', 'Зона_Д', 'Активний', 4);

INSERT INTO incidents VALUES
(1, '2026-01-10 10:00', 'Високий', 'Новий', 1, 1),
(2, '2026-01-10 11:30', 'Середній', 'В обробці', 2, 1),
(3, '2026-01-11 09:15', 'Низький', 'Закритий', 3, 2),
(4, '2026-01-11 14:20', 'Високий', 'В обробці', 4, 3),
(5, '2026-01-12 08:45', 'Середній', 'Новий', 5, 4);

INSERT INTO resources VALUES
(1, 'Екіпаж', 'База_1', 'Задіяний', 1),
(2, 'Обладнання', 'Склад_А', 'Вільний', NULL),
(3, 'Екіпаж', 'База_2', 'Задіяний', 2),
(4, 'Обладнання', 'Склад_Б', 'Задіяний', 4),
(5, 'Екіпаж', 'База_3', 'Вільний', NULL);
"""

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
cursor.executescript(schema_sql)
cursor.executescript(data_sql)
conn.commit()
conn.close()

print("[OK] База даних створена та заповнена")
