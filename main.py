from dataclasses import dataclass


@dataclass
class Study:
    id: int
    name: str
    description: str


study = Study(
    id="Единица",
    name="Исследование ФБМ при ЧМТ",
    description="4 группы: контроль, ФБМ 1 день, ФБМ 4 день, ФБМ 7 день",
)

print(study)
