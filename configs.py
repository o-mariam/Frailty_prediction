import pathlib
import os

root_path = pathlib.Path(__file__).parent.absolute()
dataset_path = pathlib.Path(os.getenv("DATASET_DIR"))
raw_data_path = dataset_path


features_path = dataset_path / 'features'


