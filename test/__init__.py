import os

current_path = os.path.dirname(__file__)
BasePath = "/".join(current_path.split("/")[:-1]) + "/"
print(current_path, BasePath)
