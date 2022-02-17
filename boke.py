import bokeh
import sqlite3

from bokeh.plotting import figure, output_file, show

output_file("output.html")
lista = ["asdf", 'wer', 'awe']
toppi = [12, 23, 15]

p = figure(x_range=lista)
p.vbar(x=lista, top=toppi, width=0.5)
show(p)