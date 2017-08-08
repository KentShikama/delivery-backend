from django.conf.urls import url, include

from delivery.api.views import ApiVersionCheck, CategoriesList, StoresList, SchoolsList, OrderCreator

urlpatterns = [
    url(r'version/(?P<app_id>[0-9]+)/?$', ApiVersionCheck.as_view(), name="version"),
    url(r'categories/?$', CategoriesList.as_view(), name="categories"),
    url(r'stores/?$', StoresList.as_view(), name="stores"),
    url(r'schools/?$', SchoolsList.as_view(), name="schools"),
    url(r'order/?$', OrderCreator.as_view(), name="new_order")
]