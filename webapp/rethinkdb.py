import rethinkdb as r


class RethinkDBFactory(object):
    def __init__(self, host="127.0.0.1", port=28015, db="data", tables: dict = None, **kwargs):
        if tables is None:
            tables = {}
        self.host = host
        self.port = port
        self._db = db
        self._tables = tables
        self._conn = None
        self._init()

    def _init(self):
        conn = self.conn

        try:
            r.db_create(self._db).run(conn)
        except r.errors.ReqlOpFailedError as e:
            pass

        for table_name, index_names in self._tables.items():
            self.create_table(table_name, index_names)

    def create_table(self, table_name, index_names=None):
        if index_names is None:
            index_names = []
        conn = self.conn
        try:
            r.table_create(table_name).run(conn)
        except r.errors.ReqlOpFailedError as e:
            pass

        for idx_name in index_names:
            try:
                r.table(table_name).index_create(idx_name).run(conn)
            except r.errors.ReqlOpFailedError as e:
                pass

    @property
    def conn(self):
        if self._conn is None:
            return r.connect(self.host, self.port, self.db)
        else:
            return self._conn

    @property
    def db(self):
        return self._db


class RethinkResource(object):
    def __init__(self, factory: RethinkDBFactory = None, host="127.0.0.1", port: int = 28015, db="data",
                 tables: dict = None, **kwargs):
        if factory is None:
            self.factory = RethinkDBFactory(host, port, db, tables, **kwargs)
        else:
            self.factory = factory

    @property
    def conn(self):
        return self.factory.conn
