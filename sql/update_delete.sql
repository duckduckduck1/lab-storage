SELECT id AS target_session_id
FROM sessions
ORDER BY id
LIMIT 1
\gset

BEGIN;

UPDATE sessions
SET note = 'test-change'
WHERE id = :target_session_id
RETURNING id, note;

SELECT id, note
FROM sessions
WHERE id = :target_session_id;

ROLLBACK;

SELECT id, note
FROM sessions
WHERE id = :target_session_id;

\set VERBOSITY verbose

BEGIN;
\set ON_ERROR_STOP off

DELETE FROM sessions
WHERE id = :target_session_id
RETURNING id;

\set ON_ERROR_STOP on
ROLLBACK;

BEGIN;

DELETE FROM files
WHERE session_id= :target_session_id
RETURNING id, session_id, name;

DELETE FROM sessions
WHERE id = :target_session_id
RETURNING id, note;

SELECT count(*)
FROM sessions
WHERE id = :target_session_id;

SELECT count(*)
FROM files
WHERE session_id = :target_session_id;

ROLLBACK;

SELECT count(*)
FROM sessions
WHERE id = :target_session_id;

SELECT count(*)
FROM files
WHERE session_id = :target_session_id;
