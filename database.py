from sqlalchemy import create_engine, text
import pymysql
import json

#Link especifico a Aiven


connection_string =("mysql://avnadmin:AVNS_5g2Um49Zo1pu6CQWE_S@aio-moviesv2-aio-movies.c.aivencloud.com:13633/newdatabaseformysql?ssl_mode=REQUIRED"
)

#connect args tiene el certificado

engine = create_engine(connection_string,
                       connect_args={
                           'ssl': {
                               'sslmode': 'REQUIRED',
                               'ssl_ca': "/CERTIFICADOSSL/ca.pem"
                           }
                       })


def load_users_from_db():
   
   with engine.connect() as conn:
    result = conn.execute(text("select * from users"))

    users = []
    for row in result.all():
        users.append(row._mapping)
    print(users)    
    return users


load_users_from_db()


def add_aplication_to_db(data):
    with engine.connect() as conn:
        query = text(
            f"INSERT INTO APPLICATIONS(user, email, linkedin_url) VALUES (:user, :email, :linkedin_url)"
        )

        conn.execute(
            query,
            {
                
                "user": data["user"],
                "email": data["email"],
                "linkedin_url": data["linkedin_url"]
            },
        )
        conn.commit()