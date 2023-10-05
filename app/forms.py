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