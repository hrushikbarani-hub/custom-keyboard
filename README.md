# NEXUS 2x3 Wired Macro Pad

A compact six-key wired macro pad with a small I2C OLED screen.

## Design direction

- Layout: 2 rows x 3 columns, six MX-style keys
- Controller: Hack Club Orpheus Pico 2, USB-C, Pico-compatible footprint
- Display: Waveshare 0.91-inch OLED SKU 14657, SSD1306 128x32, GP4/GP5
- Firmware: USB HID macro layers
- PCB: custom KiCad board
- Case: two-piece 3D-printed case

## Initial layers

NEXUS: Wake PC, open NEXUS, display standby, microphone toggle, Jellyfin, Pi-hole/Tailscale status.

Media: previous, play/pause, next, volume down, volume up, mute.

## Build status

- [x] Concept, layout, pin budget, BOM, and grant draft
- [x] Confirm exact controller, OLED, switch, and socket part numbers
- [x] KiCad schematic (ERC clean)
- [x] PCB routing (DRC/connectivity/parity clean)
- [x] Case CAD (v1.1; physical fit pending)
- [x] Firmware source prepared
- [ ] Physical assembly and testing
