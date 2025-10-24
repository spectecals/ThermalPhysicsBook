import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

# Only needed in Jupyter for live sliders
import ipywidgets as widgets
from IPython.display import display
import anywidget

from pathlib import Path

lw = 1.5
plt.rcParams['lines.linewidth'] = lw
plt.rcParams['patch.linewidth'] = lw
plt.rcParams['font.size'] = 14
plt.rcParams['figure.figsize'] = (5, 4)


def interactive_curve(model, x, param_specs, title="", x_label="x", y_label="y"):
    """
    Build a Plotly FigureWidget with ipywidgets sliders for arbitrary parameters. Valid for one-dimensional inputs
    and outputs.

    model(x, **params) -> y: your function
    x: np.ndarray of x values
    param_specs: dict like
        {
          "T": {"init": 300, "min": 200, "max": 600, "step": 5},
          "nR": {"init": 8.314, "min": 1, "max": 20, "step": 0.1},
        }
    """

    sliders = {}
    for variable, subdict in param_specs.items():
        sliders[variable] = widgets.FloatSlider(
            value=subdict["init"],
            min=subdict["min"],
            max=subdict["max"],
            step=subdict.get("step", 0.1),
            description=variable,
            continuous_update=True
        )

    # Returns the kwargs of the model provided when called for plotting.
    def _current_params():
        return {name: w.value for name, w in sliders.items()}

    # Generate the curve with the model and kwargs supplied through param_specs arguments.
    y = model(x, **_current_params())
    fig = go.FigureWidget(go.Scatter(x=x, y=y, mode="lines"))
    # Apply layout settings.
    fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)

    # Update the graph whenever the slider is adjusted.
    def _update(_=None):
        fig.data[0].y = model(x, **_current_params())

    for w in sliders.values():
        w.observe(_update, names="value")

    controls = widgets.VBox(list(sliders.values()))
    display(controls, fig)

    return fig, controls
