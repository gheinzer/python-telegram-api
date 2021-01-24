from actions.DeleteObject import DeleteObject
from actions.DeletePath import DeletePath
from actions.NewObject import NewObject
from actions.NewPath import NewPath


class actions:
    def DeleteObject(object_name: str):
        DeleteObject.DeleteObject()

    def NewObject(object_name: str, search_name: str):
        NewObject.NewObject()

    def NewPath(path: str):
        NewPath.NewPath()

    def DeletePath(object_name: str):
        DeletePath.DeletePath()
