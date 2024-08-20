from odoo import fields, models, api
from odoo.exceptions import ValidationError


class CustomerRecords(models.Model):
    _name = "customer.records"  # Defines the model name for customer records
    _description = "customer_records"  # Provides a description for the model

    name = fields.Char(string="Name", required=True)
    # Defines a Char field for the customer's name and makes it mandatory (required=True)

    notes = fields.One2many("customer.notes", "customer_id", string="Notes") # Defines a One2many field that creates a relationship between this model and the customer.notes model
    # This relationship links multiple notes to a single customer

    # Constraint to Validate the 'name' Field
    @api.constrains('name')  # Ensures validation is applied whenever the 'name' field is modified
    def _check_customer_name(self):
        for record in self:
            if not record.name:
                # Validation error if 'name' is empty or null
                raise ValidationError("The customer name cannot be null or empty.")
