\set VERBOSITY verbose
\set ON_ERROR_STOP on

BEGIN;
\set ON_ERROR_STOP off

INSERT INTO studies (name, description)
VALUES (NULL, 'test');

\set ON_ERROR_STOP on
ROLLBACK;

BEGIN;
\set ON_ERROR_STOP off

INSERT INTO sessions (study_id, note, uploader)
VALUES (-1, 'test', 'test');

\set ON_ERROR_STOP on
ROLLBACK;

BEGIN;
\set ON_ERROR_STOP off

INSERT INTO files (session_id, name, size_bytes)
VALUES (-1, 'test', 1);

\set ON_ERROR_STOP on
ROLLBACK;

BEGIN;
\set ON_ERROR_STOP off

INSERT INTO files (session_id, name, size_bytes)
VALUES  ((SELECT id FROM sessions ORDER BY id LIMIT 1),
        'test', -1);

\set ON_ERROR_STOP on
ROLLBACK;