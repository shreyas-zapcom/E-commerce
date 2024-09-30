from django.urls import path, include
from shop.views import RegisterView
from shop.views import LogoutView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from shop.views import CategoryViewSet, ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),  
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),  
    path('logout/', LogoutView.as_view(), name='logout'),
]