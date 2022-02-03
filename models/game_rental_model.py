from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

# refrsh

class GameRentalModel(models.Model):
    _name = "enter.game_rental_model"
    _description = "Game Rental Model"

    name = fields.Char("Name", compute="_compute_name", store=True)
    date = fields.Date("Date", Required=True, default=datetime.now())

    game_id = fields.Many2one("enter.game_model", string = "Game", help = "Game reference.", required=True)
    user_id = fields.Many2one("enter.user_model", string = "User", help = "User reference.", required=True)

    find_genre = fields.Selection(string="Genre", selection=[("S", "Survival"), ("P", "Puzzle"), ("F", "FPS")], store=False)

    @api.onchange('find_genre')
    def onchange_genre(self):
        self.game_id = None
        if self.find_genre:
            domain = {'game_id': [('genre', '=', self.find_genre)]}
        else:
            domain = {'game_id': [('genre', '!=', '*ihg')]}

        return {'domain': domain}

    @api.constrains("user_id")
    def _check_age(self):
        if self.user_id.age < self.game_id.min_age:
            raise ValidationError("The user '" + self.user_id.username + "' is too young")
        return True

    @api.depends("game_id", "user_id")
    def _compute_name(self):
        for rec  in self:
            rec.name = rec.user_id.name + "-" + rec.game_id.name