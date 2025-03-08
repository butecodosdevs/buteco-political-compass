from sys import stdout
import plotly.graph_objects as go
import random

pontos = [
    (-0.36, -0.38, 'CWBY'), (3.75, -2.72, 'Vihugo'), (1.88, -0.15, 'Eder'),
    (-2.5, -3.6, 'Kalango'), (-2.38, -0.77, 'Aninha'), (-0.88, -0.72, 'Sonee'),
    (-5.25, -3.23, 'Noah'), (-0.25, -2.97, 'Funnie'), (-3.63, -4.05, 'Bruno'),
    (4.25, -1.74, 'Miranda'), (-4.13, -3.85, 'Mango'), (5, -4.67, 'Pietro'),
    (-4.88, -3.59, 'João'), (6.88, -2.92, 'Sebas'), (-8.5, -6.62, 'Navegantes'),
    (0.38, -1.18, 'Cris'), (3.0, -1.59, 'Mucilon'), (6.75, -0.92, 'Gabiest'),
    (2.0, -3.28, 'Gio'), (-4.75, -3.85, 'Wagner'), (-6.75, -5.49, 'Jamal'), 
    (-8.63, -5.69, 'José'), (-3.13, -0.62, 'Dev Pai'), (-6.25, -3.59, 'Felurian'),
    (-2.0, -2.67, 'Henrique'), (3.63, 1.23, 'Rina'), (-1.13, 1.95, 'Deveras'),
    (-1.0, -0.21, 'Toninho'), (-4.38, -2.56, 'Montanha'), (0.63, 0.82, 'Math'),
    (-3.88, -2.56, 'Log'),  (-5.5, -5.38, 'Folle'), (7.63, -2.26, '[N]amless'), 
    (-8.63, -6.62, 'moloco'), (-7.38, -6.1, 'Professor'), (-3.75, -4.62, 'Joke'), 
    (-7.0, -3.85, 'Bloise'),

    (-4.25, 8.15, 'Hitler (Miranda)'),
    (3.5, 1.23, 'GPT 4o, mix - Fascist'),
    (-4.38,6.87, 'Kim Jong Un (mango)'),
    (4.13, 2.56, 'Ianky (suspeito)') # removido por suspeita de ter feito o teste a la caralha
]

colors = ['red', 'blue', 'green', 'purple', 'orange', 'magenta', 'lime', 'teal', 'navy']
random.shuffle(colors)

fig = go.Figure()

placed_labels = []

def adjust_position(x, y):
    print(f"y: {y}")
    min_dist = 0.3
    while any(abs(y - py) < min_dist and abs(x - px) < min_dist for px, py in placed_labels):
        y -= 0.2
    placed_labels.append((x, y))
    print(f"end y: {y}")
    return x, y

for (x, y, label) in pontos:
    x_adj, y_adj = adjust_position(x, y)
    color = random.choice(colors)

    fig.add_trace(go.Scatter(
        x=[x], y=[y], mode='markers',
        marker=dict(color=color, size=10),
        showlegend=False
    ))

    xAlign = "center"
    yAlign = "top"
    if y_adj < y:
        yAlign = "bottom"

    if yAlign == "top":
        y += 0.1
    else:
        y -= 0.1


    fig.add_trace(go.Scatter(
        x=[x], y=[y], text=[f"{label}"],
        mode='text',
        textposition=f"{yAlign} {xAlign}",
        textfont=dict(color=color, size=17),
        showlegend=False
    ))

fig.add_shape(type="rect", x0=0, x1=-10, y0=0, y1=10, fillcolor="red", opacity=0.1, line=dict(width=0))
fig.add_shape(type="rect", x0=0, x1=10, y0=0, y1=10, fillcolor="blue", opacity=0.1, line=dict(width=0))
fig.add_shape(type="rect", x0=0, x1=-10, y0=0, y1=-10, fillcolor="lightgreen", opacity=0.1, line=dict(width=0))
fig.add_shape(type="rect", x0=0, x1=10, y0=0, y1=-10, fillcolor="purple", opacity=0.1, line=dict(width=0))

fig.add_trace(go.Scatter(
    x=[-10, 10], y=[0, 0], mode='lines', line=dict(color='black', width=2), showlegend=False
))
fig.add_trace(go.Scatter(
    x=[0, 0], y=[-10, 10], mode='lines', line=dict(color='black', width=2), showlegend=False
))

fig.add_trace(go.Scatter(
    x=[10], y=[0], text=["RIGHT"], textposition='middle right', mode='text', showlegend=False
))
fig.add_trace(go.Scatter(
    x=[-10], y=[0], text=["LEFT"], textposition='middle left', mode='text', showlegend=False
))
fig.add_trace(go.Scatter(
    x=[0], y=[10], text=["AUTHORITARIAN"], textposition='top center', mode='text', showlegend=False
))
fig.add_trace(go.Scatter(
    x=[0], y=[-10], text=["LIBERTARIAN"], textposition='bottom center', mode='text', showlegend=False
))

fig.update_layout(
    xaxis=dict(range=[-10, 10], tickmode='linear', tick0=-10, dtick=0.5),
    yaxis=dict(range=[-10, 10], tickmode='linear', tick0=-10, dtick=0.5),
    plot_bgcolor='white',
    title="Buteco Political Compass",
    title_x=0.5,
    template='plotly_white',
)

fig.show()

