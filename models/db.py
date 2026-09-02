from os import getenv
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import create_engine, MetaData, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class NamelessBase(DeclarativeBase):
    metadata = MetaData(schema="public")
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        # Set a low set order to set id column first. -2 for id, -1 for name (imediately after)
        sort_order=-2,
    )
    updated_at: Mapped[str] = mapped_column(
        String,
        default=lambda: datetime.now().isoformat(),
        nullable=False,
        # Set a high sort order to set date column last
        sort_order=19,
    )
    created_at: Mapped[str] = mapped_column(
        String,
        default=lambda: datetime.now().isoformat(),
        nullable=False,
        # Set a high sort order to set date column last
        sort_order=20,
    )

    def __init__(self):
        super().__init__()

    def to_dict(self):
        return {
            "id": self.id,
            "updated_at": self.updated_at,
            "created_at": self.created_at,
        }


class Base(NamelessBase):
    # Prevent SQLAlchemy trying to map this class
    __abstract__ = True

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        # Set a low set order to set name column second. -2 for id, -1 for name (imediately after)
        sort_order=-1,
    )

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def to_dict(self):
        return {
            **super().to_dict(),
            "name": self.name,
        }

    pass


db_engine = create_engine(getenv("DB_URL") or "", echo=True)

metadata = MetaData()

db = SQLAlchemy(model_class=NamelessBase)
