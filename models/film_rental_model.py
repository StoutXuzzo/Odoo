from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

# refrsh

class FilmRentalModel(models.Model):
    _name = "enter.film_rental_model"
    _description = "Film Rental Model"

    date = fields.Date("Date", Required=True, default=datetime.now())

    film_id = fields.Many2one("enter.film_model", string = "Film", help = "Film reference.", required=True)
    user_id = fields.Many2one("enter.user_model", string = "User", help = "User reference.", required=True)