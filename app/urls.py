'''
Copyright 2023, Thomas Wright

LICENSE NOTICE
This file is part of The Pep Genie.
The Pep Genie is free software: 
you can redistribute it and/or modify it under the terms of the 
GNU General Public License as published by the Free Software Foundation, 
either version 3 of the License, or (at your option) any later version.
The Pep Genie is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with The Pep Genie.
If not, see <https://www.gnu.org/licenses/>. 


'''



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