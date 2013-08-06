from flask.ext.login import current_user
from flask.ext.superadmin import Admin, AdminIndexView, expose

from ek import app, db
from models import User, Role, Category, Thing, Object


class AdminIndexView(AdminIndexView):

    def is_accessible(self):
        return current_user.is_authenticated()

    @expose('/')
    def index(self):
        objects = Object.query.all()
        return self.render('admin/index.html', objects=objects)

admin = Admin(app, app.config['NAME'], index_view=AdminIndexView())

admin.register(User, session=db.session)
admin.register(Role, session=db.session)
admin.register(Category, session=db.session)
admin.register(Thing, session=db.session)
admin.register(Object, session=db.session)
