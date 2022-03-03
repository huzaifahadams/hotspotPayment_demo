
from django.contrib import admin
from django.urls import include,  path

from pay.views import (
    #CreateCheckoutSessionView,
    LandingPageView

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pay.urls')),

    #path('Create-Checkout-Session', CreateCheckoutSessionView.as_view(), name = 'CreateCheckoutSession')
]
