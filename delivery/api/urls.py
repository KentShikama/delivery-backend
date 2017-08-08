from django.conf.urls import url, include

from delivery.api.views import ApiVersionCheck, CategoriesList, StoresList, SchoolsList

urlpatterns = [
    url(r'version/(?P<app_id>[0-9]+)/?$', ApiVersionCheck.as_view(), name="version"),
    url(r'categories/?$', CategoriesList.as_view(), name="categories"),
    url(r'stores/?$', StoresList.as_view(), name="stores"),
    url(r'schools/?$', SchoolsList.as_view(), name="schools"),
]