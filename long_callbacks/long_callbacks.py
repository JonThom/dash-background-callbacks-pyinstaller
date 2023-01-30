import time
import os

import dash
from dash import DiskcacheManager, Input, Output, html

def register_long_callbacks(app):
    @app.callback(
        output=Output("paragraph_id", "children"),
        inputs=Input("button_id", "n_clicks"),
        background=True,
        running=[
            (Output("button_id", "disabled"), True, False),
            (Output("cancel_button_id", "disabled"), False, True),
            (
                Output("paragraph_id", "style"),
                {"visibility": "hidden"},
                {"visibility": "visible"},
            ),
            (
                Output("progress_bar", "style"),
                {"visibility": "visible"},
                {"visibility": "hidden"},
            ),
        ],
        cancel=Input("cancel_button_id", "n_clicks"),
        progress=[Output("progress_bar", "value"), Output("progress_bar", "max")],
        prevent_initial_call=True
    )
    def update_progress(set_progress, n_clicks):
        total = 5
        for i in range(total + 1):
            set_progress((str(i), str(total)))
            time.sleep(1)
    
        return f"Clicked {n_clicks} times"