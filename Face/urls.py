
from django.urls import path, include
from . import views
from .views import CUD_User, User

urlpatterns = [
    path('create/', CUD_User.as_view({'post': 'create'}), name='create'),
    path('update/', CUD_User.as_view({'patch': 'update'}), name='update'),
    path('delete/', CUD_User.as_view({'delete': 'delete'}), name='delete'),
    path('get/', User.as_view({'get': 'get'}), name='get'),
]
