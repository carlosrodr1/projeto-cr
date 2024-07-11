"""Código do projeto de CR para a analise de robustez e resiliência de redes complexas."""

"""Comando para instalar as libs necessárias:"""
        """pip install networkx
           python -m pip install -U pip
           python -m pip install -U matplotlib"""
        

import networkx
import matplotlib.pyplot as plt
import random


class Graph:
    """Classe responsavél por criar e manipular o grafo."""

    def __init__(self):
        """Inicializador da classe Graph."""
        self.__graph_obj = networkx.Graph()  #obj da graph da lib nertworkx

    def __build_graph(self):
        self.__graph_obj.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])  #build dos nós
        self.__graph_obj.add_edges_from([
                                        (1, 3),
                                        (3, 2),
                                        (3, 5),
                                        (2, 5),
                                        (5, 4),
                                        (5, 7),
                                        (5, 6),
                                        (4, 6),
                                        (6, 7),
                                        (6, 8),
                                        (7, 8)
                                        ])  #build das arestas

    def __drop_node(self):
        random_node = random.randrange(1, self.__graph_obj.number_of_nodes())  #sorteia um n aleatório no range da quantidade de nós do grafo
        try:
            print(f"Nó sofrendo ataque: {random_node}")
            self.__graph_obj.remove_node(random_node)  #remove o nó sorteado
        except networkx.exception.NetworkXError:
            pass

    def __calculate_resilience(self, graph):
        cf_resilience = networkx.density(graph)  #calcula a resiliência do grafo
        return print(f'coeficiente resiliência da rede: {cf_resilience}')

    def __calculate_robustness(self, graph):
        try:
            cf_robustness = networkx.minimum_node_cut(graph)  #calcula a robustez do grafo pelo grafo crítico para conexâo dos nós
            clustering = networkx.algorithms.approximation.average_clustering(graph)
        except networkx.exception.NetworkXError:
            print('Ataque crítico: a rede não está mais conectada')
            return False
        return print(f'grafo crítico para manter a rede conectada: {cf_robustness}\ncoeficiente de clusterização da rede: {clustering}')

    def __plot_graph_img(self):
        plt.figure(2)
        networkx.draw_networkx(self.__graph_obj,
                               pos=networkx.spring_layout(self.__graph_obj),
                               with_labels=True)
        plt.show()

    def run(self):
        self.__build_graph()
        self.__plot_graph_img()
        while self.__graph_obj.number_of_nodes() != 0:
            self.__drop_node()
            self.__plot_graph_img()
            self.__calculate_resilience(self.__graph_obj)
            if self.__calculate_robustness(self.__graph_obj) == False:
                break


grafo = Graph()
grafo.run()
