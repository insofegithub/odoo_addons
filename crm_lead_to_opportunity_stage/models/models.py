# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _
from odoo import SUPERUSER_ID

import logging
_logger = logging.getLogger(__name__)

class Team(models.Model):
    _name = 'crm.team'
    _inherit = ['crm.team']

    in_stage_default_id = fields.Many2one('crm.stage', string='Default Stage')

class Lead(models.Model):
    _name = "crm.lead"
    _inherit = ['crm.lead']
    @api.multi
    def _convert_opportunity_data(self, customer, team_id=False):
        """ Extract the data from a lead to create the opportunity
            :param customer : res.partner record
            :param team_id : identifier of the sales channel to determine the stage
        """
        if not team_id:
            team_id = self.team_id.id if self.team_id else False
        value = {
            'planned_revenue': self.planned_revenue,
            'probability': self.probability,
            'name': self.name,
            'partner_id': customer.id if customer else False,
            'type': 'opportunity',
            'date_open': fields.Datetime.now(),
            'email_from': customer and customer.email or self.email_from,
            'phone': customer and customer.phone or self.phone,
            'date_conversion': fields.Datetime.now(),
        }

        if self.team_id:
            stage = self.team_id.in_stage_default_id#self.env['crm.stage'].browse(self.team_id.in_stage_default_id)
            if stage:
                value['stage_id'] = stage.id
                value['probability'] = stage.probability
            else:
                if not self.stage_id:
                    stage = self._stage_find(team_id=team_id)
                    value['stage_id'] = stage.id
                    if stage:
                        value['probability'] = stage.probability

        else:
            if not self.stage_id:
                stage = self._stage_find(team_id=team_id)
                value['stage_id'] = stage.id
                if stage:
                    value['probability'] = stage.id.probability

        return value