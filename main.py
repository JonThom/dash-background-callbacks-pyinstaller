import time
import os
from long_callbacks.long_callbacks import register_long_callbacks
import dash
from dash import DiskcacheManager, Input, Output, html


# Diskcache for non-production apps when developing locally
import diskcache
cache = diskcache.Cache("./cache")
background_callback_manager = DiskcacheManager(cache)

app = dash.Dash(__name__, background_callback_manager=background_callback_manager)
app.layout = html.Div(
    [
        html.Div(
            [
                html.P(id="paragraph_id", children=["Button not clicked"]),
                html.Progress(id="progress_bar", value="0"),
            ]
        ),
        html.Button(id="button_id", children="Run Job!"),
        html.Button(id="cancel_button_id", children="Cancel Running Job!"),
    ]
)
register_long_callbacks(app)


if __name__ == "__main__":
    app.run_server(debug=False)

