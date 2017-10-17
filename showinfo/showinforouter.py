"""
    A router to control all database operations on models in the blog application.
"""
class ShowinfoRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'showinfo':
            return 'showinfodb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'showinfo':
            return 'showinfodb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'showinfo' or obj2._meta.app_label == 'showinfo':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'showinfo':
            return db == 'showinfodb'
        return None
