import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

FREMONT_URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"


def get_fremont_data(filename='fremont.csv', url=FREMONT_URL, force_download=False):
    """Download and cache the fremont data
    
    Parameters
    ----------
    filename : string (optional)
        location to save teh data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force redownload of the data
    
    Returns
    ----------
    data: pandas.DataFrame
        The Fremont bridge data
    """
    if force_download or not os.path.exists(filename):
        Fremont = pd.read_csv(URL)
        Fremont.to_csv('fremont.csv')
    data=pd.read_csv('fremont.csv', index_col='Date', parse_dates=True)
    data.drop(columns = "Unnamed: 0", inplace=True)
    data.columns = ('West', 'East')
    data['Total'] = data.West + data.East
    return data