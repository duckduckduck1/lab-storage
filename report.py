from pathlib import Path

from models import Study


def write_study_report(study: Study, output_path: Path) -> None:
    with output_path.open("w", encoding="utf-8") as report:
        report.write(f"Study ID: {study.id}, Name: {study.name}\n")
        for s in study.sessions:
            report.write(f"  Session ID: {s.id}, Note: {s.note}\n")
            for f in s.files:
                report.write(f"    File ID: {f.id}, Name: {f.name}, Size: {f.size}\n")
