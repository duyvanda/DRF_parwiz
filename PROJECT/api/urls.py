from django.urls import path, include
from .views import article_detail, ArticleList, ArticleListMixin,ArticleListGEN, ArticleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    # path('article/', article_list),'
    path('viewset/', include(router.urls)),
    path('article/', ArticleList.as_view()),
    path('mixin/article/', ArticleListMixin.as_view()),
    path('gen/article/', ArticleListGEN.as_view()),
    path('detail/<int:pk>/', article_detail),
]