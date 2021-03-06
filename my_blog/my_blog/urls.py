"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.decorators.cache import cache_page
import xadmin
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from blog.views import (
    PostDetailView,
    IndexView,
    CategoryView,
    TagView,
    SearchView,
    AuthorView,
)
from config.views import LinkListView
from comment.views import CommentView
from .autocomplete import CategoryAutocomplete, TagAutocomplete
from blog.apis import PostViewSet, CategoryViewSet, TagViewSet

urlpatterns = [
    # url(r"^$", cache_page(60*20)(IndexView.as_view()), name="index"),#缓存页面
    url(r"^$", IndexView.as_view(), name="index"),
    url(
        r"^category/(?P<category_id>\d+)/$",
        CategoryView.as_view(),
        name="category-list",
    ),
    url(r"^tag/(?P<tag_id>\d+)/$", TagView.as_view(), name="tag-list"),
    url(r"^post/(?P<post_id>\d+).html$", PostDetailView.as_view(), name="post-detail"),
    url(r"^search/$", SearchView.as_view(), name="search"),
    url(r"^author/(?P<owner_id>\d+)/$", AuthorView.as_view(), name="author"),
    url(r"^links/$", LinkListView.as_view(), name="links"),
    url(r"^comment/$", CommentView.as_view(), name="comment"),
]

# 后台管理系统
urlpatterns += [
                   url(r"^admin/", admin.site.urls),
                   url(r"xadmin/", include(xadmin.site.urls)),

                   # 自动补全
                   url(
                       r"^category-autocomplete/$",
                       CategoryAutocomplete.as_view(),
                       name="category-autocomplete",
                   ),
                   url(r"^tag-autocomplete/$", TagAutocomplete.as_view(), name="tag-autocomplete"),

                   # 文本编辑器
                   url(r"^ckeditor/", include("ckeditor_uploader.urls")),
                   # 静态资源访问
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 性能分析toolbar和silk
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^silk/', include('silk.urls', namespace='silk')),
    ]

# restful api
router = DefaultRouter()
router.register(r"post", PostViewSet, base_name="api-post")
router.register(r"category", CategoryViewSet, base_name="api-category")
router.register(r"tag", TagViewSet, base_name="api-tag")
urlpatterns += [
    url(r"^api/docs/", include_docs_urls(title="shiqinying's blog apis")),
    url(r"^api/", include(router.urls)),
]

# allauth

urlpatterns += [url(r'^accounts/', include('allauth.urls')), ]
