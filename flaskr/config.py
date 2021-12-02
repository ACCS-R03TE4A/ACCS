import os

DATABASE_CONNECTINO_STRING = f"mongodb://accs:{os.environ['mongodb_password']}@192.168.1.111:27017/ACCS"
DATABASE_NAME = "ACCS"