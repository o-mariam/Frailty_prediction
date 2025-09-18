from pathlib import Path

from configs import features_path, raw_data_path


def get_category_paths(category: str) -> tuple[Path, Path]:

    raw_dir = (Path(raw_data_path) / category).resolve()
    feature_dir = (Path(features_path) / category).resolve()
    feature_dir.mkdir(parents=True, exist_ok=True)
    return raw_dir, feature_dir
