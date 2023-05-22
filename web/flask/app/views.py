from flask import Flask
import psycopg2 as pg

app = Flask(__name__)

try:
    conn = pg.connect(
        host='localhost',
        database='postgres',
        port=5432,
        user='postgres',
        password='admin'
    )

    cursor = conn.cursor()
    print('Connection is enabled')

except Exception as e:
    print('Something went wrong')
    print(e)


class Schema:
    TABLENAME = "TODO"

    def __init__(self):
        try:
            self.conn = pg.connect(
                host='localhost',
                database='postgres',
                port=5432,
                user='postgres',
                password='admin'
            )

            self.cursor = conn.cursor()
            print('Connection is enabled')
            self.create_to_do_table()
            self.create_user_table()

        except Exception as e:
            print('Something went wrong')
            print(e)

    def create_to_do_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS "Todo" (
            id INTEGER PRIMARY KEY,
            Tittle TEXT,
            Description TEXT,
            _is_done boolean,
            _is_deleted boolean,
            CreatedOn Date DEFAULT CURRENT_DATE,
            DueDate Date
            );
        """

        self.cursor.execute(query)
        self.conn.commit()

    def create(self, text, description):
        query = f'INSERT INTO {self.TABLENAME} ' \
            f'(Title, Description) ' \
            f'values ("{text}",{description})'

        result = self.cursor.execute(query)
        self.conn.commit()

    def create_user_table(self):
        pass


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/<name>')
def hello_name(name):
    return 'Hello ' + name


if __name__ == '__main__':
    schema = Schema()
    print(schema.fetch_data())
    app.run()
