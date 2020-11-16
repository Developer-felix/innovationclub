from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'User'
    def ready(self):
        import User.signals
