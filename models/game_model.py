from odoo import models, fields, api
from odoo.exceptions import ValidationError

# refrsh

class GameModel(models.Model):
    _name = "enter.game_model"
    _description = "Game Model"

    title = fields.Char("Title", default="HoseCraft", required=True)
    genres = fields.Char("Genre", default="FPS", required=True)
    
    min_age = fields.Integer("Min Age", required = True, default=16)
    
    rental_ids = fields.One2many("enter.game_rental_model", "game_id", string = "Rentals")