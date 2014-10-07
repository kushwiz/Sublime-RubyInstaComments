import sublime, sublime_plugin

"""
Command to stick in comments for a controller action
"""
class RcaCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    comment = file("rca.comment").read()
    pos = self.view.sel()[0].begin()
    self.view.insert(edit, pos, comment)

"""
Command to stick in comments for a model function
"""
class RmfCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    comment = file("rmf.comment").read()
    pos = self.view.sel()[0].begin()
    self.view.insert(edit, pos, comment)
