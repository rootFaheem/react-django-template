from django.conf.urls import url

from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    url('', ArticleListView.as_view()),
    url('<pk>', ArticleDetailView.as_view())
]
