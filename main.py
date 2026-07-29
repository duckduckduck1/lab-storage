from generator import generate_study
from models import Study, Session


def find_session_by_id(study: Study, session_id: int) -> Session | None:
    for s in study.sessions:
        if session_id == s.id:
            return s
    return None


def main() -> None:

    study = generate_study(1, 2, 2)

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
