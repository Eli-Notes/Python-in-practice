# 1 Installation prophet
Setting:windows 10, anaconda 3, python 3, 2019 Jul
1. Attempted to pip isntall fbprophet, but got this:
  `pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available`
  The solution can be found in [stackoverflow](https://stackoverflow.com/questions/45954528/pip-is-configured-with-locations-that-require-tls-ssl-however-the-ssl-module-in):
  > For Windows 10 if you want use pip in normal cmd, not only in Anaconda prompt. you need add 3 environment paths. like these: D:\Anaconda3; D:\Anaconda3\Scripts; D:\Anaconda3\Library\bin.  
  > Most people only add D:\Anaconda3\Scripts;
2. However, something still went wrong when using pip.
3. So I used conda, but `conda install fbprophet` got `PackageNotFoundError: Packages missing in current channels`, so I found a new solution from [prophet - github](https://github.com/facebook/prophet): `conda install -c conda-forge fbprophet`. 
> **Anaconda**  
> Use `conda install gcc` to set up gcc. The easiest way to install Prophet is through conda-forge: `conda install -c conda-forge fbprophet`.  
> **Windows**  
> On Windows, `PyStan` requires a compiler so you'll need to follow the [instructions](https://pystan.readthedocs.io/en/latest/windows.html). The easiest way to install Prophet in Windows is in Anaconda.
4. When importing fbprophet, I got `ERROR:fbprophet:Importing plotly failed. Interactive plots will not work`. The solution is `conda install plotly -y`. Finally, it worked!
