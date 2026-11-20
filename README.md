# Nerima Brenda, Interior and Landscape Design Portfolio

A warm-minimal static portfolio for Nerima Brenda of Neri Creations & Interiors, an interior designer and landscape design graduate in Kampala. The site presents five measured 3D room studies, field photographs, client mood charts and her CV.

**Live site:** https://brendabritney2-prog.github.io/nerima-brenda-portfolio/

## Structure

- `build.py`: static site generator (project data, page templates, sitemap)
- `index.html`, `work/*.html`: generated pages, do not edit by hand
- `assets/css/style.css`: design system and responsive layout
- `assets/js/main.js`: navigation and reveal animations
- `assets/js/viewer3d.js`: lazy Three.js orbit viewer with poster fallback
- `assets/models/*.glb`: exported 3D models, ceiling removed
- `assets/img/brenda-*.webp`: Nerima's portrait and project photographs
- `assets/img/field-*.webp`: field and client-work images, prepared with OpenCV
- `assets/img/business-card-966.webp`: Neri Creations & Interiors card used for business details
- `assets/img/`: responsive WebP stills (800/1280 px) and 1200×630 OG images
- `assets/nerima-brenda-cv.pdf`: downloadable CV
- `assets/vendor/`: vendored Three.js r160 module and addons
- `blender/render_rooms.py`: headless scene builder, five rooms, Cycles renders
- `blender/export_glb.py`: exports each `.blend` to `assets/models/*.glb`
- `blender/audit_geometry.py`: wall, rug and depth checks for each room
- `blender/make_web_images.py`: converts renders into site WebP assets

## Content

The copy is written from Nerima's CV, voice-note interview, field images and OCR of her business card. It covers her Bachelor of Interior and Landscape Design at Kyambogo University, two internships at Meek Construction Company Limited, the Neri Creations & Interiors practice, and client work on TV wall units, kitchen cabinets, floor plans, site plans, 3D designs, custom furniture, lighting, decor and landscaping. Past-client mood charts pair the field imagery with palettes extracted from the photographs.

## Room dimensions

The 3D scenes use researched anthropometric standards: seat heights around 450 mm, dining tops at 750 mm, worktops at 900 mm, 600 mm bed clearances, 900 mm circulation routes, a compact kitchen work triangle, pendants 750 mm above the table, artwork centred at 1.5 m and windows above one-eighth of the floor area. References include Neufert's *Architects' Data* and Panero and Zelnik's *Human Dimension and Interior Space*.

## Rebuild

Render the five scenes (Cycles CPU; `ROOMS_ONLY=dining-corner` limits the run):

```sh
/Applications/Blender.app/Contents/MacOS/Blender -b --python blender/render_rooms.py
```

Audit, export the web models and regenerate images:

```sh
/Applications/Blender.app/Contents/MacOS/Blender -b --python blender/audit_geometry.py
/Applications/Blender.app/Contents/MacOS/Blender -b --python blender/export_glb.py
python3 blender/make_web_images.py
python3 build.py
```

Edit `PROJECTS`, `EMAIL`, `PHONE`, `PHONE_2`, `BUSINESS`, `LOCATION` or `BASE` at the top of `build.py`, then rebuild.

## Local preview

```sh
python3 -m http.server 8099
```

Then open http://localhost:8099/.

## Deploy

GitHub Pages serves the repository root from `main`. Push changes:

```sh
git add -A && git commit -m "Update site" && git push
```
