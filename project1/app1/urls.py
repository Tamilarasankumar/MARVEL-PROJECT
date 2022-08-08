
from django.urls import path
from.import views
urlpatterns = [
    path('',views.logging),
    path('marvel',views.show),
    path('new',views.callCreate),
    path('home',views.callList),
    path('<int:number>',views.callRead),
    path('edit/<int:new>',views.callEdit),
    path('del/<int:remove>',views.callDelete),
    path('short',views.callShort),
     path('logout',views.callOut)
]