"""Modal staging deploy for the Green Leaf Counseling static site.

Serves the current working-tree copy of the site at a stable Modal URL so
edits can be previewed before they go to production (GitHub Pages).

Deploy / re-deploy staging with the current files:

    modal deploy staging.py

Production is separate: pushing to the `main` branch publishes to
https://greenleafcounselingnyc.com via GitHub Pages.
"""

import modal

app = modal.App("greenleaf-staging")

# Bake the current site files into the image. Re-running `modal deploy`
# picks up whatever is in the working tree, so staging always reflects the
# latest local edits. Infra/meta files are excluded.
image = (
    modal.Image.debian_slim()
    .pip_install("fastapi[standard]==0.115.4")
    .add_local_dir(
        ".",
        remote_path="/site",
        ignore=[
            ".git",
            ".git/**",
            ".claude",
            ".claude/**",
            "staging.py",
            "CLAUDE.md",
            "README.md",
        ],
    )
)


@app.function(image=image)
@modal.asgi_app()
def web():
    from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles

    web_app = FastAPI()
    # html=True serves index.html at "/" and resolves directory indexes;
    # the site uses explicit .html links so this matches GitHub Pages.
    web_app.mount("/", StaticFiles(directory="/site", html=True), name="site")
    return web_app
