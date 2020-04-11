from rope.base.project import Project
from rope.refactor.rename import Rename

proj = Project('../lib/ansible')

context = proj.get_file('context.py')

change = Rename(proj, context).get_changes('new_context')

proj.do(change)
