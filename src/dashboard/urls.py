from django.conf.urls import url
from dashboard import views


urlpatterns = [
    url(
        r'^api/v1/operating_systems/(?P<pk>[0-9]+)$',
        views.get_delete_update_operating_system,
        name='get_delete_update_operating_system'
    ),
    url(
        r'^api/v1/operating_systems/$',
        views.get_post_operating_sytems,
        name='get_post_operating_systems'
    )
]
