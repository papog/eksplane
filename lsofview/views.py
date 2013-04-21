# Create your views here.
from django.http import HttpResponse
from popen2 import popen2
from django.shortcuts import render_to_response, get_object_or_404
import string
import sys
from eksplane.util.tablecmd import render_program_output


def list(request):
    return render_program_output('/usr/sbin/lsof','lsofview/lsof_list.html')


def show_one_process(request, object_id):
    return render_program_output(['/usr/sbin/lsof','-p',str(object_id)],'lsofview/lsof_list.html') 



