from odoo import models, fields, api
from odoo.exceptions import ValidationError

# refrsh

class BookModel(models.Model):
    _name = "enter.book_model"
    _description = "Book Model"

    name = fields.Char("Title", default="HoseBook", required=True)
    genre = fields.Char("Genre", default="romance", required=True)

    author = fields.Char("Author", required=True, default="Pedro")
    
    rental_ids = fields.One2many("enter.book_rental_model", "book_id", string = "Rentals")