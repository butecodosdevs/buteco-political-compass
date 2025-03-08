from sys import stdout
import plotly.graph_objects as go
import random
import pandas as pd

df_points = pd.read_csv('points.csv', sep=';')
pontos = [tuple(x) for x in df_points.values.tolist()]

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
