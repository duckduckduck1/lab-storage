CREATE TEMP TABLE cascade_studies(
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name text NOT NULL
);

CREATE TEMP TABLE cascade_sessions (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    study_id bigint NOT NULL REFERENCES cascade_studies (id) ON DELETE CASCADE,
    name text NOT NULL
);

CREATE TEMP TABLE cascade_files (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    session_id bigint NOT NULL REFERENCES cascade_sessions (id) ON DELETE CASCADE,
    name text NOT NULL
);

INSERT INTO cascade_studies (name)
VALUES ('Synthetic-cascade-study-1')
RETURNING id AS study_id
\gset

INSERT INTO cascade_sessions (study_id, name)
VALUES (:study_id, 'Synthetic-cascade-session-1')
RETURNING id AS session_1_id
\gset

INSERT INTO cascade_sessions (study_id, name)
VALUES (:study_id, 'Synthetic-cascade-session-2')
RETURNING id AS session_2_id
\gset

INSERT INTO cascade_files (session_id, name)
VALUES (:session_1_id, 'Synthetic-cascade-session-1-file-cascade-1.zip'),
        (:session_1_id, 'Synthetic-cascade-session-1-file-cascade-2.zip'),
        (:session_2_id, 'Synthetic-cascade-session-2-file-cascade-1.zip');

SELECT count(*) AS study_count
FROM cascade_studies;

SELECT count(*) AS session_count
FROM cascade_sessions;

SELECT count(*) AS file_count
FROM cascade_files;

BEGIN;

DELETE FROM cascade_studies
WHERE id = :study_id;

SELECT count(*) AS study_count
FROM cascade_studies;

SELECT count(*) AS session_count
FROM cascade_sessions;

SELECT count(*) AS file_count
FROM cascade_files;

ROLLBACK;

SELECT count(*) AS study_count
FROM cascade_studies;

SELECT count(*) AS session_count
FROM cascade_sessions;

SELECT count(*) AS file_count
FROM cascade_files;