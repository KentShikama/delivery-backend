from django.conf import settings
from rest_framework.views import APIView

class ApiVersionCheck(APIView):
    def get(self, request, app_id):
        if app_id == settings.LATEST_CLIENT_VERSION:
            return True
        else:
            return False


