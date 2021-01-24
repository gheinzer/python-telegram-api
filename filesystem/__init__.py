import os
import gc
from tinydb import TinyDB, Query
gc.collect()


class filesystem():
    def listdir_recursively(path):
        database = TinyDB("files.json")
        table = database.table("files")
        files = []
        for root, dirs, files in os.walk(path):
            for name in files:
                table.insert({"filename": name})
            for name in dirs:
                table.insert({"filename": name})
        return list(table.all())

    def wait_on_changes(path):
        no_changes = True
        while no_changes:
            old_files = database = TinyDB("files.json")
            table = database.table("old_files")


print(filesystem.wait_on_changes("./"))
