from db_app import DbApp
from abc import ABC


class FetchAccounts(ABC):

    @staticmethod
    def fetch():
        index_accounts_list = DbApp.fetch_accounts_in_db()
        return index_accounts_list