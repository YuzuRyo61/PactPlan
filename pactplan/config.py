import os
import toml


if os.path.isfile("config.toml"):
    with open("config.toml", "r", encoding="utf-8") as f:
        PP_CONFIG = toml.load(f)
else:
    raise OSError("Configuration file was not found.")
