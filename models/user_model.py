from odoo import models, fields, api
from odoo.exceptions import ValidationError

# refrsh

class UserModel(models.Model):
    _name = "enter.user_model"
    _description = "User Model"

    name = fields.Char("Name", default="Juan", required=True)
    surname = fields.Char("Surname", required=True)
    username = fields.Char("Username", required=True, default="Juan123")

    age = fields.Integer("Age")
    
