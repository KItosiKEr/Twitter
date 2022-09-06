from email.policy import default
from .views import PostView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('api/post', PostView)

urlpatterns = router.urls