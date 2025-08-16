from django.urls import path
from .import views
from .views import CsrfExemptTokenView
from .views import get_user_todos


urlpatterns = [
    path('toDoListView', views.toDoListView, name='toDoListView'),
    path('token/', CsrfExemptTokenView.as_view(), name='token_obtain_pair'),
    path('todos/', get_user_todos),
]