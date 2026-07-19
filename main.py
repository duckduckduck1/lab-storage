from dataclasses import dataclass


@dataclass
class Study:
    id: int
    name: str
    description: str


@dataclass
class Session:
    id: int
    study_id: int
    note: str
    uploader: str


@dataclass
class File:
    id: int
    session_id: int
    name: str
    size: int


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


print(study)
print(session)
print(file)
