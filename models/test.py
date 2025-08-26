import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import json
from rich import print
from models import User
from pathlib import Path

if __name__ == "__main__":
    path = Path(__file__).parent.parent / "data/user.json"
    with open(path) as f:
        data = json.load(f)

    user = User.model_validate(data)
    
    print(user)
