from django.urls import path,include
from home import views
app_name='home'
urlpatterns = [
path('',views.HomeView.as_view(),name='home'),
    path('unit/<str:slug>',views.units_detail,name='unit_detail'),
    path('departament/<str:slug>',views.departament_detail,name='departament_detail'),
    path('departament_block/<str:slug>',views.departament_block_detail,name='departament_block_detail'),
]
