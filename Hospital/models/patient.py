from odoo import api, fields,models,_
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit=['mail.thread']
    _description = 'Patient Master'
    

    name=fields.Char(string="Name",tracking=True,copy=False,required=True,default="Mukesh")
    DOB=fields.Date(string="DOB")
    gender=fields.Selection([("male","male"),("female","female")],string="Gender")
    tag_ids = fields.Many2many('patient.tag', 'patient_tag_rel', 'patient_id', 'tag_id', string="Tag")
    is_minor=fields.Boolean(string="Minor")
    guardian=fields.Char(String="Gardian")
    weight=fields.Float(string="weight")
    Total_amount=fields.Monetary("Total amount")
    currency_id=fields.Many2one("res.currency")
    active=fields.Boolean(string="Activate",default=True)
    # def unlink(self):
    #     for rec in self:
    #         domain=[("patient_id","=",rec.id)] #structure=[("field", "operator", value)]
    #         appointment=self.env["hospital.appointment"].search(domain)
    #         if appointment:
    #             raise ValidationError(f"You can not  delete patient now {rec.name}")
    #
    # #     return super().unlink()
    # @api.model_create_multi
    # def create(self,vals):
    #     return super().create(vals)

    # def write(self,vals):
    #     return super().write(vals)

    # @api.returns('self',lambda value:value.id)
    # def copy(self,default={'name':"raj"}): 
    #     print("new",default)   
    #     return super().copy(default)

    # def unlink(self):
    #     print(self)
    #     for reco in self:
    #         print("Total",reco.Total_amount)
    #         if reco.Total_amount>1000:
    #             raise UserError(f"you not delet this recors{reco.name}")
    #     return super().unlink()    
        
    # @api.model
    # def name_create(self,name):
    #     default_email=15
    #     new_record=self.create({
    #         "name":name,
    #         "Total_amount":default_email
    #     })

    #     print(new_record)
    #     return new_record.id,new_record.display_name

    @api.model
    def default_get(self,list=[]):
        print("hjlkjjkjkkkkkkkkk",list)
        rtn=super().default_get(list)
        print(rtn)
        rtn["weight"]=25
        return rtn


    @api.ondelete(at_uninstall=False)
    def _check_patient_appointment(self):
        for rec in self:
            domain=[("patient_id","=",rec.id)]
            appointment = self.env["hospital.appointment"].search(domain)
            if appointment:
                raise ValidationError(f"you can not delete")