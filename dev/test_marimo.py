import marimo

__generated_with = "0.14.0"
app = marimo.App(width="medium")


@app.cell
def _():
    print("hello world")
    return


@app.cell
def _():
    a = 123
    print(a)
    return (a,)


@app.cell
def _():
    b = 2
    print(b)
    return (b,)


@app.cell
def _(a, b):
    c = a + b  # E226 fixed: added whitespace around operator
    print(c)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
