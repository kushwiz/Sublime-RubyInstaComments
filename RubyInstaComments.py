import sublime, sublime_plugin

"""
Command to stick in comments for a controller action
"""
class RcaCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    comment = """  # Public: The / action
  #
  # params - The Hash options
  #
  # Renders <action name> action
  """
    pos = self.view.sel()[0].begin()
    self.view.insert(edit, pos, comment)

"""
Command to stick in comments for a model function
"""
class RmfCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    comment = """  # <access modifier>: <description>
  #
  # parameters -
  #
  # Returns <return type>
  """
    pos = self.view.sel()[0].begin()
    self.view.insert(edit, pos, comment)