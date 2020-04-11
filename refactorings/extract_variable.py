import rope.base.project
from rope.base import libutils

from rope.refactor.extract import ExtractVariable

project = rope.base.project.Project('../lib/ansible')

resource = libutils.path_to_resource(
    project, '../lib/ansible/collections/list.py')

extractor = ExtractVariable(project, resource, 1, 50)

changes = extractor.get_changes('extracted_variable')

project.do(changes)
