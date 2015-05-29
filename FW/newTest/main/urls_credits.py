# =====================
# FEATURE BEGIN : MONEY
# =====================
from django.conf.urls import patterns, url

from main.fw_views import credits_view

urlpatterns = patterns('',
                       url(r'^credit/$',
                           credits_view,
                           name='credit_page'),
                       )
# ===================
# FEATURE END : MONEY
# ===================
