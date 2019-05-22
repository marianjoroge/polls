from django.conf.urls import url


from .views import pollsAPIView


urlpatterns = [
    url(r'^$', pollsAPIView.as_view(),
        name='polls-create'),
]
