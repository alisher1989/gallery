from django.urls import path
from webapp.views import IndexView, PhotoDetailView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView, login_view, logout_view
app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', login_view, name='login'),
    path('logout/', login_view, name='logout'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/create/', PhotoCreateView.as_view(), name='create_photo'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='update_photo'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete_photo'),
]