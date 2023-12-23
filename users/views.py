from django.contrib.auth.views import LogoutView


class LogoutView(LogoutView):
     def get_redirect_url(self):
        return '/'
