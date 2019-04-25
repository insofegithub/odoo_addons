# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrmTeam(models.Model):
    _name = "crm.team"
    _inherit = ['crm.team']

    member_ids = fields.Many2many('res.users', 'crm_team_res_users_rel', 'crm_team_id', 'res_users_id', string='Channel Members')

class Users(models.Model):
    _name = "res.users"
    _inherit = ['res.users']

    team_ids = fields.Many2many('crm.team', 'crm_team_res_users_rel', 'res_users_id', 'crm_team_id', string='Sales Channels')
