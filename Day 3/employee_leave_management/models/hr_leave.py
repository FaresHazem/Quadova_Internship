from odoo import fields, models


class HRLeave(models.Model):
    _name = "hr.leave"
    _description = "HR Leave"

    # Field Definitions
    employee_id = fields.Char(string="Employee ID", required=True)
    leave_type = fields.Char(string="Leave Type", required=True)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    reason = fields.Char(string="Reason", required=True)
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("submitted", "Submitted"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        default="draft",
    )