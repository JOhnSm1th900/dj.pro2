from django.shortcuts import render
from django.contrib.auth.views import LogoutView

class LogoutViewWithGet(LogoutView):

    http_method_names = LogoutView.http_method_names + ['get']

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
