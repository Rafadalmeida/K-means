# K-means
pós graduação data science


Modelo k-means
1. Criar dados aleatórios (data)

2. Definir funções auxiliares

3. Criar Algoritmo

	* Escolher o número de centroides (K) para os nossos dados. 
 		o Pedir input de K clusters ao utilizador.
   
	* Criar função que selecione aleatoriamente x pontos que serão os nossos primeiros centroides.
	
	* Calcular a distância dos restantes pontos aos primeiros centroides escolhidos. 
		o métodos: Euclidean
	
	* Distribuir as observações por cluster conforme as distâncias mínimas aos centroides.
	
	* Recalcular os novos centroides 

	* Recalcular a distância de cada observação aos novos centroides
	
	* Repetir os passos deste o ponto 3, até que nenhuma observação mude o seu cluster. 

4. Plot dos clusters

5. Inserir observação aleatória pelo utilizador e obter o cluster a que pertence

6. Aplicar a um data set publico

7. preencher o ficheiro readme de como funciona e se utiliza o modelo

K means divide os dados em vários clusters e o número de clusters é igual ao valor de k. Se k for igual a 3 então os dados vão ser dividideos em 3 clusters. Cada valor de k é um centoide à volta do qual serão agregados os restantes dados. 

O cálculo da distancia pode ser feito por vários métodos: Euclidean, 
