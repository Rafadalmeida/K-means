# Trabalho Algoritmo K-means 

Pós graduação em Data Science and Business Inteligence

Florbela Amaral,
Pedro Fernandes,
Rafael Almeida,

Exploração de um algoritmo K-means

K-means é um método de clustering que permite dividir o número de observações da nossa amostra em K-clusters onde cada observação pertence ao grupo mais próximo da média.

O algoritmo atribui k centroides aleatórios, otimiza os K centroides: calcula distâncias entre pontos com o objetivo de as minimizar e determinar o centoide de cada cluster.
Ao mesmo tempo, ele atribui cada amostra ao cluster correspondente ao longo de cada iteração.

Estruta do algoritmo 
1. Importar as bibliotecas
2. Defenir a random seed 
3. Aplicar a função da distância euclidiana
4. Implementar o K-means class
5. Defenir o K e o número de iterações máximas
6. Criar uma lista vazia para cada cluster
7. Criar uma lista vazia para o centro de cada cluster
8. Aplicar o método preditivo 
9. Atribuição aleatória de k centroids pelo algoritmo 
10. Optimizar os clusters
11. Atribuir as amostras aos centroids mais próximos (Criar clusters)
12. Guarda info do plot da primeira iteração e seguintes
13. Recalcula os novos centroides dos clusters e substitui os cluster antigos pelos novos. Guarda a informação do antigo cluster para comparar com os novo
14. Verificar se os cluster mudaram
15. Se os clusters novos forem iguais ao anterior faz break. Para a iteração e faz o resultado final
16. Plot final dos ultimos clusters determinados
17. Atribui cada amostra ao seu cluster 
18. Cada amostra irá ter a label do cluster que lhe foi atribuido
19. Atribuir as amostra aos centroides mais próximos para criar clusters
20. Distância da amostra atual a cada centroide utilizando o cálculo da distância euclediana
21. Atribuir o valor médio de cada cluster aos centroides
22. Distância entre cada centroide antigo e o novo centroide, para todos os centroides
23. Se a distância é igual a zero significa que o novo centroide é igual ao último calculado, o algoritmo faz break e obtemos a posição final dos centroides. 
23. Definir o gráfico a plotar





