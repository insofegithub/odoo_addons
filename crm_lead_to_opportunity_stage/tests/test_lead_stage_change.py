#from odoo.tests import common
from odoo.tests.common import TransactionCase


class TestLeadStageChange(TransactionCase):

    def test_lead_stage_change(self):
        # I create a new lead
        lead = self.env['crm.lead'].create({
            'type': "lead",
            'name': "Test lead new1",
            'partner_id': self.env.ref("base.res_partner_1").id,
            'description': "This is the description of the test new lead1.",
            'team_id': self.env.ref("sales_team.team_sales_department").id
        })

        stage_id = lead._stage_find(domain=[('probability', '=', 70.00)])

        # Assign proposition stage to team
        self.env.ref("sales_team.team_sales_department").in_stage_deafult_id = stage_id.id

        # Change type from lead to opportunity
        lead.convert_opportunity(self.env.ref("base.res_partner_2").id)

        self.assertEqual(stage_id, lead.stage_id, "Stage of opportunity is incorrect!")
