# -*- coding: utf-8 -*-
###############################################################################
#
#   Module for OpenERP
#   Copyright (C) 2014 Akretion (http://www.akretion.com).
#   Copyright (C) 2010-2013 Akretion LDTA (<http://www.akretion.com>)
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
#   @author Benoît GUILLOT <benoit.guillot@akretion.com>
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


from openerp.osv import fields, orm


class project_project(orm.Model):
    _inherit = "project.project"

    _columns = {
        'order_ids': fields.one2many(
            'sale.order',
            'related_project_id',
            'Orders'),
    }
