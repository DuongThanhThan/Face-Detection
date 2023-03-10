
from django.urls import path, include
from . import views
from .views import CGUD_User

urlpatterns = [
    path('create/', CGUD_User.as_view({'post': 'create'}), name='create'),
    path('update/', CGUD_User.as_view({'patch': 'update'}), name='update'),
    path('delete/', CGUD_User.as_view({'delete': 'delete'}), name='delete'),
    path('get_user/', CGUD_User.as_view({'get': 'get_user'}, name='get_user'))
]
