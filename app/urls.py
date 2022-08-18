from django.urls import path

from .views import PictureListView, PictureDetailView

app_name = 'farzicom'

urlpatterns = [
    path("cat", PictureListView.as_view(), name="Blog"),
    path('cat/<int:pk>/', PictureDetailView.as_view(), name="Blog Detail"),
]
