import yaml

def load_yaml(path: str):
    """
    Load a YAML file and return its content.

    Parameters
    ----------
    path : str
        Path to the YAML file.

    Returns
    -------
    dict or list
        Parsed YAML content.
    """
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
