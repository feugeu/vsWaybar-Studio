#!/usr/bin/env bash
# weather.sh — fallback weather via wttr.in (no API key required)
# Used when weather.py is unavailable or unconfigured.
# Output: JSON for waybar custom/weather module.

CITY="${WEATHER_CITY:-Monterrey}"
LANG="${WEATHER_LANG:-es}"

DATA=$(curl -sf "https://wttr.in/${CITY}?format=j1&lang=${LANG}" 2>/dev/null)

if [[ -z "$DATA" ]]; then
    echo '{"text": "󰖐 --", "tooltip": "Sin conexión", "class": "unknown"}'
    exit 0
fi

TEMP=$(echo "$DATA" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['current_condition'][0]['temp_C'])" 2>/dev/null)
DESC=$(echo "$DATA" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['current_condition'][0]['weatherDesc'][0]['value'])" 2>/dev/null)
ICON="󰖙"

echo "{\"text\": \"${ICON} ${TEMP}°C\", \"tooltip\": \"${DESC}\", \"class\": \"weather\"}"
