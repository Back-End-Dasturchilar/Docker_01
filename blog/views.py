from rest_framework import generics
from .serializers import TagSerializer, CategorySerializer, PostSerializer
from .models import Tag, Category, Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        cat = self.request.query_params.get('cat')
        q = self.request.query_params.get('q')
        if tag is not None:
            return Post.objects.filter(tags__title=tag)
        if cat is not None:
            return Post.objects.filter(category__title=cat)
        if q is not None:
            return Post.objects.filter(title__icontains=q)
        return Post.objects.all()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
