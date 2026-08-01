\pset null ['NULL']

BEGIN;

INSERT INTO sessions (study_id, note, uploader)
VALUES ((SELECT id FROM studies ORDER BY id LIMIT 1),
        'Synthetic empty session',
        'synthetic-user-empty'
)
RETURNING id AS empty_session_id

\gset

SELECT
    s.id AS session_id,
    s.note AS session_note,
    f.id AS file_id,
    f.name AS file_name
FROM sessions as s
INNER JOIN files as f
ON s.id = f.session_id
WHERE s.id = :empty_session_id;

SELECT
    s.id AS session_id,
    s.note AS session_note,
    f.id AS file_id,
    f.name AS file_name
FROM sessions as s
LEFT JOIN files as f
ON s.id = f.session_id
WHERE s.id = :empty_session_id;

SELECT
    s.id AS session_id,
    s.note AS session_note,
    count(*) AS joined_row_count,
    count(f.id) AS file_count
FROM sessions AS s
LEFT JOIN files AS f
ON s.id = f.session_id
GROUP BY s.id, s.note
ORDER BY s.id;

SELECT
    s.id AS session_id,
    s.note AS session_note,
    count(*) AS joined_row_count,
    count(f.id) AS file_count
FROM sessions AS s
LEFT JOIN files AS f
ON s.id = f.session_id
GROUP BY s.id, s.note
HAVING count(f.id) >= 2
ORDER BY s.id;

ROLLBACK;

SELECT count(*) AS remaining_empty_sessions
FROM sessions
WHERE id = :empty_session_id;
