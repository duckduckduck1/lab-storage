from sqlalchemy import DateTime, BigInteger, Text, CheckConstraint
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

    assert isinstance(id_column.type, BigInteger)
    assert isinstance(name_column.type, Text)
    assert isinstance(description_column.type, Text)


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


def test_session_orm_matches_sql_schema() -> None:
    session_table = SessionORM.metadata.tables["sessions"]

    study_id_column = session_table.columns["study_id"]

    foreign_keys = list(study_id_column.foreign_keys)

    assert session_table.name == "sessions"

    assert set(session_table.columns.keys()) == {
        "id",
        "study_id",
        "note",
        "uploader",
        "created_at",
    }

    assert isinstance(session_table.columns["id"].type, BigInteger)
    assert isinstance(session_table.columns["study_id"].type, BigInteger)
    assert isinstance(session_table.columns["note"].type, Text)
    assert isinstance(session_table.columns["uploader"].type, Text)
    assert isinstance(session_table.columns["created_at"].type, DateTime)

    assert session_table.columns["id"].primary_key is True

    assert session_table.columns["id"].identity is not None
    assert session_table.columns["id"].identity.always is True

    assert session_table.columns["id"].nullable is False
    assert session_table.columns["study_id"].nullable is False
    assert session_table.columns["note"].nullable is False
    assert session_table.columns["uploader"].nullable is False
    assert session_table.columns["created_at"].nullable is False

    assert session_table.columns["created_at"].type.timezone is True
    assert session_table.columns["created_at"].server_default is not None

    assert len(foreign_keys) == 1
    assert foreign_keys[0].target_fullname == "studies.id"


def test_file_orm_matches_sql_schema() -> None:
    file_table = FileORM.metadata.tables["files"]

    session_id_column = file_table.columns["session_id"]

    foreign_keys = list(
        session_id_column.foreign_keys,
    )

    check_constraints = [
        constraint
        for constraint in file_table.constraints
        if isinstance(constraint, CheckConstraint)
    ]

    assert file_table.name == "files"

    assert set(file_table.columns.keys()) == {
        "id",
        "session_id",
        "name",
        "size_bytes",
        "created_at",
    }

    assert file_table.columns["id"].primary_key is True

    assert file_table.columns["id"].identity is not None
    assert file_table.columns["id"].identity.always is True

    assert isinstance(file_table.columns["id"].type, BigInteger)
    assert isinstance(file_table.columns["session_id"].type, BigInteger)
    assert isinstance(file_table.columns["name"].type, Text)
    assert isinstance(file_table.columns["size_bytes"].type, BigInteger)
    assert isinstance(file_table.columns["created_at"].type, DateTime)

    assert file_table.columns["id"].nullable is False
    assert file_table.columns["session_id"].nullable is False
    assert file_table.columns["name"].nullable is False
    assert file_table.columns["size_bytes"].nullable is False
    assert file_table.columns["created_at"].nullable is False

    assert file_table.columns["created_at"].type.timezone is True
    assert file_table.columns["created_at"].server_default is not None

    assert len(foreign_keys) == 1
    assert foreign_keys[0].target_fullname == "sessions.id"

    assert len(check_constraints) == 1
    assert str(check_constraints[0].sqltext) == "size_bytes >= 0"
