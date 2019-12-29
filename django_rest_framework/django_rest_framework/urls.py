from django.conf.urls import url, include
from django.contrib import admin
from diary.urls import router as diary_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(diary_router.urls)),
]
