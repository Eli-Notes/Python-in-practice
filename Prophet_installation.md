# Prophet Installation
Setting:windows 10, anaconda 3, python 3, 2019 Jul
1. Pip installation gets:
  `pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available`
  Solution: [stackoverflow](https://stackoverflow.com/questions/45954528/pip-is-configured-with-locations-that-require-tls-ssl-however-the-ssl-module-in):
2. Pip installation still collapses. So I use `conda install fbprophet`, but get `PackageNotFoundError: Packages missing in current channels`. Solution from [prophet - github](https://github.com/facebook/prophet): `conda install -c conda-forge fbprophet`. 
> **Anaconda**  
> `conda install -c conda-forge fbprophet`.  
> **Windows**  
> On Windows, `PyStan` requires a compiler so you'll need to follow the [instructions](https://pystan.readthedocs.io/en/latest/windows.html). The easiest way to install Prophet in Windows is in Anaconda.
4. Importing fbprophet results in `ERROR:fbprophet:Importing plotly failed. Interactive plots will not work`. Solution: `conda install plotly -y`.
