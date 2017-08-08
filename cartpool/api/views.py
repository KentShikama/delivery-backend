from django.conf import settings
from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from cartpool.api.models import Category, Store, School


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
    List of all categories with option to filter by school TODO: Change
    """

    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        return [
            row[0]
            for row in cursor.fetchall()
        ]

    def fetch_category_ids(self, school_id):
        with connection.cursor() as cursor:
            cursor.execute("""
              SELECT api_category.id FROM api_category, api_store, api_school, api_store_schools, api_store_category 
              WHERE api_school.id = %s AND
              api_store_schools.school_id = api_school.id AND
              api_store_schools.store_id = api_store.id AND
              api_store_category.store_id = api_store.id AND
              api_store_category.category_id = api_category.id
              GROUP BY api_category.id;
            """, [school_id])
            return self.dictfetchall(cursor)

    def get(self, request, format=None):
        query = request.query_params.get('school') or ''
        if query:
            school = School.objects.get(id=query)
            category_ids = self.fetch_category_ids(school.id)
            categories = Category.objects.filter(pk__in=category_ids).all()
        else:
            categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"

class StoresList(APIView):
    """
    List of all stores
    """
    def get(self, request, format=None):
        query = request.query_params.get('category') or ''
        if query:
            stores = Store.objects.filter(category__in=query)
        else:
            stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"

class SchoolsList(APIView):
    """
    List of all schools
    """

    def get(self, request, format=None):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

#class Ordering(APIView):
