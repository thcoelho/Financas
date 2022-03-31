# Financas

## Racionalização
Aqui estão contidas funções a fim de se explorar uma carteira teórica de ações brasileiras. Esta não é uma biblioteca a ser utilizada para trading ou com use cases sérios, mas somente um projeto a fim de testar meus conhecimentos acerca da linguagem Python e da funcionalidade de seus módulos.

## Uso
Para se testar as funcionalidades deste projeto, insira o arquivo Financas.py em seu diretório e o importe:

```python
import Financas
```
Para criar uma carteira, alimente a classe Carteira com uma lista de ativos e pesos na carteira para cada ativo, a exemplo:

```python
Ativos = ["ITSA4", "BBAS3", "WEGE3"]
Pesos = [0.3, 0.4, 0.3]
Carteira = Financas.Carteira(Ativos, Pesos)
```
Se nenhuma lista de pesos for passada ao construtor, será assumido que todos os ativos possuem pesos iguais na carteira.
Observação: a vírgula separa os objetos da lista no python, então ao passar os pesos, um peso de 10% para o primeiro ativo é: 0.1

O Objeto carteira possui funções a fim de se obter diversas métricas acerca dos ativos, com mais a serem adicionadas:

```python
# Desvios Padrão
Carteira.Desvios()

# Betas
Carteira.Betas()

# Correlacao entre ativos
Carteira.Correlacao()

# Grafico de evolução dos precos:
Carteira.Grafico(Data_inicial, Data_final)

```

O objeto Carteira guarda o histórico de preços dos ativos em sua propriedade Precos:

```python
# DataFrame com Precos
Carteira.Precos
```


