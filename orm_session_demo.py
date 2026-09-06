from sqlalchemy.orm import Session

from database import engine
from orm_models import StudyORM


def main() -> None:
    with Session(engine) as session, session.begin():
        commited_study = StudyORM(
            name="Синтетическое исследование",
            description="Учебный пример с авто COMMIT",
        )
        session.add(commited_study)
        session.flush()
        commited_id = commited_study.id

    with Session(engine) as session:
        loaded_study = session.get(StudyORM, commited_id)

        assert loaded_study is not None
        print(f"{loaded_study.id} {loaded_study.name}")

    with Session(engine) as session:
        rolled_back_study = StudyORM(
            name="Синетическое исследование 2",
            description="Учебный пример с Rollback",
        )
        session.add(rolled_back_study)
        session.flush()
        rolled_back_id = rolled_back_study.id
        session.rollback()

    with Session(engine) as session:
        rolled_back_result = session.get(StudyORM, rolled_back_id)

        assert rolled_back_result is None

    with Session(engine) as session, session.begin():
        saved_study = session.get(StudyORM, commited_id)

        assert saved_study is not None
        session.delete(saved_study)


if __name__ == "__main__":
    main()
