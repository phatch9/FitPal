from fitness import app, db
from flask_admin import Admin
from fitness.database import Plan
from flask_admin.contrib.sqla import ModelView

create_plan = Admin (app=app, name="Create your workout plan", template_mode='bootstrap4')

create_plan.add_view(ModelView(Plan, db.session))

