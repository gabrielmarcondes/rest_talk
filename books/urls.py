from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from books import views

router = DefaultRouter()
router.register('books', views.BookViewset)

urlpatterns = [
    url(r'', include(router.urls)),
]
