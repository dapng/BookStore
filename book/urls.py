from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('info', views.info, name='info'),
    path('home', views.book_home, name='home'),
    path('create', views.create, name='books-create'),
    path('sell', views.sell_home, name='sell-home'),
    path('sinfo', views.book_info, name='sale-info'),
    path('book/<int:pk>', views.BooksDetailView.as_view(), name='books-detail'),
    path('<int:pk>/update', views.BooksUpdateView.as_view(), name='books-update'),
    path('<int:pk>/delete', views.BooksDeleteView.as_view(), name='books-delete'),
    path('sale/<int:pk>', views.BooksSaleDetailView.as_view(), name='sale-detail'),
    path('<int:pk>/sell', views.BooksSaleUpdateView.as_view(), name='sale-update'),
]
