#!/usr/bin/env python3
"""linking Basemodel to filestorage with the var storage"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
