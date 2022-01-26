from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

# refrsh

class BookRentalModel(models.Model):
    _name = "enter.book_rental_model"
    _description = "Book Rental Model"

    date = fields.Date("Date", Required=True, default=datetime.now())

    book_id = fields.Many2one("enter.book_model", string = "Book", help = "Book reference.", required=True)
    user_id = fields.Many2one("enter.user_model", string = "User", help = "User reference.", required=True)