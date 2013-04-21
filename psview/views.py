# Create your views here.
from django.http import HttpResponse
from popen2 import popen2
from django.shortcuts import render_to_response, get_object_or_404
import string
from eksplane.util.tablecmd import render_program_output, render_program_output_with_heads


action_list = [{'url': '/pstackview/',
               'text': 'Get the current call stack of the process (pstack)'},
               {'url': '/lsofview/',
                'text': 'list all the open files of the process (lsof)'},
              ]
def list(request):
    return render_program_output_with_heads(['ps','aux'],
                                            'psview/ps_list.html',
                                            {'PID' : '/psview/'}   )



def show_one_process(request, object_id):
    return render_to_response('psview/ps_object.html', {'object_id': object_id,
                                                        'action_list' : action_list}) 



