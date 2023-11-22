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



from .models import gridModel
from django import forms 


class gridModelForm(forms.ModelForm):
    class Meta:
        model = gridModel
        fields = ('img_test','img_con','img_vis','cols','first_col','strip_request','graph_types')
        labels = {
        "img_test": "1) Test Array Image:",
        "img_con": "2) Control Array Image:",
        "img_vis": "3) UV/Vis Array Image:",
        "cols": "4) Number of Columns in Array:",
        "first_col": "5) Number of First Column:",
        "strip_request": "6) Enter Your Desired Strips:",
        "graph_types": "7) Enter the Type of Graph for Each Strip:",
        }