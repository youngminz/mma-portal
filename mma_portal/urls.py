from django.urls import include, path

urlpatterns = [
    path('company/', include('company.urls')),
]
