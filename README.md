# Green Leaf Counseling — website

Static HTML site for Green Leaf Counseling NYC. No build step; the `.html`
files are served directly.

## Editing

Edit the `.html` files directly. Images live alongside them in the repo root.

## Staging preview (Modal)

Preview changes at a Modal URL **before** they go live:

```sh
modal deploy staging.py
```

This publishes the current working-tree copy of the site to
**https://zl2799--greenleaf-staging-web.modal.run** — re-run it after each
round of edits to refresh the preview.

## Production (GitHub Pages)

Pushing to the `main` branch publishes to
**https://greenleafcounselingnyc.com** via GitHub Pages. Always confirm the
change looks right on staging first.
