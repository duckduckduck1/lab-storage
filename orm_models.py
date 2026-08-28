from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Identity, Text, func, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class StudyORM(Base):
    __tablename__ = "studies"

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True), primary_key=True)
    name: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.current_timestamp(),
    )
    sessions: Mapped[list["SessionORM"]] = relationship(back_populates="study")


class SessionORM(Base):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True), primary_key=True)
    study_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("studies.id"))
    note: Mapped[str] = mapped_column(Text)
    uploader: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.current_timestamp(),
    )

    study: Mapped["StudyORM"] = relationship(back_populates="sessions")
    files: Mapped[list["FileORM"]] = relationship(back_populates="session")


class FileORM(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(always=True),
        primary_key=True,
    )
    session_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("sessions.id"),
    )
    name: Mapped[str] = mapped_column(Text)
    size_bytes: Mapped[int] = mapped_column(BigInteger)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.current_timestamp()
    )

    session: Mapped["SessionORM"] = relationship(back_populates="files")
