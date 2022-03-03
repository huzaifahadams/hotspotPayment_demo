from .import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path('', views.LandingPageView.as_view(), name='landing-page')
    path('', views.LandingPageView ),
    #path('checkout/', views.Checkout ),
    #path('/',  views.cancle, name='cancle'),
   # path('checkme/', views.Checkme)
]

urlpatterns += staticfiles_urlpatterns()