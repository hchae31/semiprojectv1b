from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey
from datetime import datetime
from app.model.base import Base

class Board(Base):
    __tablename__ = 'board'

    bno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(index=True)
    userid: Mapped[str] = mapped_column(ForeignKey('member.userid'), index=True)
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)
    views: Mapped[int] = mapped_column(default=0)
    contents: Mapped[str]