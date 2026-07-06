import os
base_dir = os.path.dirname(os.path.dirname(_index_ if "_index" in locals() else __file_))
app_path = os.path.join(base_dir, "app.py")

with open(app_path, "r", encoding="utf-8") as f:
    code = f.read()

exec(code, globals())
