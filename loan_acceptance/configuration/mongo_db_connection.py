from loan_acceptance.exceptions import LoanAcceptanceException
from loan_acceptance.logger import logging
import os
import sys
from loan_acceptance.coonstants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo # type: ignore[import]
import certifi 

ca = certifi.where()

class MongoDBClient:
    """
    Class Name : export_data_into_feature_store
    Description : This method exports the dataframe from mongodb feature store as dataframe

    Output : connection to mongodb database
    On Failure : Raise an Exception
    """
    clinet = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.clinet is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.clinet = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.clinet = MongoDBClient.clinet
            self.database = self.clinet[database_name]
            self.database_name = database_name
            logging.info(f"Connection to MongoDB database: {database_name} is successful.")
        except Exception as e:
            raise LoanAcceptanceException(e, sys)
        