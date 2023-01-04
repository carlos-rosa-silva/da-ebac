with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda', ci=None, palette='pastel')
  grafico.set(title='Preço Gasolina', xlabel='Dia', ylabel='Vanda');
  grafico.get_figure().savefig(f'gasolina.png')
