-- Список активних сенсорів
SELECT *
FROM sensors
WHERE status = 'Активний';

-- Кількість інцидентів за статусом
SELECT status, COUNT(*) AS total
FROM incidents
GROUP BY status;

-- Інциденти та відповідальні оператори
SELECT 
    incidents.incident_id,
    incidents.severity,
    incidents.status,
    operators.name AS operator_name
FROM incidents
JOIN operators
ON incidents.operator_id = operators.operator_id;
