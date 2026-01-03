from flask import Blueprint, request, Response
from app.models.board import Board
from .routes_utilities import get_models_with_filters, validate_model, create_model
from ..db import db

bp = Blueprint("boards", __name__, url_prefix="/boards")

# GET /boards
@bp.get("")
def get_all_boards():
    filters = request.args
    return get_models_with_filters(Board, filters)

#GET /one board by id
@bp.get("/<int:board_id>")
def get_one_board(board_id):
    board = validate_model(Board, board_id)
    return board.to_dict(), 200

#GET /boards/<board_id>/cards
@bp.get("/<int:board_id>/cards")
def get_cards_for_board(board_id):
    board = validate_model(Board, board_id)
    cards = [card.to_dict() for card in board.cards]
    return {"cards": cards}, 200


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