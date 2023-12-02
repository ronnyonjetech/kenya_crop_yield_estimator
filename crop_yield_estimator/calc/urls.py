
from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    # path('add',views.add,name='add'),
    path('predict',views.predict,name='predict'),
    path('calculations',views.calculations,name='calculations'),

]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)