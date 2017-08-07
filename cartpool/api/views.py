from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from cartpool.api.models import Category


class ApiVersionCheck(APIView):
    def get(self, request, app_id):
        if int(app_id) == settings.LATEST_CLIENT_VERSION:
            return Response({"status": "updated"})
        elif int(app_id) >= settings.LATEST_CLIENT_VERSION:
            return Response({"status": "future"})
        else:
            return Response({"status": "out of date"})


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CategoriesList(APIView):
    """
    List of all categories
    """
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

#class Ordering(APIView):
