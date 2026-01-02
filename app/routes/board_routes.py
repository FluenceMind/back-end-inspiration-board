from flask import Blueprint, request, Response
from app.models.board import Board
from .routes_utilities import validate_model, create_model
from ..db import db

bp = Blueprint("boards", __name__, url_prefix="/boards")

# GET /boards
@bp.get("")
def get_all_boards():
    boards = db.session.scalars(db.select(Board).order_by(Board.id))
    return [board.to_dict() for board in boards], 200

#GET /one board by id
@bp.get("/<int:board_id>")
def get_one_board(board_id):
    board = validate_model(Board, board_id)
    return board.to_dict(), 200

#POST /boards
@bp.post("")
def create_board():
    request_body = request.get_json()
    return create_model(Board, request_body)

#DELETE /boards/<board_id>
@bp.delete("/<int:board_id>")
def delete_board(board_id):
    board = validate_model(Board, board_id)

    db.session.delete(board)
    db.session.commit()

    return Response(status=204, mimetype="application/json")