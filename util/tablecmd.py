from popen2 import popen2
import sys
import string
import re
from django.shortcuts import render_to_response, get_object_or_404

def render_program_output(command, template):
    (out,err) = popen2(command)
    line_list = out.readlines()
    object_list = []
    for line in line_list:
        object_list.append(string.split(line))
    print >> sys.stderr, command
    return render_to_response(template, {'object_list': object_list})

def render_program_output_with_heads(command, template, url_map):
    (out,err) = popen2(command)
    line_list = out.readlines()
    object_list = []
    if len(line_list) > 1:
        head_list = string.split(line_list[0])
        for line in line_list[1:]:
            row = []
            item_list = string.split(line)
            for index in range(len(item_list)):
                dict = {'data' : item_list[index]}
                try:
                    dict ['url'] = url_map.get(head_list[index]) 
                except:
                    dict ['url'] = None
                row.append(dict) 
            object_list.append(row)
    else:
        head_list = []
        object_list = []
    print >> sys.stderr, command
    return render_to_response(template, {'head_list' : head_list,
                                         'object_list': object_list})



