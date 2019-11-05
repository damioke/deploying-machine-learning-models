import pathlib # For managing system path: a more modern and an alternative to os.path module)


PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent # (resolve) standardize the path and (parent) returns the root directory of __file__
TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_models'
DATASET_DIR = PACKAGE_ROOT / 'datasets'

TESTING_DATA_FILE = DATASET_DIR / 'test.csv'
TRAINING_DATA_FILE = DATASET_DIR / 'train.csv'
TARGET = 'SalePrice'


# Features we will be pulling out from the train.csv
FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood', 'OverallQual',
            'OverallCond', 'YearRemodAdd', 'RoofStyle', 'MasVnrType',
            'BsmtQual', 'BsmtExposure', 'HeatingQC', 'CentralAir',
            '1stFlrSF', 'GrLivArea', 'BsmtFullBath', 'KitchenQual',
            'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageFinish',
            'GarageCars', 'PavedDrive', 'LotFrontage',
            # this variable is only to calculate temporal variable:
            'YrSold']


def save_pipeline() -> None:
    """Persist the pipeline."""

    pass


# This function relies on code from the pipeline.py module
def run_training() -> None:
    """Train the model."""

    print('Training...')


if __name__ == '__main__':
    run_training()
