from django.conf.urls import url, include

from cartpool.api.views import ApiVersionCheck, CategoriesList

urlpatterns = [
    url(r'version/(?P<app_id>[0-9]+)/?$', ApiVersionCheck.as_view(), name="version"),
    url(r'categories/?$', CategoriesList.as_view(), name="categories"),
]