from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

storage_t = os.getenv('HBNB_TYPE_STORAGE')

if storage_t == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
