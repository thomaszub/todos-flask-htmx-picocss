import os
import shutil
from typing import List, Tuple


def copy_assets(assets: List[Tuple[str, str]]):
    for asset in assets:
        source = asset[0]
        target = asset[1]
        os.makedirs(name=target, exist_ok=True)
        shutil.copy(src=source, dst=target)


if __name__ == "__main__":
    assets = [
        ("node_modules/@picocss/pico/css/pico.min.css", "todos/static/assets/css"),
        ("node_modules/@picocss/pico/css/pico.min.css.map", "todos/static/assets/css"),
        ("node_modules/htmx.org/dist/htmx.min.js", "todos/static/assets/js"),
    ]
    copy_assets(assets)
