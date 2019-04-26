# -*- coding: utf-8 -*-
###############################################################################
#
#   sales_channel_multiple_users
#   This module allows to assign a user to multiple sale channels
#   Copyright (C) 2019 INSOFE Education Private Limited  (https://www.insofe.edu.in). All Rights Reserved
#   @author B Geetha Reddy <geetha.badvel@insofe.edu.in>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': "sales_channel_multiple_users",
    'summary': """
        A odoo user can be assigned to multiple sales channels""",
    'description': """
        By default, odoo allows to assign a user to single sales channel. This module allows to assign a user to 
        multiple sale channels 
    """,
    'author': "INSOFE Education Private Limited",
    'website': "https://www.insofe.edu.in",
    'category': 'Sales',
    'version': '1.1',
    # any module necessary for this one to work correctly
    'depends': ['base','crm'],
    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
