from django.contrib import admin
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from .views import AuthorEdit, AuthorList, BookEdit, FriendList, FriendUpdate, FriendEdit, \
    BookDetailView, RegisterView, CreateUserProfile


app_name = 'p_library'
urlpatterns = [
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('book/create', BookEdit.as_view(), name='book_create'),
    path('friends', FriendList.as_view(), name='friend_list'),
    path('<pk>/friend_update', FriendUpdate.as_view(), name='friend_update'),
    path('friend/create', FriendEdit.as_view(), name='friend_create'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(
        template_name='register.html',
        success_url=reverse_lazy('p_library:profile-create')
    ), name='register'),
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
]
