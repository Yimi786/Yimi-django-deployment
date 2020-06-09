from django.conf.urls import url
from App_Five import views

# TEMPLATE URLS!
app_name = 'App_Five'

urlpatterns = [
    url(r'^register/$',views.register, name='register'),
    #url(r'^media/profile_pics',views.register, name='register'),
    url(r'^user_login/$',views.user_login, name='user_login'),

]
