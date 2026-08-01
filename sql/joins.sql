SELECT st.name AS study_name,
        s.note AS session_note,
        s.uploader AS session_uploader,
        f.id AS file_id,
        f.name AS file_name,
        f.size_bytes AS file_size_bytes

FROM studies AS st

JOIN sessions AS s

ON st.id = s.study_id

JOIN files AS f

ON s.id = f.session_id

ORDER BY s.id, f.id;