from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'protest.views.index'),
    url(r'^index/$', 'protest.views.index'),
    url(r'^protests/$', 'protest.views.protest_list'),
    url(r'^protests/(?P<pk>\d+)/$', 'protest.views.protest_detail'),
    url(r'^protests/new/$', 'protest.views.protest_new'),
    # url(r'^protests/(?P<pk>\d+)/edit/$', 'protest.views.protest_edit'),
    # url(r'^protests/(?P<protest_pk>\d+)/comments/new/$', 'protest.views.comment_new'),
    # url(r'^protests/(?P<protest_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'protest.views.comment_edit'),
    url(r'^users/(?P<pk>\d+)/$', 'protest.views.user_detail'),
    url(r'^accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)