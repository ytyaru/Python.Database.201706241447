from abc import ABCMeta, abstractmethod
import os
import dataset
import inspect
import databases.Table
class Database(metaclass=ABCMeta):
    def __init__(self):
        pass    
    """
    DBファイルがなければ作成。テーブルがなければ作成。dataset.connect()の戻り値を返す。
    """
    def Initialize(self, dir_path):
        self.__dir_path = dir_path
        os.makedirs(self.__dir_path, exist_ok=True)
        if not os.path.isdir(self.__dir_path): raise Exception('引数dir_pathにはディレクトリのパスを指定してください。: {0}'.format(self.__dir_path))
        return self.__Create()
    
    def __Create(self):
        if not os.path.isfile(self.Path):
            with open(self.Path, mode='w', encoding='utf-8') as f: f.write('')
        self.__db = dataset.connect('sqlite:///' + self.Path)
        self.__CreateTables()
        self.__CreateTableInstances()
        return self.__db
    
    def __CreateTables(self):
        for table in self.Tables:
            if table.Name not in self.__db.tables:
                self.__db.query(table.CreateTableSql)
    
    """
    本クラス継承クラスの定義内でTable継承クラスを定義するとそのインスタンスを生成する。
    """
    def __CreateTableInstances(self):
        self.__tables = []
        classes = inspect.getmembers(self, inspect.isclass)
        for c in classes:
            name, typ = c
            print(name, typ)
            if isinstance(typ, databases.Table.Table): self.__tables.append(typ())

    @property
    def Tables(self): return self.__tables
    
#    @property
#    @abstractmethod
#    def Tables(self): pass
    
    @property
    def Path(self): return os.path.join(self.DirectoryPath, (self.Filename + '.' + self.Extension))
    @property
    def DirectoryPath(self): return self.__dir_path
    @property
    def Filename(self): return self.__class__.__name__
    @property
    def Extension(self): return 'sqlite3'

