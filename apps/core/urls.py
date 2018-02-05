from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken import views as rest_framework_views

from .views import AddressViewSet

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
]