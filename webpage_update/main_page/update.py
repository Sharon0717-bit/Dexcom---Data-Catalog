from jinja2 import Environment, FileSystemLoader
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

def get_table():
    db_connect = "mysql+mysqldb://test:1234567@localhost/dc"
    engine = create_engine(db_connect, echo = True)
    sql = "select * from post"
    df = pd.read_sql(sql, engine)
    df['cid'] = df.title
    df['cid_'] = df['cid'].apply(lambda x: '{}{}'.format('#', x))
    df.title = df.title.replace({'_':" "}, regex = True)
    df.title = df.title.str.title()
    return df

def generate_html (posts):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('template.html')
    with open("result.html", "w+") as f:
        html_content = template.render(posts = posts)
        f.write(html_content)

if __name__ == '__main__':
    df = get_table()
    posts = df.to_dict(orient = 'records')
    generate_html(posts)


# def generate_html (n, posts):
#     env = Environment(loader=FileSystemLoader('./'))
#     template = env.get_template('template.html')
#     DF = divide_df()
#     A = range(len(DF))
#     with open("result{}.html".format(n), "w+") as f:
#         html_content = template.render(posts = posts, A = A)
#         f.write(html_content)

# def divide_df():
#     DF = []
#     df = get_table()
#     rnum = np.arange(0, len(df), 1)
#     for i in range(2):
#         indices = rnum[2*i : 2*i +2]
#         DF.append(df.iloc[indices])
#     return DF

# if __name__ == '__main__':
#     df = get_table()
#     DF = divide_df()
#     POSTS = []
#     for i in range(len(DF)):
#         posts = DF[i].to_dict(orient = 'records')
#         POSTS.append(posts)
#     for j, POST in enumerate(POSTS):
#         generate_html(j, POST)