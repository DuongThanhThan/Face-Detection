
from django.urls import path, include
from . import views
<<<<<<< HEAD:Face/urls.py
from .views import CUD_User, User

urlpatterns = [
    path('create/', CUD_User.as_view({'post': 'create'}), name='create'),
    path('update/', CUD_User.as_view({'patch': 'update'}), name='update'),
    path('delete/', CUD_User.as_view({'delete': 'delete'}), name='delete'),
    path('get/', User.as_view({'get': 'get'}), name='get'),
=======
from .views import CGUD_User

urlpatterns = [
    path('create/', CGUD_User.as_view({'post': 'create'}), name='create'),
    path('update/', CGUD_User.as_view({'patch': 'update'}), name='update'),
    path('delete/', CGUD_User.as_view({'delete': 'delete'}), name='delete'),
    path('get_user/', CGUD_User.as_view({'get': 'get_user'}, name='get_user'))
>>>>>>> 2257d60 (image upload):apps/Face/urls.py
]
