from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.board import Board
from ..db import db
from sqlalchemy import ForeignKey
from typing import Optional

class Card(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]
    likes_count: Mapped[int] = mapped_column(default=0)
    board_id: Mapped[int]=mapped_column(ForeignKey("board.id"))
    board: Mapped["Board"] = relationship(back_populates="cards")

    def to_dict(self):
        result = {
            "id": self.id,
            "message": self.message,
            "likes_count": self.likes_count,
            "board_id": self.board_id,
        }
        return result
        
    @classmethod
    def from_dict(cls, card_data):
        return cls(
        message=card_data["message"],
        board_id=card_data["board_id"]
    )


