# 1 Installition on windows
1. Attempted to pip, but got this:
  `pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available`
  The solution is [stackoverflow](https://stackoverflow.com/questions/45954528/pip-is-configured-with-locations-that-require-tls-ssl-however-the-ssl-module-in):
  > For Windows 10 if you want use pip in normal cmd, not only in Anaconda prompt. you need add 3 environment paths. like these: D:\Anaconda3; D:\Anaconda3\Scripts; D:\Anaconda3\Library\bin. Most people only add D:\Anaconda3\Scripts;
2. However, something wrong still when using pip.
3. So I use conda, but `conda install fbprophet` got `PackageNotFoundError: Packages missing in current channels`, so I found a new solution: `conda install -c conda-forge fbprophet`
