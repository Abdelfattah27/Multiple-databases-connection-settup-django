class ExistingDBRouter:
    def db_for_read(self, model, **hints):
        print(model._meta.app_label)
        if model._meta.app_label == 'helloketty': 
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'helloketty':  
            return 'default'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'helloketty':  
            return False 
        return None
   
   
 
class DjangoDBRouter:
    
    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}

    def db_for_read(self, model, **hints):
        print(model._meta.app_label)
        if model._meta.app_label in self.route_app_labels:
            return 'django_system'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'django_system'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):        
        if app_label in self.route_app_labels:
            return db == 'django_system'
        return None