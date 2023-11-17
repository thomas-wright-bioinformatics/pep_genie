from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('request', views.request, name='request'),
    path('validate',views.validate, name = 'validate'),
    path('graph_types',views.graph_types, name = 'graph_types'),
    path('grid_test',views.grid_test, name = 'grid_test'),
    path('grid_con',views.grid_con, name = 'grid_con'),
    path('grid_vis',views.grid_vis, name = 'grid_vis'),
    path('grid_vis_after',views.grid_vis_after, name = 'grid_vis_after'),
    path('download',views.download, name = 'download'),
    path('grid_result',views.grid_result, name = 'grid_result'),
    path('file_download',views.file_download, name = 'file_download'),
    path('ss_form',views.ss_form, name = 'ss_form'),
    path('ss_result',views.ss_result, name = 'ss_result'),
    path('documentation',views.documentation, name = 'documentation'),
    path('tutorial',views.tutorial, name = 'tutorial')
]