from django.contrib import admin
from celery_tasks.task import generate_static_index_html
from goods.models import GoodsType, IndexPromotionBanner, IndexTypeGoodsBanner, IndexGoodsBanner


class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """新增或更新表中数据的数据时使用"""
        super().save_model(request, obj, form, change)
        # 发出任务让celery重新生成首页静态页面
        generate_static_index_html.delay()

    def delete_model(self, request, obj):
        """删除表中的数据时使用"""
        super().delete_model(request, obj)
        generate_static_index_html.delay()


class IndexPromotionBannerAdmin(admin.ModelAdmin):
    pass


class GoodsTypeAdmin(BaseModelAdmin):
    pass


class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    pass


class IndexGoodsBannerAdmin(BaseModelAdmin):
    pass


admin.site.register(GoodsType)
admin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)
admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
admin.site.register(IndexTypeGoodsBanner, IndexTypeGoodsBannerAdmin)
