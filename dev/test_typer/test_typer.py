# test_typer.py
import typer

app = typer.Typer(name="demo")

@app.command()
def hello_world(name):
    """Say hello"""
    print(f"hello {name}!")

@app.command()
def goodbye_world(name):
    """Say goodbye"""
    print(f"goodbye {name}!")

if __name__ == "__main__":
    app()
