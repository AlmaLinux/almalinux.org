from django.contrib.admin.apps import AdminConfig


class AlmaLinuxAdminConfig(AdminConfig):
    default_site = 'almalinux.admin.AlmaLinuxAdminSite'
