import matplotlib.pyplot as plot


def generate_piec_chart():
    labels = ['A', 'B', 'C']
    values = [35, 38, 80]

    fig, ax = plot.subplots()
    ax.pie(values, labels=labels)
    plot.savefig('pie.png')
    plot.close()