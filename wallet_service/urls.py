from django.contrib import admin
from django.urls import path, include
from wallet import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('wallet.urls')),
    path('',  views.create_account, name='create-account')
]
