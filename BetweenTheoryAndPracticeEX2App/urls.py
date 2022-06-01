from django.urls import re_path as url
from BetweenTheoryAndPracticeEX2App import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^api/users$', views.userApi),
    url(r'^api/user/([0-9]+)$', views.userApi),
    url(r'^api/users/$', views.filteredData),
    url(r'^api/users/exportToExcel$', views.exportToExcel)

]
