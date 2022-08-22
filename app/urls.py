from django.urls import path

from .views import PictureListView, PictureDetailView, reordering_cats

app_name = 'farzicom'

urlpatterns = [
    path("cat", PictureListView.as_view(), name="Blog"),
    path('cat/<int:pk>/', PictureDetailView.as_view(), name="Blog Detail"),
    path('re-order-position', reordering_cats, name="Reordering cats"),
]
