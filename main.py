from dataclasses import dataclass, field


@dataclass
class File:
    id: int
    session_id: int
    name: str
    size: int


@dataclass
class Session:
    id: int
    study_id: int
    note: str
    uploader: str
    files: list[File] = field(default_factory=list)


@dataclass
class Study:
    id: int
    name: str
    description: str
    sessions: list[Session] = field(default_factory=list)


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
    id=1, session_id=session.id, name="Архив 10 мышей ЭЭГ Контроль.zip", size=1024
)

session.files = [file]
study.sessions = [session]

print(study)
