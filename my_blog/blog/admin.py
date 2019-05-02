from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from my_blog.base_admin import BaseOwnerAdmin
from .models import Post, Category, Tag
from .adminforms import PostAdminForm



# class PostInline(admin.TabularInline):
#     fields = ('title','desc')
#     extra = 1
#     model = Post


@admin.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    # inlines = [PostInline]  #在同一页面编辑关联数据
    list_display = ('name', 'status', 'is_nav', 'created_time','post_count')
    fields = ('name', 'status', 'is_nav')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super().save_model(request,obj,form,change)

    def post_count(self,obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'


@admin.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status','created_time')
    fields = ('name', 'status')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(TagAdmin, self).save_model(request,obj,form,change)


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器：只展示当前用户分类"""
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset


@admin.register(Post)
class PostAdmin(BaseOwnerAdmin):
    """自定义form"""
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'created_time','operator',
    ]
    list_display_links = []

    list_filter = [CategoryOwnerFilter, 'tag']
    search_fields = ['title', 'category__name']
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    exclude = ('owner',)

    # fields = (
    #     ('category','title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )



    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super().save_model(request,obj,form,change)
    #
    # def get_queryset(self, request):
    #     """定制列表页：只展示当前用户创建的文章"""
    #     qs = super(PostAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)



