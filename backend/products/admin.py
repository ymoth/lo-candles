from django.http import HttpRequest
from tortoise.queryset import QuerySet

from products.models import Product

from django.contrib import admin


# Create a user admin page
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_top', 'is_published', 'category')

    actions = (
        '_set_actions_to_display_on_homepage',
        '_del_actions_to_display_on_homepage',
        '_set_is_published_true',
        '_set_is_published_false'
    )

    # list_filter = ('is_top',)

    # fieldsets = (
    #     (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
    #     ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')}),
    # )
    #
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2'),
    #     }),
    # )
    #
    # search_fields = ('email',)
    # ordering = ('email',)
    # filter_horizontal = ()

    @admin.action(description='Отображать на главной странице')
    def _set_actions_to_display_on_homepage(self, request: HttpRequest, queryset: QuerySet) -> None:
        """
        Метод для отображения товаров массово, для главной страницы.
        (Показывать на главной странице)
        """
        queryset.update(is_top=True)
        self.message_user(request, f'Было обновлено {queryset.count():,} записей')

    @admin.action(description='Не отображать на главной странице')
    def _del_actions_to_display_on_homepage(self, request: HttpRequest, queryset: QuerySet) -> None:
        """
        Метод для НЕ отображения товаров массово, для главной страницы.
        (Показывать на главной странице)
        """
        queryset.update(is_top=False)
        self.message_user(request, f'Было обновлено {queryset.count():,} записей')

    @admin.action(description='Поставить опубликованным')
    def _set_is_published_true(self, request: HttpRequest, queryset: QuerySet) -> None:
        queryset.update(is_published=True)
        self.message_user(request, f'Было обновлено {queryset.count():,} записей')

    @admin.action(description='Убрать публикацию')
    def _set_is_published_false(self, request: HttpRequest, queryset: QuerySet) -> None:
        queryset.update(is_published=False)
        self.message_user(request, f'Было обновлено {queryset.count():,} записей')


admin.site.register(Product, ProductAdmin)
admin.site.site_title = 'LO-Candle | Администрирование'
admin.site.site_header = 'LO-Candle | Администрирование'
