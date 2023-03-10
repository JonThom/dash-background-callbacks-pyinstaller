# Dash background callbacks with pyinstaller

A working example of packaging a Plotly Dash app with background callbacks using [PyInstaller](https://pyinstaller.org).
Tested on macOS, should work cross-platform.
Based on toy example at https://github.com/plotly/dash/issues/1885#issuecomment-1405490068.

## quick start

`git clone` the github repo and `cd` into the project directory. Then

create and activate a virtual environment
```shell
python3 -m venv .venv
source .venv/bin/activate
```

install the dependencies
```shell
pip install -r requirements.txt

```

Make a `.spec` specification file for the build.
See the [PyInstaller docs](https://pyinstaller.org/en/stable/usage.html) for options.

```shell
pyinstaller main.py
```

in the new `main.spec` file, add the following to the `datas` in `Analysis`
```{r}
a = Analysis(
    ...,
    datas=[
        ('long_callbacks', 'long_callbacks'),
        ('cache', 'cache')
    ],
    ...
)
```

build the app bundle
```shell
pyinstaller --noconfirm main.spec
```

run the app by running the executable or app bundle in the `dist` directory
(depends on OS and build specs)

```shell
# e.g., on macOS
./dist/main/main
```
