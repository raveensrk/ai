# Wiki Methodology Presentation

A [reveal.js](https://revealjs.com/) web slideshow — "Your Wiki Is the Product: a
methodology for structuring shared knowledge between you and your LLM."

All slide content lives in [slides.md](./slides.md). Edit that file to change the
deck; [index.html](./index.html) is just the runtime shell.

## Viewing

The slides are loaded from an external markdown file, which browsers block over
`file://` (CORS). Serve the directory over HTTP instead:

```sh
cd presentations/wiki_methodology
python3 -m http.server 8000
```

Then open <http://localhost:8000/>. Internet access is required the first time
(reveal.js and the mermaid plugin load from the jsDelivr CDN).

Keyboard: `→`/`Space` next · `←` previous · `↓` enter a section's vertical
slides · `Esc` overview · `s` speaker notes · `f` fullscreen.

## Editing slides.md

- `---` on its own line (blank lines around it) starts a new **horizontal** slide.
- `--` starts a **vertical** slide (nested under the current section).
- A line starting with `Note:` begins **speaker notes** (visible in the `s` view).

### Animations

- Stagger bullets in with fragments:

  ```markdown
  - Appears on click <!-- .element: class="fragment fade-up" -->
  ```

- Morph between two adjacent slides by giving both
  `<!-- .slide: data-auto-animate -->` as their first line; reveal.js animates
  matching elements (used for the title/agenda and directory-tree slides).

### Diagrams (mermaid)

Wrap [mermaid](https://mermaid.js.org/) source in a `div.mermaid` with a `pre`
(plain ```` ```mermaid ```` fences are not picked up by the plugin):

```html
<div class="mermaid">
<pre>
flowchart LR
  A --> B
</pre>
</div>
```

Diagrams are themed to Solarized Dark automatically (see the `mermaid` config in
[index.html](./index.html)). Keep one diagram per slide.

### Colors

The theme is Solarized Dark ([theme/solarized_dark.css](./theme/solarized_dark.css)),
layered over reveal's built-in solarized theme. Helper classes for accents:
`sol-yellow`, `sol-orange`, `sol-red`, `sol-magenta`, `sol-violet`, `sol-blue`,
`sol-cyan`, `sol-green`, `sol-muted` — plus `cite` for footnote-style source
lines and `cols` for two-column layouts.

## Citations

Per the repo's citation rule, claims carry inline source links in a
`<p class="cite">…</p>` line on the slide where they are made, and everything is
collected on the final References slides.
