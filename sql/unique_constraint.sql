\set VERBOSITY verbose

CREATE TEMP TABLE synthetic_users (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username text NOT NULL UNIQUE
);

INSERT INTO synthetic_users (username)
VALUES ('synthetic-user');

\set ON_ERROR_STOP off

INSERT INTO synthetic_users (username)
VALUES ('synthetic-user');

\set ON_ERROR_STOP on

INSERT INTO synthetic_users (username)
VALUES ('synthetic-user-2');

SELECT id, username
FROM synthetic_users
ORDER BY id;
