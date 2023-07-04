import yfinance as yf
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *


def get_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data


def plot_candlestick(data, title):
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])])
    fig.update_layout(title=title,
                      xaxis_rangeslider_visible=False,
                      yaxis=dict(tickformat=".0f"))
    fig.show()


def plot_change(bitcoin_change, ethereum_change):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(bitcoin_change, label='Bitcoin Değişim', color='blue')
    ax.plot(ethereum_change, label='Ethereum Değişim', color='red')
    ax.set_title('Bitcoin ve Ethereum Yüzde Değişimleri')
    ax.legend()

    return fig


def show_graph():
    start_date = entry1.get()
    end_date = entry2.get()

    bitcoin_data = get_data('BTC-USD', start_date, end_date)
    ethereum_data = get_data('ETH-USD', start_date, end_date)

    bitcoin_change = bitcoin_data['Close'].pct_change()
    ethereum_change = ethereum_data['Close'].pct_change()

    plot_candlestick(bitcoin_data, 'Bitcoin Fiyatları')
    plot_candlestick(ethereum_data, 'Ethereum Fiyatları')

    fig = plot_change(bitcoin_change, ethereum_change)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()


root = Tk()

label1 = Label(root, text="Başlangıç Tarihi (YYYY-MM-DD)")
label1.pack()

entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text="Bitiş Tarihi (YYYY-MM-DD)")
label2.pack()

entry2 = Entry(root)
entry2.pack()

button = Button(root, text="Grafikleri Göster", command=show_graph)
button.pack()

root.mainloop()
