from random import Random

from models import Study, Session, File


def generate_study(
    study_id: int, session_count: int, files_per_session: int, seed: int
) -> Study:

    if study_id < 1:
        raise ValueError("study_id must be greater than 0")

    if session_count < 0:
        raise ValueError("session_count must be greater than or equal to 0")

    if files_per_session < 0:
        raise ValueError("files_per_session must be greater than or equal to 0")

    rng = Random(seed)

    synthetic_study = Study(
        id=study_id,
        name="Synthetic Study",
        description="Synthetic laboratory study",
    )

    session_kinds = [
        "control",
        "calibration",
        "recording",
    ]

    uploaders = [
        "synthetic-user-1",
        "synthetic-user-2",
        "synthetic-user-3",
    ]

    file_kinds = [
        "eeg",
        "tracking",
        "metadata",
    ]

    for i in range(session_count):
        session = Session(
            study_id=synthetic_study.id,
            id=i + 1,
            note=f"Synthetic {rng.choice(session_kinds)} session {i + 1}",
            uploader=rng.choice(uploaders),
        )
        for j in range(files_per_session):
            file_id = i * files_per_session + j + 1
            file = File(
                session_id=session.id,
                id=file_id,
                name=f"session-{session.id}-file-{file_id}.{rng.choice(file_kinds)}",
                size=rng.randint(1024, 1024 * 1024),
            )
            session.files.append(file)
        synthetic_study.sessions.append(session)

    return synthetic_study
