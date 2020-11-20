import sqlalchemy
from sqlalchemy import create_engine

def get_test_connection():
    db_connect = "mysql+mysqldb://test:1234567@localhost/dc"
    engine = create_engine(db_connect, echo = True)
    return engine

def upload_doc_string_to_mysql(title = None, Path_ = None, Parent_landing_page_path = None, Landing_page_path = None, Repository_path = None, Github_repository_path = None, Short_description = None, Long_description = None, Long_description_html = None, Technical_description = None, Databases_used = None, Technical_databases_used = None, Created_by = None, Maintained_by = None, Maintained_by_backup = None):
    test_con = get_test_connection()

    if title == None:
        raise ValueError("title cannot be None")
    else: 
        con = test_con.connect()
        sql_insert = "insert into post values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(title, Path_, Parent_landing_page_path, Landing_page_path, Repository_path, Github_repository_path, Short_description, Long_description, Long_description_html, Technical_description, Databases_used, Technical_databases_used, Created_by, Maintained_by, Maintained_by_backup)
        sql_update = "on duplicate key update path = '{}', parent_landing_page_path = '{}', landing_page_path = '{}', repository_path = '{}', github_repository_path = '{}', short_description = '{}', long_description = '{}', long_description_html = '{}', technical_description = '{}', databases_used = '{}', technical_databases_used = '{}', created_by = '{}', maintained_by = '{}', maintained_by_backup = '{}'".format(Path_, Parent_landing_page_path, Landing_page_path, Repository_path, Github_repository_path, Short_description, Long_description, Long_description_html, Technical_description, Databases_used, Technical_databases_used, Created_by, Maintained_by, Maintained_by_backup)
        sql_upload = sql_insert + ' ' + sql_update        
        con.execute(sql_upload) 









