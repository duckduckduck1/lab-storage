from generator import generate_study


def test_generate_study_creates_expected_tree() -> None:
    study = generate_study(1, 2, 3, seed=42)

    assert study.id == 1

    assert len(study.sessions) == 2

    for s in study.sessions:
        assert len(s.files) == 3

    assert study.sessions[1].files[2].id == 6

    assert study.sessions[1].files[2].session_id == study.sessions[1].id

    assert study.sessions[1].note.startswith("Synthetic ")


def test_generate_study_is_peproducible_by_seed() -> None:
    first = generate_study(1, 2, 2, seed=42)
    second = generate_study(1, 2, 2, seed=42)
    different = generate_study(1, 2, 2, seed=43)

    sample_first = (
        first.sessions[0].note,
        first.sessions[0].uploader,
        first.sessions[0].files[0].name,
        first.sessions[0].files[0].size,
        first.sessions[1].note,
        first.sessions[1].files[1].size,
    )

    sample_second = (
        second.sessions[0].note,
        second.sessions[0].uploader,
        second.sessions[0].files[0].name,
        second.sessions[0].files[0].size,
        second.sessions[1].note,
        second.sessions[1].files[1].size,
    )

    sample_different = (
        different.sessions[0].note,
        different.sessions[0].uploader,
        different.sessions[0].files[0].name,
        different.sessions[0].files[0].size,
        different.sessions[1].note,
        different.sessions[1].files[1].size,
    )

    assert sample_first == sample_second

    assert sample_first != sample_different
