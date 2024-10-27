from django.urls import path

from app.views import *

urlpatterns = [
    path('', toWelcomeView),
    path('types/page/view', toTypeView),
    path('types/add/view', toTypeAddView),
    path('types/add/form', typeAddForm),
    path('types/upd/view', toTypeUpdView),
    path('types/upd/form', typeUpdForm),
    path('types/del/form', typeDelForm),

    path('infos/page/view', toInfoView),
    path('infos/add/view', toInfoAddView),
    path('infos/add/form', InfoAddForm),
    path('infos/upd/view', toInfoUpdView),
    path('infos/upd/form', InfoUpdForm),
    path('infos/del/form', InfoDelForm)
]