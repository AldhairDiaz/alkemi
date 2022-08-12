class Data_Processing:
    import db   
    from sqlalchemy import Column, Integer, Float, Date, String, VARCHAR
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import csv
    import pandas as pd
    
    
    db.Base.metadata.create_all(db.engine)
    file_name = 'client_db.csv'
    df = pd.read_csv(file_name)
    df.to_sql(con=db.engine, index_label='id', name=cdb1.__tablename__, if_exists='replace')