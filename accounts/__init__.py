from django.apps import AppConfig

class AccountsAppConfig(AppConfig):
    name = 'conduit.apps.accounts'
    label = 'accounts'
    verbose_name = 'Accounts'

    def ready(self):
        from . import signals

# This is how we register our custom app config with Django. Django is smart
# enough to look for the `default_app_config` property of each registered app
# and use the correct app config based on that value.
default_app_config = 'hangrs.apps.accounts.AccountsAppConfig'