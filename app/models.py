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




from django.conf import settings
from django.db import models
from django.utils import timezone

from email.policy import default
from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension

import datetime
import os
import random


dummy_url = os.path.join(settings.BASE_DIR, 'app/dummy.png')

def fileFormat(instance, filename):
    return '{0}/{1}/{2}'.format('sd',instance.user_id,filename)


class gridModel(models.Model):

    #form 
    cols = models.IntegerField(default=4)
    first_col = models.IntegerField(default=8)
    strip_request = models.CharField(max_length=1000, default='A08-T08,A09-T09')
    graph_types = models.CharField(max_length=1000, default='d')
    strip_request_string = models.CharField(max_length=1000, default='A08-T08,A09-T09')
    measure_diameter = models.IntegerField(default=70)
    #norm = models.BooleanField(default=False)

    img_test = models.FileField(upload_to=fileFormat, validators=[validate_image_file_extension])
    img_test_crop = models.ImageField(upload_to=fileFormat,default=dummy_url, null=True)
    img_test_coords = models.CharField(max_length=200, default = 'empty')
    img_test_csv = models.FileField(upload_to=fileFormat)

    img_con = models.FileField(upload_to=fileFormat)
    img_con_crop = models.ImageField(upload_to=fileFormat,default=dummy_url, null=True)
    img_con_coords = models.CharField(max_length=200, default = 'empty')
    img_con_csv = models.FileField(upload_to=fileFormat)

    img_vis_crop = models.ImageField(upload_to=fileFormat,default=dummy_url, null=True, blank=True)
    img_vis = models.FileField(upload_to=fileFormat)
    img_vis_coords = models.CharField(max_length=200, default = 'empty')
    img_vis_csv = models.FileField(upload_to=fileFormat)

    #gen
    user_id = models.CharField(max_length=100)
    ppt_path = models.CharField(max_length=100)
    full_grid = models.ImageField(upload_to=fileFormat,default=dummy_url)
    dens_list = models.CharField(max_length=1000, default='null')
    config = models.CharField(max_length=1000, default="{'c':0}") #user_id,  
    normalised_csv = models.FileField(upload_to=fileFormat)   


