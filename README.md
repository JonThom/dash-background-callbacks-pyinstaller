# Debug Dash long callbacks

A working example of packaging a Plotly Dash app with long callbacks.
Uses [pyinstaller](https://pyinstaller.org) for packaging, but should work for similar frameworks like cx_freeze. 

The app is based on toy example at https://github.com/plotly/dash/issues/1885#issuecomment-1405490068, with the following changes:

- call `register_long_callbacks(app)` _after_ adding the layout to app
- in `debuglc.spec`, include `./cache` among the 'datas' that are packaged with the app, alongside `long_callbacks.py`
- also moved `long_callbacks.py` into a directory called `long_callbacks`, although this shouldn't matter

## quick start

install dependencies
```shell
poetry install
```

build the app bundle
```shell
poetry run pyinstaller --noconfirm debuglc.spec
```

