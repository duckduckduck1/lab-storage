from generator import generate_study


def test_generate_study_creates_expected_tree() -> None:
    study = generate_study(1, 2, 3)

    assert study.id == 1

    assert len(study.sessions) == 2

    for s in study.sessions:
        assert len(s.files) == 3

    assert study.sessions[1].files[2].id == 6

    assert study.sessions[1].files[2].session_id == study.sessions[1].id

    assert study.sessions[1].note == "Synthetic session 2"
