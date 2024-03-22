from ui.console import start
from application.controller import Controller
from domain.person import Patient
from infrastructure.repositories import *

if __name__ == "__main__":
    controller = Controller(Hospital([Department("dep1", "dis1", 13, [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                             Patient("David", "Maria", "5020714225891", "covid"),
                                             Patient("Alex", "Stefan", "5020714225892", "tuberculosis")]),
                     Department("dep2", "dis2", 10,  [Patient("Marin", "Chad", "5020714225893", "covid"),
                                             Patient("Raul", "Marc", "5020714225894", "covid"),
                                             Patient("Paul", "Apostol", "5020714225895", "covid"),
                                             Patient("Tudor", "Lung", "5020714225896", "sida"),
                                             Patient("Anca", "Serban", "5020714225897", "flu")]),
                     Department("dep3", "dis3", 20, [Patient("Nicu", "Alb", "5020714225898", "cancer"),
                                             Patient("Eugenia", "Nour", "5020714225899", "covid"),
                                             Patient("Sandra", "Dinu", "5020714225805", "covid"),
                                             Patient("Costel", "Virgil", "5020714225815", "malaria"),
                                             Patient("Stefan", "Mircea", "5020714225825", "covid"),
                                             Patient("Anton", "Baltazar", "5020714225835", "hypertension"),
                                             Patient("Cristi", "Chin", "5020714225845", "cancer")]),
                     Department("dep4", "dis4", 5, [Patient("Marcel", "Nica", "5020214225855", "parkinson"),
                                            Patient("Brian", "Maier", "5020114225865", "covid")])]))
    start(controller)
