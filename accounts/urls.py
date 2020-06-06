from django.urls import url
from accounts.views import login_view, profile_view, register_view

urlpatterns = [
    url(r'^login/$', login_view, name='login_page'),
    url(r'^profile/$', profile_view, name='profile_page'),
    url(r'^register/$', register_view, name='register_page')

]
