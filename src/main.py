from sys import stdout
import plotly.graph_objects as go
import random
import pandas as pd

def load_points(file_path):
    """Load points from a CSV file."""
    df_points = pd.read_csv(file_path, sep=';')
    return [tuple(x) for x in df_points.values.tolist()]

def adjust_position(x, y, placed_labels):
    """Adjust the position of the label to avoid overlap."""
    min_dist = 0.3
    while any(abs(y - py) < min_dist and abs(x - px) < min_dist for px, py in placed_labels):
        y -= 0.2
    placed_labels.append((x, y))
    return x, y

def add_point(fig, x, y, color):
    """Add a point to the figure."""
    fig.add_trace(go.Scatter(
        x=[x], y=[y], mode='markers',
        marker=dict(color=color, size=10),
        showlegend=False
    ))

def add_label(fig, x, y, label, color):
    """Add a label to the figure."""
    xAlign = "center"
    yAlign = "top"

    if y < 0:
        yAlign = "bottom"

    fig.add_trace(go.Scatter(
        x=[x], y=[y], text=[f"{label}"],
        mode='text',
        textposition=f"{yAlign} {xAlign}",
        textfont=dict(color=color, size=17),
        showlegend=False
    ))

def add_quadrants(fig):
    """Add quadrants to the figure."""
    fig.add_shape(type="rect", x0=0, x1=-10, y0=0, y1=10, fillcolor="red", opacity=0.1, line=dict(width=0))
    fig.add_shape(type="rect", x0=0, x1=10, y0=0, y1=10, fillcolor="blue", opacity=0.1, line=dict(width=0))
    fig.add_shape(type="rect", x0=0, x1=-10, y0=0, y1=-10, fillcolor="lightgreen", opacity=0.1, line=dict(width=0))
    fig.add_shape(type="rect", x0=0, x1=10, y0=0, y1=-10, fillcolor="purple", opacity=0.1, line=dict(width=0))

def add_axes(fig):
    """Add axes to the figure."""
    fig.add_trace(go.Scatter(
        x=[-10, 10], y=[0, 0], mode='lines', line=dict(color='black', width=2), showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=[0, 0], y=[-10, 10], mode='lines', line=dict(color='black', width=2), showlegend=False
    ))

def add_axis_labels(fig):
    """Add axis labels to the figure."""
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

def create_figure(points):
    """Create the political compass figure."""
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'magenta', 'lime', 'teal', 'navy']
    random.shuffle(colors)

    fig = go.Figure()
    placed_labels = []

    for (x, y, label) in points:
        x_adj, y_adj = adjust_position(x, y, placed_labels)
        color = random.choice(colors)
        add_point(fig, x, y, color)
        add_label(fig, x, y_adj, label, color)

    add_quadrants(fig)
    add_axes(fig)
    add_axis_labels(fig)

    fig.update_layout(
        xaxis=dict(range=[-10, 10], tickmode='linear', tick0=-10, dtick=0.5),
        yaxis=dict(range=[-10, 10], tickmode='linear', tick0=-10, dtick=0.5),
        plot_bgcolor='white',
        title="Buteco Political Compass",
        title_x=0.5,
        template='plotly_white',
    )

    return fig

if __name__ == "__main__":
    points = load_points('src/points.csv')
    fig = create_figure(points)
    fig.show()