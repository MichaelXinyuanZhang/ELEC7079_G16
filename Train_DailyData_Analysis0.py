for symbol in df.columns.levels[0]:
    # 创建一个图形对象和四个子图对象
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(15, 10), sharex=True)

    # 在第一个子图上绘制收盘价和移动平均线
    ax1.plot(df.index, df[(symbol, "close_px")], label="Close Price")
    ax1.plot(df.index, df[(symbol, "ma")], label="Moving Average")
    # 设置标题、图例、网格线和纵轴标签
    ax1.set_title(symbol)
    ax1.legend(loc="upper left")
    ax1.grid()
    ax1.set_ylabel("Price")

    # 在第二个子图上绘制相对强弱指数
    ax2.plot(df.index, df[(symbol, "rsi")], label="RSI")
    # 设置图例、网格线和纵轴标签
    ax2.legend(loc="upper left")
    ax2.grid()
    ax2.set_ylabel("RSI")

    # 在第三个子图上绘制随机指标
    ax3.plot(df.index, df[(symbol, "k")], label="K")
    ax3.plot(df.index, df[(symbol, "d")], label="D")
    # 设置图例、网格线和纵轴标签
    ax3.legend(loc="upper left")
    ax3.grid()
    ax3.set_ylabel("KDJ")

    # 在第四个子图上绘制指数平滑异同平均线和成交量
    ax4.plot(df.index, df[(symbol, "macd")], label="MACD")
    ax4.plot(df.index, df[(symbol, "macdsignal")], label="MACD Signal")
    ax4.bar(df.index, df[(symbol, "macdhist")], label="MACD Histogram", width=0.5)
    # 创建一个次坐标轴，用于显示成交量
    ax5 = ax4.twinx()
    ax5.bar(df.index, df[(symbol, "volume")], label="Volume", color="gray", alpha=0.3, width=0.5)
    # 设置图例、网格线和纵轴标签
    ax4.legend(loc="upper left")
    ax4.grid()
    ax4.set_ylabel("MACD")
    ax5.set_ylabel("Volume")

    # 调整子图之间的间距
    fig.tight_layout()

    fig.savefig(f"/content/drive/MyDrive/Colab Notebooks/investment/{symbol}.png")