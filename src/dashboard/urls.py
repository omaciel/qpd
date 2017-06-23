from django.conf.urls import url
from dashboard.views import (
    api_root,
    get_delete_update_operating_system,
    get_post_operating_systems,
    get_delete_update_product,
    get_post_products,
    get_delete_update_release,
    get_post_releases,
    get_delete_update_testrun,
    get_post_testruns,
    )


urlpatterns = [
    url(r'^api/$', api_root, name='api_root'),
    url(
        r'^api/v1/operating_systems/(?P<pk>[0-9]+)$',
        get_delete_update_operating_system,
        name='get_delete_update_operating_system'
    ),
    url(
        r'^api/v1/operating_systems/$',
        get_post_operating_systems,
        name='get_post_operating_systems'
    ),
    url(
        r'^api/v1/products/(?P<pk>[0-9]+)$',
        get_delete_update_product,
        name='get_delete_update_product'
    ),
    url(
        r'^api/v1/products/$',
        get_post_products,
        name='get_post_products'
    ),
    url(
        r'^api/v1/releases/(?P<pk>[0-9]+)$',
        get_delete_update_release,
        name='get_delete_update_release'
    ),
    url(
        r'^api/v1/releases/$',
        get_post_releases,
        name='get_post_releases'
    ),
    url(
        r'^api/v1/testruns/(?P<pk>[0-9]+)$',
        get_delete_update_testrun,
        name='get_delete_update_testrun'
    ),
    url(
        r'^api/v1/testruns/$',
        get_post_testruns,
        name='get_post_testruns'
    ),
]
