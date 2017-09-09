import os
from databases.Database import Database
from databases.Table import Table
class Accounts(Database):
    def __init__(self): super().__init__()
    @property
    def Tables(self): return [Accounts.Accounts()]
    
    class Accounts(Table):
        def __init__(self):
            super().__init__()
        @property
        def CreateTableSql(self): return """create table Accounts(
        Id          integer primary key,
        Username    text not null,
        MailAddress text unique not null,
        Password    text not null,
        CreatedAt   text,
        UpdatedAt   text
    );
    """

        
