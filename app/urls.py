from django.urls import path

from .views import PictureListView, PictureDetailView

app_name = 'farzicom'

urlpatterns = [
    path("cat/", PictureListView.asview(), name="Blog"),
    path('cat/<int:pk>/', PictureDetailView.asview(), name="Blog Detail"),
]
