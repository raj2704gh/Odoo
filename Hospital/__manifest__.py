{
    'name': 'Hospital Managment System',
    "author": "ME",
    "license": "LGPL-3",
    "version": "17.0.1.1",
    "depends": ['mail','product',"account",'project'],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/appointment_views.xml",
        "views/patient_views.xml",
        "views/patient_readonly_views.xml",
        "views/patient_tag_views.xml",
        "views/appointment_line_views.xml",
        "views/account_move_views.xml",
        "views/project_task_views.xml",
        "views/menu.xml", 
        "data/sequence.xml"
        
    ]

}
