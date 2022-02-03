from odoo import models, fields, api
from odoo.exceptions import ValidationError

# refrsh

class GameModel(models.Model):
    _name = "enter.game_model"
    _description = "Game Model"

    name = fields.Char("Title", default="HoseCraft", required=True)
    genre = fields.Selection(string="Genre", selection=[("S", "Survival"), ("P", "Puzzle"), ("F", "FPS")], default="F")
    
    min_age = fields.Integer("Min Age", required = True, default=16)
    
    rental_ids = fields.One2many("enter.game_rental_model", "game_id", string = "Rentals")