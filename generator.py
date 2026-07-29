from models import Study, Session, File


def generate_study(study_id: int, session_count: int, files_per_session: int) -> Study:
    synthetic_study = Study(
        id=study_id,
        name="Synthetic Study",
        description="Synthetic laboratory study",
    )

    for i in range(session_count):
        session = Session(
            study_id=synthetic_study.id,
            id=i + 1,
            note=f"Synthetic session {i + 1}",
            uploader="synthetic-user",
        )
        for j in range(files_per_session):
            file_id = i * files_per_session + j + 1
            file = File(
                session_id=session.id,
                id=file_id,
                name=f"session-{session.id}-file-{file_id}.bin",
                size=file_id * 1024,
            )
            session.files.append(file)
        synthetic_study.sessions.append(session)

    return synthetic_study
