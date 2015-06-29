from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^goto/$', views.track_url, name='goto'),
        url(r'^register/$', views.register, name='register'),
        url(r'^profile/$', views.profile, name='profile'),
        url(r'^users/$', views.users, name='users'),
        url(r'^users/(?P<username>[\w\-]+)/$', views.user_profile, name='user_profile'),
        url(r'^like_category/$', views.like_category, name='like_category'),
        )