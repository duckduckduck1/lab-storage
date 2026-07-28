from models import Study, Session, File


def find_session_by_id(study: Study, session_id: int) -> Session | None:
    for s in study.sessions:
        if session_id == s.id:
            return s
    return None


def main() -> None:
    study = Study(
        id=1,
        name="Исследование ФБМ при ЧМТ",
        description="4 группы: контроль, ФБМ 1 день, ФБМ 4 день, ФБМ 7 день",
    )

    session = Session(
        id=1,
        study_id=study.id,
        note="Контроль ЭЭГ группа 1 Контроль",
        uploader="Sergey Popov",
    )

    file = File(
        id=1,
        session_id=session.id,
        name="Архив 10 мышей ЭЭГ Контроль.zip",
        size=1024,
    )

    session_2 = Session(
        id=2,
        study_id=study.id,
        note="Контроль ЭЭГ группа 2 Контроль",
        uploader="Sergey Popov",
    )

    study.sessions.append(session)
    study.sessions.append(session_2)
    session.files.append(file)

    for i, s in enumerate(study.sessions):
        print(
            f"ID:[{i}] Session ID: {s.id}, Note: {s.note}, Uploader: {s.uploader}, created_at: {s.created_at}"
        )
        for j, f in enumerate(s.files):
            print(
                f"\tID:[{j}] File ID: {f.id}, session_id: {f.session_id}, Name: {f.name}, Size: {f.size}, created_at: {f.created_at}"
            )

    print(find_session_by_id(study, 2))
    print(find_session_by_id(study, 999))


if __name__ == "__main__":
    main()
