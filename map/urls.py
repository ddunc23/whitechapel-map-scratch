from django.conf.urls import include, url
import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'map_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name='home'),
    url(r'feature/(?P<feature>\d+)/$', views.feature, name='feature'),
    url(r'feature/(?P<feature>\d+)/detail/$', views.detail, name='detail'),
    url(r'feature/(?P<feature>\d+)/legend/$', views.feature_legend, name='feature_legend'),
    url(r'^category/(?P<category>\w+)/$', views.category, name='category'),
    url(r'^features/tagged/(?P<tag>.+)/$', views.tag, name='tag'),
    url(r'^api/features/$', views.features, name='features'),
    url(r'^api/features/date/(?P<build_date>\d+)/$', views.features_by_build_date, name='features_by_date'),
    url(r'^api/features/date/(?P<start_date>\d+)/(?P<end_date>\d+)/$', views.features_by_date_range, name='features_by_date_range'),
    url(r'^api/features/street/(?P<street>.+)/$', views.features_by_street_name, name='features_by_street_name'),
    url(r'^api/features/category/(?P<category>\d+)/$', views.features_by_category, name='features_by_category'),
    url(r'^api/features/tagged/(?P<tag>.+)/$', views.features_by_tag, name='features_by_tag'),
]