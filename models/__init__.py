"""

#!/usr/bin/python3
Init method
"""
#from models.engine.file_storage import FileStorage
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
