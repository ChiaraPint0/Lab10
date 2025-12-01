from database.dao import DAO
import networkx as nx
from model import hub

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        self._grafo = nx.Graph()
        lista_hub = DAO.get_all_hub()

        self._dizionario_hub = {}
        for hub in lista_hub:
            self._dizionario_hub[hub.id] = hub

        self._grafo.add_nodes_from(lista_hub)
        self._edges = DAO.get_all_tratte()
        for tratta in self._edges:
            if tratta.media_valore_merce >= threshold:
                hub1 = self._dizionario_hub[tratta.id_hub_origine]
                hub2 = self._dizionario_hub[tratta.id_hub_destinazione]
                self._grafo.add_edge(hub1, hub2, weight= tratta.media_valore_merce)

        return self._grafo
        # TODO

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        return self._grafo.number_of_edges()
        # TODO

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return self._grafo.number_of_nodes()
        # TODO

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        return self._grafo.edges(data = True)
        # TODO

