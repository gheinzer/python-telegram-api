import os
import gc
from tinydb import TinyDB, Query
gc.collect()


class filesystem():
    def listdir_recursively(path, filepath) -> list:
        database = TinyDB(filepath)
        table = database.table("files")
        files = []
        for root, dirs, files in os.walk(path):
            for name in files:
                table.insert({"filename": name})
            """for name in dirs:
                table.insert({"filename": name})"""
        return list(table.all())
        database.close()

    def wait_on_changes(path) -> list:
        try:
            os.remove("old_files.json")
        except:
            pass
        no_changes = True
        old_files = filesystem.listdir_recursively(path, "old_files.json")
        changes = []
        x = 0
        while no_changes:
            x = 0
            try:
                os.remove("new_files.json")
            except:
                pass
            new_files = filesystem.listdir_recursively(path, "new_files.json")
            for i in new_files:
                if not x > len(new_files) and not x > len(old_files) and not len(old_files) > len(new_files):
                    if not i == old_files[x]:
                        no_changes = False
                        changes.append(i)
                x = x + 1
                # no_changes = False
        return changes
