import typer

from commands.detect import app as detect

app = typer.Typer(
    help="A CLI to detect faces in videos and images.", name="face-detector"
)

app.registered_commands += detect.registered_commands

if __name__ == "__main__":
    app()
