import numpy as np
from astropy.io import fits
import pandas as pd
from os import listdir

def get_features(folder,funcs,keys):
    """
    Extract table of metadata features
    from a subdirectory of exposure maps.

    Parameters
    -----------------
    folder : str
        Path to folder containing images with filenames
        like rs9*.fits.
    funcs : list of callable
        List of functions used to extract features.
        Each function should take a single input of
        a 2D numpy array.
    keys : list of strings
        List of size len(funcs) describing what each feature
        will be named in the dataframe.

    Returns
    -----------------
    X : pd.DataFrame
        Data table of features for training. Unique rows are given by
        `image`.
    """
    files = listdir(folder)
    features=[]
    names=[]
    for ff in files:
        name = ff.split('_')[0]
        image_array = fits.open(folder+ff)[0].data
        features.append([ff(image_array) for ff in funcs]+[name])
    X = pd.DataFrame(features, columns = keys+['image'])
    return X

if __name__=='__main__':
    X = get_features('./exposuremaps/',\
        [lambda x: len(x[x<50]), contrast, np.sum], \
        [ 'N50', 'contrast', 'sum']
    )
    print(X)
    X.to_csv("features.csv",index=False)
