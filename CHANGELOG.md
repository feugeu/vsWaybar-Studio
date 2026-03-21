# Changelog

All notable changes to vsWaybar Studio are documented here.

---

## [1.0.1] — 2026-03-21

### New features

- **User Commands** — add unlimited custom launcher modules from the Modules tab: pick an icon from a curated Nerd Font glyph library (~96 glyphs), set a color, an on-click command and an optional tooltip; each module appears in the bar as a clickable icon and can be added to any zone in the Layout tab
- **`custom/settings` module** — new built-in module: gear icon that opens vsWaybar Studio on click
- **Automatic backups** — every save operation (Apply, Save as…, Save script, Save script as…) creates a timestamped backup of `config`, `style.css` and all scripts to `~/.config/waybar/backups/` using the format `YYYYMMDD_HHMMSS_filename`
- **Bar-style detection** — reopening the editor now correctly reads `bar` / `islands` / `modules` style from the existing CSS instead of defaulting to `bar`; also restores `zone-radius`, `border-width` and module colors
- **Script execute permissions** — saving a script now sets `chmod 755` automatically; previously scripts were saved without execute permission and Waybar could not run them
- **`weather.sh` bundled default** — the fallback weather script now ships as a bundled default and is shown in the Scripts tab instead of "File not found"
- **Waybar process tracking** — the editor tracks the Waybar process it started and kills only that one on restart, avoiding conflicts with other Waybar instances

### Bug fixes

- **First install** — config and CSS directories are now created automatically if they don't exist
- **Empty or missing CSS** — when `style.css` is absent or incomplete, the editor generates a full stylesheet from a built-in base template driven by the 14 color tokens
- **CSS color tokens** — missing `@define-color` tokens are injected automatically instead of being silently skipped
- **Double Waybar** — applying changes could leave two Waybar instances running simultaneously
- **Weather and clock same color** — `#custom-weather` now uses `@peach`, `#clock` uses `@blue`; enforced on every CSS write
- **Border-width always 0 on reopen** — now correctly detected from `window#waybar` (bar style) and `.modules-left` (islands/modules)
- **Default font** — changed from `Product Sans` to `JetBrainsMono Nerd Font`
- **Default palette** — out-of-the-box palette is now Catppuccin Mocha instead of Forest Night
- **User Command color persistence** — the chosen color is saved to `style.css` and restored correctly on reopen
- **User Command padding** — each user module receives the global `mod-padding` in the CSS so icons are correctly spaced
- **Deleted User Command staying in preview** — removing a User Command now also clears it from the Layout tab zone stores immediately
- **Right-side modules too close to border** — `.modules-right` now gets extra right padding so the last icon is not flush against the bar edge

---

## [1.0.0] — 2026-03-21

### Initial release

**Core editor**
- Single-file Python 3 + GTK3 application
- Reads and writes `~/.config/waybar/config` (JSON) and `~/.config/waybar/style.css`
- Live bar preview strip at the top of the window — updates on every field change
- Dark / Light editor theme toggle
- Open and Save As support for alternative config files

**Bar tab**
- Position, output/monitor, height, spacing, layer, margins
- Visual style selector: Bar / Islands / Modules
- Opacity, zone radius, border width, separators toggle
- Font family and font size

**Layout tab**
- Interactive editor for Left / Center / Right module zones
- Add, remove and reorder modules per zone
- Load defaults button

**Modules tab**
- Full module list with per-module configuration forms
- Supported modules: `hyprland/workspaces`, `hyprland/window`, `clock`, `cpu`, `memory`, `network`, `pulseaudio`, `battery`, `tray`, `custom/arch`, `custom/weather`, `custom/updates`, `custom/swaync`, `custom/power`, and more
- Clock: format combos with presets, timezone, locale, interval, on-click actions
- Workspaces: workspace animation colors, duration, button radius/padding/min-width, persistent workspaces
- custom/arch: glyph picker, icon size, color, padding

**Styling tab**
- 14 CSS color tokens with color button + hex entry per token
- Load palette from wallpaper image via matugen
- Random palette generator (dark and light modes)
- Named palette presets (Catppuccin Mocha default)

**Templates tab**
- 54 ready-made templates across 36 color palettes
- Three visual styles per palette: Bar, Islands, Modules
- Vista previa — applies template in-place without leaving the tab or scrolling
- Aplicar — writes config + CSS to disk and restarts Waybar
- Card UI showing palette background color, text colors and color swatches

**Scripts tab**
- In-place editor for `weather.py` and other custom scripts
- OpenWeatherMap integration: API key, city and units configuration

**Palettes included**
- Catppuccin Mocha, Latte, Macchiato, Frappe
- Forest Night, Forest, Forest Daylight
- Dracula, Nord, Nord Light, Gruvbox Dark, Gruvbox Light
- Tokyo Night, One Dark, Rosé Pine, Everforest, Kanagawa
- Solarized Dark, Solarized Light, Monokai, GitHub Dark
- Mario, Mario Dark, Luigi Dark, Vader
- Cyberpunk Neon, Cyberpunk Yellow, Aurora Borealis
- Carnage, Anime, Hello Kitty, Tux, Sand, Ubuntu Dark, Ice Mint, Retro Paper
