from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

# refrsh

class GameRentalModel(models.Model):
    _name = "enter.game_rental_model"
    _description = "Game Rental Model"

    date = fields.Date("Date", Required=True, default=datetime.now())

    game_id = fields.Many2one("enter.game_model", string = "Game", help = "Game reference.")
    user_id = fields.Many2one("enter.user_model", string = "User", help = "User reference.")