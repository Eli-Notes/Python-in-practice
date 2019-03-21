# How to connect to MySQL using pkg MySQLdb, on windows

## 1 Before All
1. Suppose you are using Python37 on windows. (other versions are also ok mostly.)
2. Install MySQL and make connection to the database you want to manipulate.
3. Install Visual Studio C++ (at least in version of 2014).

## 2 Install MySQLdb
1. Try to install 'mysqlclient', According to [How to install Python MySQLdb module using pip?](https://stackoverflow.com/questions/25865270/how-to-install-python-mysqldb-module-using-pip), `pip` can be used in windows command line:
```cmd
pip install mysqlclient
```
2. Maybe you will see an error like ["fatal error C1083: Cannot open file: 'mysql.h': No such file or directory](https://stackoverflow.com/questions/51294268/pip-install-mysqlclient-returns-fatal-error-c1083-cannot-open-file-mysql-h). According to link here, this error occurs when trying to install mysqlclient for python32 in 64 bit environments, so there are two solutions(I suggest the second one):
   1. Uninstall python and re-install 64 bit version.
   2. Download wheel from [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient.Then), the file name could be like this:
      * mysqlclient‑1.4.2‑cp37‑cp37m‑win32.whl
      * mysqlclient‑1.4.2‑cp37‑cp37m‑win_amd64.whl
   3. Just try to install either of them (if you are using python3.7) in command line:
```cmd
pip install "path to the downloaded .whl file"
```
After solving the problem, you can install `mysqlclient` successfully.

## 3 Manipulate on MySQL with pkg MySQLdb
```python
import MySQLdb
def changeMySQL(queryList, dbArg):
# queryList: string list of sql querys
# dbArg: arguments for database connection, including Host, User, Password, and Database Name.
    connection = MySQLdb.connect(
        host   = dbArg["MySQL_Host"],
        user   = dbArg["MySQL_User"],
        passwd = dbArg["MySQL_Password"],
        db     = dbArg["MySQL_Database"]
        for q in queryList:
            if len(q) > 0:
                #connection.query() # we should not use 'query', but 'execute'.
                cursor = connection.cursor()
                cursor.execute(q)
                connection.commit() # to commit all the changes that we 'loaded' into the mysql server.
                cursor.close()
        connection.close()
