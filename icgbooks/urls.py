from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .shelves.views import ShelfViewSet
from .users.views import UserViewSet, UserCreateViewSet
from .books.views import BookViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)
router.register(r'books', BookViewSet)
router.register(r'shelves', ShelfViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
    path('auth/', include('rest_framework_social_oauth2.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
