from django.urls import path

from api.views import *

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("product",ProductCrud,basename="product")
router.register("productread",ProductReadOnly,basename="readonlypro")
router.register("order/(?P<product_id>\d+)",OrderView,basename="order")
router.register("allorders",AllOrderedProductsView,basename="all-order")
router.register("maxporducts",ProductListView,basename="maxproducts")


urlpatterns=[
    path('register/',SignUpView.as_view()),
    path('token/',ObtainAuthToken.as_view(),name="token"),
]+router.urls