from odoo import api,fields,models
from odoo.fields import Many2one


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = 'Hospital Appointment'
    _rec_names_search = ["refrence","patient_id"]
    _rec_name = "patient_id"

    refrence = fields.Char(string="Reference",default="New")
    patient_id=Many2one('hospital.patient',string="Patient",required=True,ondelete='restrict')
    # patient_id=Many2one('hospital.patient',string="Patient")
    date_appointment=fields.Date(string="Date")
    note=fields.Text(string="Note")
    state=fields.Selection([('draft',"Draft"),
                            ('confirm',"Confirmed"),
                            ('ongoing',"Ongoing"),
                            ('done',"Done"),
                            ('cancel',"Canceled")],default="draft",tracking=True)
    appointment_line_ids=fields.One2many("hospital.appointment.line","appointment_id",string="Line")
    total_qty=fields.Float(compute="_compute_total_qty",string="Total Qty", store=True)
    date_of_birth=fields.Date(related="patient_id.DOB",string="Date of Birth")
    reference_id=fields.Reference([("hospital.patient","patient"),("patient.tag","Symtoms"),("project.task","Task")])

    @api.model_create_multi
    def create(self, vals_list):
        print("odooMates",vals_list)
        for vals in vals_list:
            if 'refrence' not in vals: #refrence is not present in vals because refrence bydefault store "New" value
                vals['refrence'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)

    @api.depends("appointment_line_ids.qty")
    def _compute_total_qty(self):
        for rec in self:
            print(rec.appointment_line_ids)

            #case-1
            # total_qty=0
            # for line in rec.appointment_line_ids:
            #     total_qty+=line.qty
            #     print(line.qty)
            # rec.total_qty=total_qty

            #case-2
            # rec.total=sum(rec.appointment_line_ids.mapped('qty'))

            #case-3
            print(line.qty for line in rec.appointment_line_ids)
            rec.total_qty = sum(line.qty for line in rec.appointment_line_ids)


    def action_confirm(self):
        for rec in self:
            rec.state = "confirm"

    def action_ongoing(self):
        for rec in self:
            print("hii")
            rec.state = "ongoing"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"[{rec.refrence}]{rec.patient_id.name}"


class HospitalAppointmentLine(models.Model):
    _name = 'hospital.appointment.line'
    _description = "Hospital Appointment "

    product_id=fields.Many2one('product.product',string="Product",required=True)
    # product=fields.Char(string="Product")
    appointment_id=fields.Many2one("hospital.appointment",string="Appointment")
    qty=fields.Float(string="Quantity")



