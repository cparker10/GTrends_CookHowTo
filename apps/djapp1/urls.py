from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.homepage),
    # url('admin/', admin.site.urls),
    # url('', include('djapp1.urls')),
]
