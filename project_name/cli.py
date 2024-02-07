from tkinter import *  # noqa: F403
from base import browser, app, initialize, start_snipe_thread, stop_snipe

"""CLI interface for project_name project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""


def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m project_name` and `$ project_name `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    print("This will do something")

    # Create window object

    # Open Browser Button
    submit_btn = Button(app, text='Open Browser', width=12, command=initialize)
    submit_btn.grid(row=1, column=0, pady=20, padx=20)

    # Close Browser Button
    submit_btn = Button(app, text='Close Browser', width=12, command=browser.close_browser)
    submit_btn.grid(row=1, column=1, pady=20, padx=20)

    # Start Button
    submit_btn = Button(app, text='Start', width=12, command=start_snipe_thread)
    submit_btn.grid(row=2, column=0, pady=20, padx=20)

    # Stop Button
    submit_btn = Button(app, text='Stop', width=12, command=stop_snipe)
    submit_btn.grid(row=2, column=1, pady=20, padx=20)

    app.title('RTX Bot')
    app.geometry('270x130')

    # Start program
    app.mainloop()
