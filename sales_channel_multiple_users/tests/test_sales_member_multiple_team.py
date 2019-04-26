from odoo.tests.common import TransactionCase


class TestSalesMemberMultipleTeam(TransactionCase):

    def test_sales_member_multiple_team(self):
        user1 = self.env['res.users'].create({
            'name': 'test user1',
            'login': 'test1',
            'groups_id': [4, self.ref('base.group_user')],
        })
        user2 = self.env['res.users'].create({
            'name': 'test user2',
            'login': 'test2',
            'groups_id': [4, self.ref('base.group_user')],
        })
        team1 = self.env['crm.team'].sudo(self.crm_salemanager.id).create({'name': "Phone Marketing",'member_ids':[user1,user2]})
        team2 = self.env['crm.team'].sudo(self.crm_salemanager.id).create({'name': "Email Marketing",'member_ids':[user1]})