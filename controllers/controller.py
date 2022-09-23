from views.menu import MenuView
from views.view import View
from views.error import ErrorView
from views.reports import ReportsView
from models.database import Database


class Controller:
    players_list = []
    tournaments_list = []

    def __init__(self):
        self.menu_view = MenuView()
        self.error_view = ErrorView()
        self.view = View()
        self.reports_view = ReportsView()
        self.db = Database()
