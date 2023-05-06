from rest_framework.routers import DefaultRouter
from authentication.staff_user_api import UserLoginViewSet

router = DefaultRouter()
router.register("staff_api", UserLoginViewSet, basename="")

urlpatterns = router.urls
