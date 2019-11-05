from sklearn.pipeline import Pipeline # used to define transformation

import preprocessors as pp #  a module (preprocessors.py) we've created for all transformation/preprocessing


CATEGORICAL_VARS = ['MSZoning',
                    'Neighborhood',
                    'RoofStyle',
                    'MasVnrType',
                    'BsmtQual',
                    'BsmtExposure',
                    'HeatingQC',
                    'CentralAir',
                    'KitchenQual',
                    'FireplaceQu',
                    'GarageType',
                    'GarageFinish',
                    'PavedDrive']

PIPELINE_NAME = 'lasso_regression'

price_pipe = Pipeline(
    [
        ('categorical_imputer',
         pp.CategoricalImputer(variables=CATEGORICAL_VARS)),
    ])
