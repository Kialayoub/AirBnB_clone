#!/usr/bin/python3
"""create an object of the FileStorage class and reload data"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
