import os.path
import os
from django.shortcuts import render_to_response, get_object_or_404

   
class Context:
   def __init__(self, config, title):
      self.config = config
      self.results = {"title" : title,
                      "components" :[]}
      self.stack = [self.results]
      
   def add_level(self,name):
      new = {"title": name,
             "components" : []}
      self.stack[-1]["components"].append(new)
      self.stack.append(new)

   def add_summary(self, summary):
      self.stack[-1]["summary"] = summary

   def add_path(self, path):
      self.stack[-1]["path"] = path

   def pop_level(self):
      self.stack.pop()

def process_one_dir(arg, dirname, fnames):
   arg.add_level(dirname)
   for name in fnames:
      arg.add_level(name)
      arg.pop_level()
   arg.pop_level()
def my_walk(path, arg):
   arg.add_level(os.path.basename(path))
   arg.add_path(path)
   if os.path.isdir(path):
      for item in os.listdir(path):
         my_walk(path+os.sep+item,arg)
   else:
      try:
         if os.stat(path)[6] < 100:
            arg.add_summary(open(path).readline())   
      except:
            pass
   arg.pop_level() 

def render_path(path, template, config):
   arg = Context(config, path)
   my_walk(path,arg)
   return render_to_response(template, {"tree" : arg.results})  

if __name__=="__main__":
  import sys
  arg = Context(None, "main") 
  os.path.walk(sys.argv[1], process_one_dir, arg)
  print arg.results   
