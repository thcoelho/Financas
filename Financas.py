import pandas as pd
import yfinance as yf

def Ibovespa():
    """
    Retorno Dataframe com as empresas presentes no índice IBOVESPA
    """
    url = "https://pt.wikipedia.org/wiki/Lista_de_companhias_citadas_no_Ibovespa"
    df = pd.read_html(url)[0]
    df.set_index("Código", inplace=True)
    return df

class Carteira:
    
    def __init__(self, Ativos):
        self.Ativos = [Ativo + ".SA" for Ativo in Ativos]
        Carteira.Coletar_Precos(self)
        # TODO self.Pesos

    def Coletar_Precos(self):
        """
        Coletar Precos dos Ativos, exportar para DataFrame e salvar em propriedade no objeto carteira. Também cria objeto Ticker do módulo yfinance para cada Papel
        """
        df = pd.DataFrame()

        # Criar Lista contendo os objetos Yfinance.Tickers para utilização em outras funções do módulo
        tickers = [yf.Ticker(f"{ticker}") for ticker in self.Ativos]

        for ticker in tickers:
            df[ticker] = ticker.history()["Close"]

        df.columns = self.Ativos
        self.Precos = df
        self.Tickers = tickers
    
    def Desvios(self):
        """ 
        Função para calcular rapidamente o desvio padrão de ativos de uma carteria teórica
        """
        print(" Os desvios padrão são:")
        print(self.Precos.std())
    
    def Correlacao(self):
        """
        Calcular a correlação entre os ativos de uma carteira teórica
        """
        print("A Matriz de correlação entre os ativos é:")
        print(self.Precos.corr())
    
    def Betas(self):
        """
        Coletar o Beta de cada ativo
        """
        Betas = pd.DataFrame()
        Betas["Papel"] = self.Ativos
        Betas["Beta"] = [ticker.info.get("beta") for ticker in self.Tickers]

        print("Os betas dos ativos são:")
        print(Betas)

    # TODO def Modigliani(self):

    # TODO def Sharpe(self):
        


