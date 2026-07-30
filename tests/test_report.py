from pathlib import Path

from report import write_study_report
from generator import generate_study


def test_write_study_report(tmp_path: Path) -> None:
    study = generate_study(1, 2, 2, 42)

    path = tmp_path / "study-report.txt"

    write_study_report(study, path)

    assert path.exists()

    text = path.read_text(encoding="utf-8")

    assert "Study ID: 1, Name: Synthetic Study" in text

    assert "Session ID: 1" in text

    assert "File ID: 1" in text

    assert "Size:" in text

    assert text.count("Session ID:") == 2

    assert text.count("File ID:") == 4
