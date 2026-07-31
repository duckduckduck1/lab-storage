INSERT INTO studies (name, description)
VALUES ('Synthetic Study', 'Synthetic laboratory study')
RETURNING id AS study_id
\gset

INSERT INTO sessions (study_id, note, uploader)
VALUES (:study_id, 'Synthetic control session 1', 'synthetic-user-1')
RETURNING id AS session_1_id
\gset

INSERT INTO sessions (study_id, note, uploader)
VALUES (:study_id, 'Synthetic control session 2', 'synthetic-user-2')
RETURNING id AS session_2_id
\gset

INSERT INTO files (session_id, name, size_bytes)
VALUES (:session_1_id, 'session-1-file-1.zip', 1024),
    (:session_1_id, 'session-1-file-2.7z', 2048),
    (:session_2_id, 'session-2-file-1.rar', 4096)
RETURNING id, session_id, name, size_bytes;

SELECT id, name, description, created_at
FROM studies
ORDER BY id;

SELECT id, study_id, note, uploader, created_at
FROM sessions
WHERE study_id = :study_id
ORDER BY id;

SELECT id, session_id, name, size_bytes, created_at
FROM files
WHERE session_id IN (:session_1_id, :session_2_id)
ORDER BY id;