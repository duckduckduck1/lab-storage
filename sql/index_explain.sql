CREATE TEMP TABLE file_search_demo (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    session_id bigint NOT NULL,
    name text NOT NULL,
    size_bytes bigint NOT NULL CHECK (size_bytes >= 0)
);

INSERT INTO file_search_demo (session_id, name, size_bytes)
SELECT (n % 100) + 1, 'file-' || n || '.bin', n * 1024
FROM generate_series(1, 50000) AS generated(n);

SELECT id, session_id, name, size_bytes
FROM file_search_demo
ORDER BY id
LIMIT 5;

-- Прогноз: file_count = 50000, session_count = 100, min_session_id = 1, max_session_id = 100
SELECT 
    count(*) AS file_count,
    count(DISTINCT session_id) AS session_count,
    min(session_id) AS min_session_id,
    max(session_id) AS max_session_id
FROM file_search_demo;

analyze file_search_demo;

explain (analyze, buffers)
select id, session_id, name, size_bytes
from file_search_demo
where session_id = 42;

create index file_search_demo_session_id_idx
ON file_search_demo (session_id);
-- прогноз Ожидаю Bitmap-план, вернется 500 строк, не ожидаю увидеть Rows Removed by Filter: 49500
explain (analyze, buffers)
select id, session_id, name, size_bytes
from file_search_demo
where session_id = 42;

-- Прогноз: Способ чтения Seq Scan, кол-во строк 50000,
explain (analyze, buffers)
select id, session_id, name, size_bytes
from file_search_demo
where session_id >= 1;