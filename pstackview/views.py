# Create your views here.
from django.http import HttpResponse
from popen2 import popen2
from django.shortcuts import render_to_response, get_object_or_404
import string
import sys

def render_program_output(command, template):
    (out,err) = popen2(command)
    line_list = out.readlines()
    object_list = []
    for line in line_list:
        object_list.append(string.split(line))
    print >> sys.stderr, command
    return render_to_response(template, {'object_list': object_list})



def show_one_process(request, object_id):
    return render_program_output(['pstack',str(object_id)],'pstackview/pstack.html') 



