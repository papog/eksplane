# Create your views here.
from django.http import HttpResponse
from popen2 import popen2
from django.shortcuts import render_to_response, get_object_or_404
import string
from eksplane.util.filetree import render_path





def show_path(request, object_path):
    return render_path(object_path, 'dirtree/tree.html', None)



