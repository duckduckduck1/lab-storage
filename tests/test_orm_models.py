from sqlalchemy import DateTime
from orm_models import StudyORM, SessionORM, FileORM


def test_study_orm_matches_sql_schema() -> None:
    table = StudyORM.metadata.tables["studies"]

    id_column = table.columns["id"]
    name_column = table.columns["name"]
    description_column = table.columns["description"]
    created_at_column = table.columns["created_at"]

    assert table.name == "studies"

    assert set(table.columns.keys()) == {
        "name",
        "description",
        "created_at",
        "id",
    }

    assert id_column.primary_key is True
    assert id_column.nullable is False

    identity = id_column.identity

    assert identity is not None
    assert identity.always is True

    assert name_column.nullable is False
    assert description_column.nullable is False

    assert created_at_column.nullable is False
    assert isinstance(created_at_column.type, DateTime)
    assert created_at_column.type.timezone is True
    assert created_at_column.server_default is not None


def test_orm_relationships_are_bidirectional() -> None:
    study = StudyORM(
        name="Синтетическое исследование",
        description="Тест ORM-связи",
    )
    session = SessionORM(
        note="Синтетическая сессия",
        uploader="Test User",
    )

    file = FileORM(
        name="Synthetic.zip",
        size_bytes=1024,
    )

    study.sessions.append(session)

    session.files.append(file)

    assert session.study is study

    assert file.session is session
