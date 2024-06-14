import os
from pathlib import Path
from typing import Annotated, Optional

import typer
import yaspin

from classes.face import FaceDetector

from utils.inquiries import should_delete
from utils.spinner import custom_spinner
from utils.text import cstring, printc

app = typer.Typer()


@app.command(
    short_help="Detects faces in a video, drawing red rectangles around them and saving to a new file.",
    name="detect",
)
def detect(
    input: Annotated[
        Path,
        typer.Argument(
            help="The input file path",
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
        ),
    ],
    output: Annotated[
        Path,
        typer.Argument(
            help="The output file path.",
            writable=True,
            readable=False,
            resolve_path=True,
        ),
    ],
):
    if output.exists():
        if should_delete(output.name):
            return printc("&r[&c!&r]&c Aborted.")

        try:
            os.remove(output)
        except Exception as e:
            return printc(
                f"&r[&c!&r]&c Unable to delete the file &d{output.name}&c. {e}"
            )

    try:
        with yaspin.yaspin(
            custom_spinner, text=cstring("&eDetecting faces in video...")
        ) as spinner:
            try:
                face_detector = FaceDetector()

                face_detector.detect_video(
                    input_path=input,
                    output_path=output,
                )

                spinner.text = cstring(
                    f"&aFaces detected successfully! Saved to &d{output.name}&a."
                )
                spinner.ok(cstring("&r[&a✔&r]"))
            except Exception as e:
                spinner.text = cstring(f"&cError while detecting faces: {e}")
                spinner.fail(cstring(f"&r[&c!&r]&c {e}"))
    except KeyboardInterrupt:
        printc("&r[&c!&r]&c Aborted.")
    except Exception as e:
        printc(f"&r[&c!&r]&c {e}")
