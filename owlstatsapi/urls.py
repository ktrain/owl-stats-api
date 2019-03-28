from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from owlstatsapi.api import views

v1Router = routers.DefaultRouter(trailing_slash=False)
v1Router.register(r'users', views.UserViewSet)
v1Router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('v1/', include(v1Router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
