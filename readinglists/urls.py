from django.urls import path
from .views import ReadinglistList, ReadinglistDetail


urlpatterns = [
    path('', ReadinglistList.as_view()),  # don't need the `name='wishlist_list'`
    path('<int:pk>/', ReadinglistDetail.as_view()),
]
