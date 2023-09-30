"""
Optional script only for preloading a model.
"""
import yaml

from main import CONFIG_PATH
from main import load_model


if __name__ == "__main__":
    with open(CONFIG_PATH, "r") as config_file:
        config = yaml.safe_load(config_file)

    load_model(config["model_size"])
