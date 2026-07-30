import pytest

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


def test_generate_study_is_reproducible_by_seed() -> None:
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


def test_generate_study_rejects_invalid_study_id() -> None:
    with pytest.raises(ValueError, match="study_id"):
        generate_study(0, 1, 1, seed=42)


def test_generate_study_rejects_invalid_session_count() -> None:
    with pytest.raises(ValueError, match="session_count"):
        generate_study(1, -1, 1, seed=42)


def test_generate_study_rejects_invalid_files_per_session() -> None:
    with pytest.raises(ValueError, match="files_per_session"):
        generate_study(1, 1, -1, seed=42)


def test_generate_study_allows_zero_sessions() -> None:
    study = generate_study(1, 0, 1, 42)

    assert study.sessions == []


def test_generate_study_allows_zero_files() -> None:
    study = generate_study(1, 1, 0, 42)

    assert len(study.sessions) == 1

    assert study.sessions[0].files == []


def test_generate_study_creates_unique_ids() -> None:
    study = generate_study(1, 4, 3, 42)

    session_ids = [s.id for s in study.sessions]

    file_ids = [f.id for s in study.sessions for f in s.files]

    assert len(session_ids) == 4

    assert len(file_ids) == 12

    assert len(session_ids) == len(set(session_ids))

    assert len(file_ids) == len(set(file_ids))
