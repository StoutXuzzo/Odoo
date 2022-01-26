from email.policy import default
from odoo import models, fields, api
from odoo.exceptions import ValidationError

# refrsh

class FilmModel(models.Model):
    _name = "enter.film_model"
    _description = "Film Model"

    name = fields.Char("Title", default="HoseFilm", required=True)
    genre = fields.Char("Genre", default="action", required=True)

    producer = fields.Char("Producer", default="HoseProductions", required=True)
    
    rental_ids = fields.One2many("enter.film_rental_model", "film_id", string = "Rentals")