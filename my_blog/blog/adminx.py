from django.urls import reverse
from django.utils.html import format_html

import xadmin
from xadmin.layout import Row, Fieldset
from xadmin.filters import manager
from xadmin.filters import RelatedFieldListFilter

from my_blog.base_adminx import BaseOwnerAdmin
from .models import Post, Category, Tag
from .adminforms import PostAdminForm


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ("name", "status", "is_nav", "created_time", "post_count")
    fields = ("name", "status", "is_nav")

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = "文章数量"


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ("name", "status", "created_time")
    fields = ("name", "status")


class CategoryOwnerFilter(RelatedFieldListFilter):

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        # 重新获取lookup_choices，根据owner过滤
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')


manager.register(CategoryOwnerFilter, take_priority=True)


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    """自定义form"""

    form = PostAdminForm
    list_display = ["title", "category", "status", "created_time", "operator"]
    list_display_links = []

    list_filter = ["category", "tag"]
    search_fields = ["title", "category__name"]
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    exclude = ("owner",)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>', reverse("xadmin:blog_post_change", args=(obj.id,))
        )

    operator.short_description = "操作"

