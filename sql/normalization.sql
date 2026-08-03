CREATE TEMP TABLE denormalized_sessions (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    note text NOT NULL,
    uploader_username text NOT NULL,
    uploader_role text NOT NULL
);

INSERT INTO denormalized_sessions (note, uploader_username, uploader_role)
VALUES ('Session A', 'Synthetic-user', 'researcher');

INSERT INTO denormalized_sessions (note, uploader_username, uploader_role)
VALUES ('Session B', 'Synthetic-user', 'researcher');

UPDATE denormalized_sessions
SET uploader_role = 'admin'
WHERE id = 1;

SELECT *
FROM denormalized_sessions
ORDER BY id;

CREATE TEMP TABLE normalized_users (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username text NOT NULL UNIQUE,
    role text NOT NULL
);

CREATE TEMP TABLE normalized_sessions (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    note text NOT NULL,
    uploader_id bigint NOT NULL REFERENCES normalized_users (id)
);

INSERT INTO normalized_users (username, role)
VALUES ('Synthetic-user', 'researcher')
RETURNING id AS uploader_id
\gset

INSERT INTO normalized_sessions (note, uploader_id)
VALUES ('Session A', :uploader_id);

INSERT INTO normalized_sessions (note, uploader_id)
VALUES ('Session B', :uploader_id);

UPDATE normalized_users
SET role = 'admin'
WHERE id = :uploader_id;

SELECT ns.note, nu.username, nu.role
FROM normalized_users AS nu
JOIN normalized_sessions as ns
ON nu.id = ns.uploader_id
ORDER BY ns.id;