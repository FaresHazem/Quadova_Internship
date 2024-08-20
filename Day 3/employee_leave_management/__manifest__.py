{
    "name": "employee_leave_management",
    "version": "17.0.0.0.0",
    "license": "OEEL-1",
    "depends": ["base", "hr"],
    "application": True,
    "data": [
        # SECURITY
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        # VIEWS
        "views/hr_leave_views.xml",
        # MENUS
        "views/hr_leave_menu.xml",
    ],
}
