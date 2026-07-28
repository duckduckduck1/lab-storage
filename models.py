from dataclasses import dataclass, field
from datetime import UTC, datetime


def utc_now() -> datetime:
    return datetime.now(UTC)


@dataclass
class Study:
    id: int
    name: str
    description: str
    sessions: list[Session] = field(default_factory=list)


@dataclass
class Session:
    id: int
    study_id: int
    note: str
    uploader: str
    created_at: datetime = field(default_factory=utc_now)
    files: list[File] = field(default_factory=list)


@dataclass
class File:
    id: int
    session_id: int
    name: str
    size: int
    created_at: datetime = field(default_factory=utc_now)
