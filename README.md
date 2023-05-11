# Relatorio_Automatico
No dia a dia de uma empresa, muitas vezes precisamos mandar relatórios atualizados toda semana. Porém, com Python podemos cuidar disso sem encostar no computador, basta que o mesmo esteja ligado.

Utilizando as bibliotes do Python "pyautogui" e "pyperclip", criei esse programa que toma controle do comportador para executar a tarefa de forma automática.
A tarefa em questão é o tratamento de uma base de dados de compras de produtos, onde a mesma possui informações de fornecedor, valores e quantidades. Pensando em um relatório semanal, pensei no tratamento de dados para o total gasto com os produtos, a quantidade e preço médio por unidade.

A leitura e tratamento de dados foi feita utilizando a biblioteca "pandas".

Para controlar quando esse relatório será realizado, utilizei a biblioteca "datetime" para rodar a aplicação apenas se for sexta-feira.
Por fim, para não precisar rodar o programa monualmente, podemos deixar o mesmo rodando em cloud.
