from flask import Blueprint, request, Response
from app.models.card import Card         
from .routes_utilities import validate_model, create_model
from ..db import db

bp = Blueprint("cards", __name__, url_prefix="/cards")

@bp.get("/<int:card_id>")
def get_one_card(card_id):
    card = validate_model(Card, card_id)
    return card.to_dict(), 200

@bp.post("")
def create_card():
    request_body = request.get_json()
    return create_model(Card, request_body)

@bp.patch("/<int:card_id>/like")
def like_card(card_id):
    card = validate_model(Card, card_id)
    card.likes_count += 1
    db.session.commit()
    return card.to_dict(), 200

@bp.delete("/<int:card_id>")
def delete_card(card_id):
    card = validate_model(Card, card_id)
    db.session.delete(card)
    db.session.commit()
    return Response(status=204, mimetype="application/json")
