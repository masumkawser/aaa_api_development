# -*- coding: utf-8 -*-
from odoo import http


class AaaApiDevelop(http.Controller):
    @http.route('/aaa/api/develop', auth='public',website=False, csrf=False, type='json', methods=['GET','POST'])
    def index(self, **kw):

        contacts = http.request.env['res.partner'].sudo().search([])
        contact_list =[]
        for contact in contacts:
            contact_list.append({
                'name': contact.name,
                'email': contact.email,
                'contact': contact.phone,
        })
        return contact_list

class AaaApiDevelop1(http.Controller):
    @http.route('/aaa/api/develop1', auth='public',website=False, csrf=False, type='json', methods=['GET','POST'])
    def index(self, **kw):

        contacts = http.request.env['crm.lead'].sudo().search([])
        contact_list =[]
        for contact in contacts:
            contact_list.append({
                'name': contact.partner_id,
                'email': contact.email_from,
                'contact': contact.phone,
        })
        return contact_list

class AaaApiDevelop11(http.Controller):
    @http.route('/aaa/api/develop11', auth='public',website=False, csrf=False, type='json', methods=['GET','POST'])
    def index(self, **kw):

        contacts = http.request.env['crm.lead'].sudo().search([])
        contact_list =[]
        for contact in contacts:
            contact_list.append({
                'name': contact.partner_name,
                'email': contact.email_from,
                'contact': contact.phone,
        })
        return contact_list