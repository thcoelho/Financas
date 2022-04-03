import pandas as pd
import yfinance as yf
import numpy as np


def Ibovespa():
    """
    Retorna Dataframe com as empresas presentes no índice IBOVESPA
    """
    url = "https://pt.wikipedia.org/wiki/Lista_de_companhias_citadas_no_Ibovespa"
    df = pd.read_html(url)[0]
    df.set_index("Código", inplace=True)
    return df


class Carteira:
    def __init__(self, Ativos, Pesos=None):
        self.Ativos = [Ativo + ".SA" for Ativo in Ativos]
        self.Pesos = [(1 / len(Ativos)) for i in Ativos] if Pesos is None else Pesos
        Carteira.Coletar_Precos(self)

    def Coletar_Precos(self):
        """
        Coletar Precos dos Ativos, exportar para DataFrame e salvar em propriedade no objeto carteira. Salva o histórico de preços e o objeto 
        yfinance.ticker como  atributos.
        """
        df = pd.DataFrame()

        # Criar Lista contendo os objetos Yfinance.Tickers para utilização em outras funções do módulo
        tickers = [yf.Ticker(f"{ticker}") for ticker in self.Ativos]

        for ticker in tickers:
            df[ticker] = ticker.history(period="max")["Close"]

        df.columns = self.Ativos
        self.Precos = df
        self.Tickers = tickers

    def Desvios(self):
        """
        Calcula o desvio padrão da carteira
        """
        print(" Os desvios padrão são:")
        print(self.Precos.std())

    def Correlacao(self):
        """
        Calcula a correlação entre os ativos da carteira
        """
        print("A Matriz de correlação entre os ativos é:")
        print(self.Precos.corr())

    def Betas(self):
        """
        Coleta o Beta de cada ativo
        """
        Betas = pd.DataFrame()
        Betas["Papel"] = self.Ativos
        Betas["Beta"] = [ticker.info.get("beta") for ticker in self.Tickers]

        print("Os betas dos ativos são:")
        print(Betas)

    def Grafico(self, inicio=None, final=None):
        """
        Gráfico com a evolução dos ativos selecionados. Se nada for passado para as datas, serão utilizados os dados
        mais recentes (no caso do final) ou mais antigos (no caso do inicio). Formato das datas:
        Ex: Grafico("2010", "2020")
        """
        inicio = self.Precos.index[0] if inicio is None else inicio
        final = self.Precos.index[-1] if final is None else final

        self.Precos.loc[inicio:final, :].plot()

    def Retornos(self, inicio=None, final=None):
        """
        Calcula os retornos da carteira de acordo com o recorte temporal selecionado
        """
        inicio = self.Precos.index[0] if inicio is None else inicio
        final = self.Precos.index[-1] if final is None else final

        Retornos = self.Precos.loc[inicio:final, :].pct_change()
        Retornos_Com_Pesos = Retornos.dot(np.array(self.Pesos))
        Retornos_Acumulados = (1 + Retornos_Com_Pesos).cumprod()
        Retorno_Total = (Retornos_Acumulados[-1] - 1) * 100
        print(f"{Retorno_Total}%")

    # TODO def Modigliani(self):

    # TODO def Sharpe(self):
