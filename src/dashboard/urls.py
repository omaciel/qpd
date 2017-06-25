from django.conf.urls import url
from dashboard.views import (
    api_root,
    OperatingSystemDetail,
    OperatingSystemList,
    ProductDetail,
    ProductList,
    ReleaseDetail,
    ReleaseList,
    TestRunDetail,
    TestRunList,
    )


urlpatterns = [
    url(r'^api/$', api_root, name='api_root'),
    # Operating System
    url(
        r'^api/v1/operating_systems/$',
        OperatingSystemList.as_view(),
        name='operating_system_list'),
    url(
        r'^api/v1/operating_systems/(?P<pk>[0-9]+)/$',
        OperatingSystemDetail.as_view(),
        name='operating_system_detail'),
    # Product
    url(
        r'^api/v1/products/$',
        ProductList.as_view(),
        name='product_list'),
    url(
        r'^api/v1/products/(?P<pk>[0-9]+)/$',
        ProductDetail.as_view(),
        name='product_detail'),
    # Release
    url(
        r'^api/v1/releases/$',
        ReleaseList.as_view(),
        name='release_list'),
    url(
        r'^api/v1/releases/(?P<pk>[0-9]+)/$',
        ReleaseDetail.as_view(),
        name='release_detail'),
    # TestRun
    url(
        r'^api/v1/testruns/$',
        TestRunList.as_view(),
        name='testrun_list'),
    url(
        r'^api/v1/testruns/(?P<pk>[0-9]+)/$',
        TestRunDetail.as_view(),
        name='testrun_detail'),
]
