# vsWaybar Studio

<p align="center">
  <img src="vswaybar-studio.png" alt="vsWaybar Studio" width="180"/>
</p>

[![AUR version](https://img.shields.io/aur/version/vswaybar-studio?color=1793d1&label=AUR&logo=arch-linux)](https://aur.archlinux.org/packages/vswaybar-studio)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A visual configuration editor for [Waybar](https://github.com/Alexays/Waybar) — build, style and preview your bar in real time.

No more editing JSON and CSS by hand. Design your Waybar with live feedback, templates and full module control.

> Available on the AUR as [`vswaybar-studio`](https://aur.archlinux.org/packages/vswaybar-studio).
> Single-file Python 3 + GTK3 application.

---

## Who is this for?

vsWaybar Studio is built for people who want a great-looking, functional Waybar **without having to learn JSON, CSS and the Waybar wiki from scratch**.

If you are new to Hyprland or tiling window managers, the default Waybar setup can feel overwhelming: a JSON config file, a separate CSS file, cryptic module keys, format strings, and a restart cycle just to see any change. vsWaybar Studio removes that friction — you pick a template, adjust colors and modules visually, hit Apply, and you have a working bar.

**This tool is not meant to replace hand-crafted configs.** If you already know Waybar well and maintain a complex setup with custom scripts, named instances, grouped modules and per-module CSS overrides, you will quickly hit the edges of what the editor can do. That is by design — the goal is a smooth on-ramp, not a full IDE.

What vsWaybar Studio does handle gracefully: it reads your existing config on startup, preserves any blocks it does not recognize, and writes them back untouched. So you can use it alongside a manually edited config without losing anything.

---

## Screenshots

### Templates
![Templates](screenshots/1.png)

### Bar Settings
![Bar](screenshots/2.png)

### Layout Editor
![Layout](screenshots/3.png)

### Module Config
![Modules](screenshots/4.png)

### Styling / Color Palette
![Styling](screenshots/5.png)

---

## Features

- **Live bar preview** — a thin strip at the top mirrors your actual Waybar in real time; always visible, never scrolls away
- **Bar settings** — position, output/monitor, height, spacing, margins, layer
- **Visual styles** — Bar (solid), Islands (floating zones), Modules (per-pill)
- **Layout editor** — drag modules between Left / Center / Right zones for both bar and dock
- **Module config** — click any module to edit its specific settings (format, intervals, on-click actions, colors, animations…)
- **User Commands** — add unlimited custom launcher modules: choose an icon from a Nerd Font glyph picker, set a color and an on-click command; they appear in the bar as clickable icons
- **Styling** — edit all 14 CSS color tokens, font, opacity, border-radius, padding
- **Templates** — 54 ready-made themes across 36 color palettes and 3 visual styles; apply with one click
- **Palette tools** — load from image via [matugen](https://github.com/InioX/matugen), or generate a random palette
- **Scripts editor** — edit `weather.py` and other custom scripts in-place
- **Automatic backups** — every apply creates a timestamped backup of your config, CSS and scripts
- **Lazy tab loading** — only the active tab is built at startup; remaining tabs load on first visit for fast startup
- **Dark / Light editor theme** toggle
- Apply writes `config` + `style.css` to disk and restarts Waybar automatically

---

## Requirements

- Python 3.10+
- `python-gobject` (GTK3 bindings)
- `python-cairo`
- [Waybar](https://github.com/Alexays/Waybar)
- [Hyprland](https://github.com/hyprwm/Hyprland) (for `hyprland/workspaces` and `hyprland/window` modules)

Optional:
- [matugen](https://github.com/InioX/matugen) — palette generation from wallpaper
- [swaync](https://github.com/ErikReider/SwayNotificationCenter) — notification center module
- [wlogout](https://github.com/ArtsyMacaw/wlogout) — power menu module

---

## Installation

### AUR (Arch Linux)

```bash
yay -S vswaybar-studio
# or
paru -S vswaybar-studio
```

### Manual

```bash
git clone https://github.com/victorsosaMx/vsWaybar-Studio
cd vsWaybar-Studio
chmod +x vswaybar-studio
./vswaybar-studio
```

The editor reads `~/.config/waybar/config` and `~/.config/waybar/style.css` on startup.
**Apply** writes both files back and restarts Waybar.

---

## Setting up the Weather module

The weather module uses `weather.py` — a script that queries the [OpenWeatherMap API](https://openweathermap.org/api).
A free API key is required (no credit card needed).

### Step 1 — Get a free API key

1. Go to [openweathermap.org](https://openweathermap.org) and create a free account
2. Go to **API Keys** in your profile → copy your key
3. The free tier includes current weather data (more than enough)

### Step 2 — Configure the script

Open vsWaybar Studio → **Modules** tab → select **Weather** from the list.

Fill in:
- **API Key** — paste your OpenWeatherMap key
- **City** — your city name (e.g. `Monterrey`, `New York`, `Madrid`)
- **Units** — `metric` (°C) or `imperial` (°F)

Click **Save weather.conf**. This writes `~/.config/waybar/weather.conf` with your settings.
The API key is stored only in that file — it is never included in the script itself.

### Step 3 — Save the script

Go to the **Scripts** tab → select **Weather fetcher** → click **Save script**.

This writes `weather.py` to `~/.config/waybar/scripts/weather.py` with execute permissions.

### Step 4 — Apply

Click **Apply** in the header. Waybar will restart and the weather module will appear in the bar.

> **Note:** The script interval defaults to 3600 seconds (1 hour). On first run it may take a moment to fetch.
> If you see no weather data, verify your API key is valid and your city name is spelled correctly.

---

## Setting up the Updates module

The updates module (`custom/updates`) shows the number of pending system updates using `checkupdates` from [pacman-contrib](https://gitlab.archlinux.org/pacman/pacman-contrib).

### Step 1 — Install pacman-contrib

```bash
sudo pacman -S pacman-contrib
```

### Step 2 — Install a terminal emulator

The updates module opens a terminal to run the actual update. By default it uses [Kitty](https://github.com/kovidgoyal/kitty):

```bash
sudo pacman -S kitty
```

If you prefer a different terminal, go to **Modules** → **Updates** and change the **On click** command.

### Step 3 — Configure the module (optional)

Go to **Modules** tab → select **Updates** from the list.

You can change:
- **On click** — the command that runs when you click the module (e.g. open a terminal with `yay` or `flatpak update`)
- **Interval** — how often to check for updates (default: 3600 seconds)

### Step 4 — Apply

Click **Apply**. The updates count will appear in the right side of the bar.

> **Note:** `checkupdates` checks only `pacman` packages. For AUR packages, edit the script in the **Scripts** tab to also run `yay -Qua` or similar.

---

## Adding User Commands

User Commands are custom launcher modules — a clickable icon in the bar that runs a command when clicked.

### Step 1 — Open the Modules tab

Go to **Modules** → scroll down to the **User Commands** section → click **+ Add**.

Enter a short name (letters and hyphens only, e.g. `spotify`, `terminal`, `files`). The module key will be `custom/<name>`.

### Step 2 — Configure the module

- **Icon** — click **Choose icon…** to pick a glyph from the Nerd Font library (~96 icons)
- **Color** — pick a color using the color button or type a hex value
- **On click** — the command to run (e.g. `spotify`, `kitty`, `nautilus`)
- **Tooltip text** — optional hover label

### Step 3 — Add it to the bar

Go to the **Layout** tab → drag `custom/<name>` into the Left, Center or Right zone.

### Step 4 — Apply

Click **Apply**. The icon appears in the bar and clicking it runs your command.

> To remove a User Command: Modules tab → select it → click **− Remove**. It is removed from the bar and all zones immediately.

---

## Backups

Every save operation (Apply, Save as…, Save script, Save script as…) automatically backs up your current files to:

```
~/.config/waybar/backups/
  20260321_143022_config
  20260321_143022_style.css
  20260321_143022_weather.py
  ...
```

Backups are timestamped — you can always roll back by copying a backup file over the original.

---

## Included Color Palettes

### Standard themes
| Palette | Source |
|---|---|
| Catppuccin Mocha / Latte / Macchiato / Frappe | [catppuccin/catppuccin](https://github.com/catppuccin/catppuccin) |
| Dracula | [dracula/dracula-theme](https://github.com/dracula/dracula-theme) |
| Nord / Nord Light | [nordtheme/nord](https://github.com/nordtheme/nord) |
| Gruvbox Dark / Light | [morhetz/gruvbox](https://github.com/morhetz/gruvbox) |
| Tokyo Night | [folke/tokyonight.nvim](https://github.com/folke/tokyonight.nvim) |
| One Dark | [atom/one-dark-ui](https://github.com/atom/one-dark-ui) |
| Rosé Pine | [rose-pine/rose-pine-theme](https://github.com/rose-pine/rose-pine-theme) |
| Everforest | [sainnhe/everforest](https://github.com/sainnhe/everforest) |
| Kanagawa | [rebelot/kanagawa.nvim](https://github.com/rebelot/kanagawa.nvim) |
| Solarized Dark / Light | [altercation/solarized](https://github.com/altercation/solarized) |
| Monokai | [monokai.pro](https://monokai.pro) |
| GitHub Dark | [primer/primitives](https://github.com/primer/primitives) |

### Custom palettes
Forest Night, Forest, Forest Daylight, Mario, Mario Dark, Luigi Dark, Vader, Cyberpunk Neon, Cyberpunk Yellow, Anime, Aurora Borealis, Carnage, Hello Kitty, Tux, Sand, Ubuntu Dark, Ice Mint, Retro Paper.

---

## Acknowledgements

This project is built on top of amazing open-source work:

**Runtime**
- [Waybar](https://github.com/Alexays/Waybar) by Alexis Rouillard — the status bar this editor configures
- [Hyprland](https://github.com/hyprwm/Hyprland) by Vaxry — the Wayland compositor
- [GTK3](https://www.gtk.org/) / [PyGObject](https://gitlab.gnome.org/GNOME/pygobject) — GUI toolkit and Python bindings
- [PyCairo](https://pycairo.readthedocs.io/) — 2D graphics for the bar preview

**Tools integrated**
- [matugen](https://github.com/InioX/matugen) by InioX — material-you palette generator from wallpaper
- [SwayNotificationCenter](https://github.com/ErikReider/SwayNotificationCenter) by Erik Reider — notification center (`custom/swaync` module)
- [wlogout](https://github.com/ArtsyMacaw/wlogout) — Wayland logout / power menu (`custom/power` module)
- [Kitty](https://github.com/kovidgoyal/kitty) by Kovid Goyal — terminal emulator used by the updates module
- [JetBrains Mono Nerd Font](https://github.com/ryanoasis/nerd-fonts) — icons used throughout the bar modules

**Module app integrations** *(default on-click actions — all configurable)*
- [ML4W Calendar](https://github.com/mylinuxforwork/dotfiles) (`com.ml4w.calendar`) — calendar app launched from the clock module
- [Mousam](https://github.com/amit9838/mousam) by Amit Sharma (`io.github.amit9838.mousam`) — weather app launched from the weather module
- [NetworkManager](https://networkmanager.dev/) / `nm-connection-editor` — network settings launched from the network module
- [pavucontrol](https://freedesktop.org/software/pulseaudio/pavucontrol/) — PulseAudio volume control launched from the audio module
- [pacman-contrib](https://gitlab.archlinux.org/pacman/pacman-contrib) (`checkupdates`) — used by the updates module to count pending packages
- [OpenWeatherMap API](https://openweathermap.org/api) — weather data source for `weather.py` (free API key required)
- [vsFetch](https://github.com/victorsosaMx/vsFetch) — system info fetcher launched from the arch logo module

**Color palettes**
- [Catppuccin](https://github.com/catppuccin/catppuccin) — Soothing pastel theme framework
- [Dracula](https://github.com/dracula/dracula-theme) — Dark theme for everything
- [Nord](https://github.com/nordtheme/nord) — Arctic, north-bluish color palette
- [Gruvbox](https://github.com/morhetz/gruvbox) by Pavel Pertsev — retro groove color scheme
- [Tokyo Night](https://github.com/folke/tokyonight.nvim) by Folke Lemaitre
- [One Dark](https://github.com/atom/one-dark-ui) — Atom's iconic dark theme
- [Rosé Pine](https://github.com/rose-pine/rose-pine-theme) — Soho vibes for the technically minded
- [Everforest](https://github.com/sainnhe/everforest) by sainnhe — Green-based warm color scheme
- [Kanagawa](https://github.com/rebelot/kanagawa.nvim) by rebelot — Inspired by the colors of the famous painting
- [Solarized](https://ethanschoonover.com/solarized/) by Ethan Schoonover — Precision colors for machines and people
- [Monokai](https://monokai.pro) by Wimer Hazenberg — The original dark color scheme

---

## License

MIT — do whatever you want, credit appreciated.

---

*Made with GTK3 and too much caffeine.*
