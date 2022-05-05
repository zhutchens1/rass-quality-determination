# Automated Determination of RASS Image Quality
Class Project for COMP 562: Introduction to Machine Learning (Spring 2022)<br>
Zack Hutchens, Andrew Zheng, Xu Tian, Xiao Wu

### Binder Link
To run our code, visit our [Binder repository](https://mybinder.org/v2/gh/zhutchens1/rass-quality-determination/HEAD) and open `FinalNotebook.ipynb`.

### Contents
 - `./exposuremaps/`: directory containing original RASS exposure maps in FITS image format.
 - `./exposuremaps/`: directory containing PNG versions of the RASS exposure maps, for easy-viewing.
 - `figures/`: directory containing some figures used in final report.
 - `features.csv`: CSV file containing features used for training k-means and Isolation Forest.
 - `prepare_features.py`: Python script to extract features from raw FITS exposure maps.
 - `FinalNotebook.ipynb`: Jupyter Notebook containing all plots, models, and analysis for the project.

### Dependencies 
 - python > 3.6
 - matplotlib
 - numpy 
 - pandas
 - scipy
 - scikit-learn
 - astropy 
