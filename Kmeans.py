import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)#random seed

#Defenir a distância euclidiana de dois vectores x1 e x2
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))

#implementar o K-means class
class KMeans():

    def __init__(self, K=5, max_iters=100, plot_steps=False): #K: n clusters / max_iters: iterações máximas / #plot_steps serve para a função mais à frente que vai plotar o gráfico
        self.K = K
        self.max_iters = max_iters
        self.plot_steps = plot_steps

        # Lista de indices amostrais para cada cluster
        self.clusters = [[] for _ in range(self.K)] #criar as empty classes e os centroids / "self.clusters [] -> empty list " Ou seja para cada cluster nós iniciamos uma lista vazia 
        
        # the centers (mean feature vector) for each cluster
        self.centroids = []

        # Método preditivo 
    def predict(self, X): 
        self.X = X
        self.n_samples, self.n_features = X.shape
        
        # Inicializar - atribuir k centroids aleatórios
        random_sample_idxs = np.random.choice(self.n_samples, self.K, replace=False)
        self.centroids = [self.X[idx] for idx in random_sample_idxs]

        # Optimizar os clusters
        for _ in range(self.max_iters):
        
            # Atribuir as amostras aos centroids mais próximos (Criar clusters)
            self.clusters = self._create_clusters(self.centroids)
            
            if self.plot_steps:
                self.plot() #faz o plot de cada iteração que fez

            # Calcular os novos centroides dos clusters / substitui os cluster antigos pelos novos, mas guarda a informação dos antigos para comparar com os novos e passa ao seguinte if
            centroids_old = self.centroids
            self.centroids = self._get_centroids(self.clusters)
            
            # Verificar se os cluster mudaram
            if self._is_converged(centroids_old, self.centroids):
                break # se os clusters novos forem iguais ao anterior faz break. Para a iteração e faz o resultado final.

            if self.plot_steps:
                self.plot() #plot final dos ultimos clusters determinados

        # Atribui cada amostra ao seu cluster 
        return self._get_cluster_labels(self.clusters) 


    def _get_cluster_labels(self, clusters):
        # Cada amostra irá ter a label do cluster que lhe foi atribuido
        labels = np.empty(self.n_samples) 
    
        for cluster_idx, cluster in enumerate(clusters):
            for sample_index in cluster:
                labels[sample_index] = cluster_idx
        return labels

    def _create_clusters(self, centroids):
        # atribuir as amostra aos centroides mais próximos para criar clusters
        clusters = [[] for _ in range(self.K)]
        for idx, sample in enumerate(self.X):
            centroid_idx = self._closest_centroid(sample, centroids)
            clusters[centroid_idx].append(idx)
        return clusters

    def _closest_centroid(self, sample, centroids):
        # Distância da amostra atual a cada centroide utilizando o calculo da distância euclediana
        distances = [euclidean_distance(sample, point) for point in centroids]
        closest_index = np.argmin(distances)
        return closest_index

    def _get_centroids(self, clusters):
        # Atribuir o valor médio de cada cluster aos centroids 
        centroids = np.zeros((self.K, self.n_features))
        for cluster_idx, cluster in enumerate(clusters):
            cluster_mean = np.mean(self.X[cluster], axis=0) 
            centroids[cluster_idx] = cluster_mean
        return centroids

    def _is_converged(self, centroids_old, centroids):
        # Distância entre cada centroide antigo e o novo centroide, para todos os centroides. 
        distances = [euclidean_distance(centroids_old[i], centroids[i]) for i in range(self.K)]
        return sum(distances) == 0 #se a distância é igual a zero significa que o novo centroide é igual ao último calculado. 

#Definições do grágico. 
    def plot(self):
        fig, ax = plt.subplots(figsize=(12, 8))

        for i, index in enumerate(self.clusters):
            point = self.X[index].T
            ax.scatter(*point)

        for point in self.centroids:
            ax.scatter(*point, marker="x", color='black', linewidth=2)

        plt.show()
