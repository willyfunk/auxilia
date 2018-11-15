from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('formulario/', views.formulario, name="formulario"),
    path('formulario/crear/', views.crear, name="crear"),
    path('embajadas/', views.embajadas, name="embajadas"),
    path('documentos/', views.documentos, name="documentos"),
    path('login',views.login,name="login"),
    path('cerrarsession',views.cerrar_session,name="cerrar_session"),
    path('login/iniciar',views.login_iniciar,name="iniciar"),
    path('vistaFormulario/',views.vistaFormulario, name="vistaFormulario"),
    path('vistaFormulario/modificar/<int:id>', views.modificar, name="modificar"),
    path('vistaFormulario/administrarMensajes/<int:id>', views.administrarMensajes, name="administrarMensajes"),

]