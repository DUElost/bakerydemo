import debug_toolbar
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.images.views.serve import ServeView
# 重定向
from bakerydemo import views
from bakerydemo.student import views

from bakerydemo.search import views as search_views
# 登录和注册
from django.contrib.auth import views as auth_views
from bakerydemo.student import views as student_views
from bakerydemo.teacher import views as teacher_views
from .api import api_router

# from django.conf.urls.i18n import i18n_patterns
# from search import views as search_views

urlpatterns = [
    path('django-admin', admin.site.urls),
    path('admin', include(wagtailadmin_urls)),
    path('documents', include(wagtaildocs_urls)),
    # 登录和注册url patterns
    path('accounts/', include('allauth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='account_login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='account_logout'),
    path('accounts/password/change/', auth_views.PasswordChangeView.as_view(), name='account_change_password'),
    path('accounts/password/reset/', auth_views.PasswordResetView.as_view(), name='account_reset_password'),
    path('accounts/password/reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='account_reset_password_done'),
    # 学生端页面路由信息
    path('emotion_record/', student_views.emotion_record, name='emotion_record'),
    path('student_homepage/', student_views.student_homepage, name='student_homepage'),
    path('wellness/', student_views.wellness, name='wellness'),
    path('wellness/mood_check/', student_views.mood_check_view, name='mood_check'),
    # path('mood_check_history/', student_views.mood_check_history, name='mood_check_history'),
    path('mood_check_history/', student_views.form_submissions_view, name='form_submissions'),
    path('myclass/', student_views.myclass_view, name='my_class'),
    path('personal/', student_views.personal_history, name = 'personal_history'),

    # 教师端页面路由信息
    path('mood_check_management/', teacher_views.form_submissions_view, name='mood_check_management'),
    path('mood_check_management/submissions/<int:submission_id>/update/', teacher_views.update_submission_view,
         name='update_submission'),
    path('myclass_manager/', teacher_views.myclass_manager_view, name='myclass_manager'),
    path('counseling_record/', teacher_views.counseling_record_view, name='counseling_record'),
    path('counseling_record/submissions/<int:submission_id>/update/', teacher_views.update_counseling_submission_view,
         name='update_counseling_submission'),


    # 系统后台页面路由信息
    re_path(
        r"^images/([^/]*)/(\d*)/([^/]*)/[^/]*$",
        ServeView.as_view(),
        name="wagtailimages_serve",
    ),
    path("search/", search_views.search, name="search"),
    path("sitemap.xml", sitemap),
    path("api/v2/", api_router.urls),
    path("__debug__/", include(debug_toolbar.urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView
    from django.views.generic.base import RedirectView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path(
            "favicon.ico",
            RedirectView.as_view(url=settings.STATIC_URL + "img/bread-favicon.ico"),
        ),
        path(
            "wellness.svg",
            RedirectView.as_view(url=settings.STATIC_URL + "img/wellness.3fb9e660.svg")
        )
    ]

    # Add views for testing 404 and 500 templates
    urlpatterns += [
        path("test404/", TemplateView.as_view(template_name="404.html")),
        path("test500/", TemplateView.as_view(template_name="500.html")),
    ]

urlpatterns += [
    path("", include(wagtail_urls)),
]

# 多语言功能
# urlpatterns += i18n_patterns(
#     # 下面这些URLs将带有前面追加的 /<language_code>/
#     # re_path(r'^search/$', search_views.search, name='search'),
#     re_path(r'', include(wagtail_urls)),
# )
