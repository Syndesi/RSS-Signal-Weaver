from __future__ import annotations

import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.output.append("hi :D")
    return


@app.cell
def _():
    import sys
    #sys.path.append("/app/src")
    sys.path
    return


@app.cell
def _():
    from rsssignalweaver.type import RssFeed

    feed = RssFeed("test", "url2")
    feed
    return


if __name__ == "__main__":
    app.run()
