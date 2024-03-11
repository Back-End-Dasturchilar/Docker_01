from django.urls import path
from .views import TagList, TagDetail, CategoryList, CategoryDetail, PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('tags/', TagList.as_view(), name='tag'),
    path('tags/<int:pk>/', TagDetail.as_view(), name='tag-detail'),
    path('category/', CategoryList.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category-detail')
]
