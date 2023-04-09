from rest_framework.routers import DefaultRouter
from .staff_user_api import OrderViewSet

router = DefaultRouter()
router.register("staff_api", OrderViewSet)

urlpatterns = router.urls
