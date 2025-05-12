from django.urls import path
from .views import remcreateview, remlist

urlpatterns = [
    path('create/',remcreateview.as_view(), name='reminder-create'),
    path('list/', remlist.as_view(), name='reminder-list'),
]
