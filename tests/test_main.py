from main import find_session_by_id
from models import Session, Study


def test_find_session_by_id_returns_existing_session() -> None:
    study = Study(
        id=1,
        name="Исследование ФБМ при ЧМТ",
        description="4 группы: контроль, ФБМ 1 день, ФБМ 4 день, ФБМ 7 день",
    )

    expected_session = Session(
        id=1,
        study_id=study.id,
        note="Контроль ЭЭГ группа 1 Контроль",
        uploader="Sergey Popov",
    )

    study.sessions.append(expected_session)

    result = find_session_by_id(study, 1)

    assert result is expected_session


def test_find_session_by_id_returns_none_for_missing_id() -> None:
    study = Study(
        id=1,
        name="Исследование ФБМ при ЧМТ",
        description="4 группы: контроль, ФБМ 1 день, ФБМ 4 день, ФБМ 7 день",
    )

    result = find_session_by_id(study, 999)

    assert result is None
