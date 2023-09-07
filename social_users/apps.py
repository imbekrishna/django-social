from django.apps import AppConfig


class SocialUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'social_users'

    def ready(self) -> None:
        import social_users.signals