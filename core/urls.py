from django.contrib import admin
from django.urls import path
from app.views import create_new_book_view, get_books_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('createbook/', view = create_new_book_view),
    path('getbook/', view = get_books_view)
]
