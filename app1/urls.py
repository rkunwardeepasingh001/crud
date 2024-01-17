from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path("create/",views.create),
  path("",views.retrive,name='read'),
  path("<int:id>/update/",views.update),
  path("<int:id>/delete/",views.delete,name='delete'),
  path("<int:id>/sure_delete/",views.sure_delete,name='sure_delete'),
  path("<int:id>/V_P_detail/",views.view_persional_detail,name='view')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)