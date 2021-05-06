from django.contrib.admin import AdminSite


class AlmaLinuxAdminSite(AdminSite):
    site_title = 'AlmaLinux'
    site_header = 'AlmaLinux'

    def get_urls(self):
        return super().get_urls()
