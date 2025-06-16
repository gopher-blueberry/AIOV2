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











    #enseñando resultados con print y tipos para confirmar que la conexión a la base de datos de ha hecho
"""print(type(result))
    result_all = result.all()
    print("type(result.all())", type(result_all))
    print("result.all():", result_all)
    first_result = result_all[0]
    print("type(first_result):",type(result_all[0]))
    
    first_result_dict = result_all[0]._asdict()
    print("type(first_result_dict):",type(first_result_dict)) """