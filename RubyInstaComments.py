import sublime, sublime_plugin
import sys
import re
from os.path import join

PLUGIN_NAME = "RubyInstaComments"

plugin_dir = join(sublime.packages_path(), PLUGIN_NAME)

"""
Command to stick in comments for a controller action
"""
class RubyActionCommentCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    comment = file(plugin_dir+"/rca.comment").read()
    pos = self.view.sel()[0].begin()
    method_defn = self.view.substr(self.view.sel()[0])
    action_name = self.extract_method_name(method_defn)
    comment = comment.replace("<action_name>", action_name)
    self.view.insert(edit, pos, comment)

  def extract_method_name(self, method_defn):
    p = re.compile("def (.*)")
    return p.search(method_defn).group(1)

"""
Command to stick in comments for a model function
"""
class RubyMethodCommentCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    comment = file(plugin_dir+"/rmf.comment").read()
    pos = self.view.sel()[0].begin()
    self.view.insert(edit, pos, comment)

