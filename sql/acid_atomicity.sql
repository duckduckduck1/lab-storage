\set VERBOSITY verbose

CREATE TEMP TABLE acid_sessions (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    note text NOT NULL
);

CREATE TEMP TABLE acid_files (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    session_id bigint NOT NULL REFERENCES acid_sessions (id),
    size_bytes bigint NOT NULL CHECK (size_bytes >= 0)
);

BEGIN;

INSERT INTO acid_sessions (note)
VALUES ('Failed upload.')
RETURNING id AS failed_session_id
\gset

\set ON_ERROR_STOP off

INSERT INTO acid_files (session_id, size_bytes)
VALUES (:failed_session_id, -1);

SELECT count(*)
FROM acid_sessions;

\set ON_ERROR_STOP on

ROLLBACK;

SELECT count(id)
FROM acid_sessions
WHERE id = :failed_session_id;


BEGIN;

INSERT INTO acid_sessions (note)
VALUES ('Successful upload')
RETURNING id AS successful_upload_id
\gset

INSERT INTO acid_files (session_id, size_bytes)
VALUES (:successful_upload_id, 1024);

COMMIT;

SELECT acid_s.id, acid_f.session_id
FROM acid_sessions AS acid_s
JOIN acid_files AS acid_f
ON acid_s.id = acid_f.session_id;



