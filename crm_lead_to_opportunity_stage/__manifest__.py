# -*- coding: utf-8 -*-
###############################################################################
#
#   crm_lead_to_opportunity_stage
#   Custom Stage while converting lead to opportunity
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
    'name': "crm_lead_to_opportunity_stage",
    'summary': """
        default (lead to opportuity) Method creates opportunity in custom stage""",
    'description': """
        This module is to change the default stage of lead_to_opportunity conversion .Changing `new` to custom stage
        defined for each sales channel
    """,
    'author': "INSOFE Education Private Limited",
    'website': "https://www.insofe.edu.in",
    'license': 'LGPL-3',
    'category': 'Sales',
    'version': '1.1',
    'depends': ['base','crm'],
    # always loaded
    'data': ['views/views.xml'],    
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}