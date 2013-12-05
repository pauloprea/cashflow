from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
#from cashflow.views import PaymentView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login_required(TemplateView.as_view(template_name="cashflow/home.html")), name="home"),
    #(r'^payment$', PaymentView.as_view()),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'cashflow/login.html'}, name="login"),

)
