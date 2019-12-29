from rest_framework import routers
from .views import DiaryViewSet

router = routers.DefaultRouter()
router.register(r'diaries', DiaryViewSet)
