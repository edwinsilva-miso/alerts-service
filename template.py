import os
from pathlib import Path

PROJECT_NAME = "alerts-service"

LIST_FILES = [
    "Dockerfile",
    ".env",
    ".gitignore",
    "app.py",
    "init_setup.py",
    "README.md",
    "requirements.txt",
    "src/__init__.py",
    # config folder
    "src/config/__init__.py",
    "src/config/config.py",
    "src/config/dev_config.py",
    "src/config/production.py",
    # core
    "src/core/__init__.py",
    "src/core/services/__init__.py",
    "src/core/services/alert_service.py",
    # models
    "src/models/__init__.py",
    "src/models/alert.py"
    # ports
    "src/ports/__init__.py",
    "src/ports/input/__init__.py",
    "src/ports/input/controllers/__init__.py",
    "src/ports/input/controllers/alert_controller.py",
    "src/ports/output/__init__.py",
    "src/ports/output/gateway/__init__.py",
    "src/ports/output/gateway/event_gateway.py",
    # routes and utils
    "src/routes.py",
    "src/utils.py",
]

for file_path in LIST_FILES:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    # first make dir
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        print(f"Creating Directory: {file_dir} for file: {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            print(f"Creating an empty file: {file_path}")
    else:
        print(f"File already exists {file_path}")