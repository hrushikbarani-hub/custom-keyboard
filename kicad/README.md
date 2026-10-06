# NEXUS 2x3 macro pad — KiCad 10

Open `NEXUS-MacroPad.kicad_pro`. Editable schematic, fully routed two-layer PCB, and project-local footprints are included. `manufacturing/` contains the two copper layers, both masks and silkscreens, board outline, and separate plated/non-plated Excellon drills. No solder-paste files are needed for this through-hole design.

## Fabrication and assembly

- PCB: 60 x 66 mm bounding box; chamfered outline with two OLED clamp reliefs. Two copper layers, 1.6 mm FR4, 0.25 mm traces/clearance, 0.8/0.4 mm vias. Order only after confirming the selected hardware dimensions.
- Six PCB-mount Cherry-MX-compatible switches, 19.05 mm pitch. Plate mounting supplies mechanical retention; switch solder joints locate the PCB. No independent PCB mounting screws are used.
- Six 1N4148 DO-35 diodes with 7.62 mm lead pitch. Cathode/band is the square pad and goes to the row. Front keys are SW1–3; rear keys SW4–6.
- Non-wireless Pico-compatible module socketed **under** the board, component side facing the case floor, USB facing the rear. Use two 1x20, 2.54 mm socket strips plus matching module headers. The host-board footprint courtyard describes socket rows, not the elevated underside module body. Do not install a Pico W: its antenna clearance is not provided.
- J1 is four direct-solder wire pads, not a header or a direct OLED-module footprint. Pin 1 GND, pin 2 3.3 V, pin 3 SCL, pin 4 SDA. Check the actual OLED pin order; use 3.3 V only. Solder insulated flexible leads directly to the pads and provide strain relief. Do not fit a vertical header: it would hit the lid. Keep solder/wire height below 1.2 mm above the PCB.
- R1 and R2 are optional 4.7k through-hole pullups on the PCB underside, marked DNP. Leave them empty if the display already has I2C pullups; populate only if needed. Top-side mounting would overlap the OLED envelope.
- Avoid long switch/diode leads on the underside where they approach the raised controller. Trim and inspect before inserting the module. Do not connect an external 5 V supply.

## Firmware pin assignment

| Function | GPIO | Pico physical pad |
|---|---|---|
| OLED SDA | GP4 | 6 |
| OLED SCL | GP5 | 7 |
| Front row ROW0 | GP6 | 9 |
| Rear row ROW1 | GP7 | 10 |
| Left column COL0 | GP8 | 11 |
| Middle column COL1 | GP9 | 12 |
| Right column COL2 | GP10 | 14 |

Scan rows low with column input pullups (COL2ROW). The schematic deliberately leaves unused module pins unconnected. Pico module ground pads are internally common; all seven carrier ground pads are also routed.

## Case compatibility and limits

Use the revised **v1.2** case in the [Onshape document](https://cad.onshape.com/documents/93b46cd1c225a7c1c0317dbe/w/328820a536ad539164365b4e/e/89c11f70e4b29e71ba5d3f40). The old v1 OLED bridge is superseded by two side clamps, which clear the PCB reliefs. Six underside diode pockets provide clearance after correcting the switch stack. Four printed bodies: base, plate, two clamps. Older case exports are superseded.

Case coordinates are front-left origin. PCB X = 100 + case X; PCB Y = 178 - case Y. Assembled PCB top is case Z = 21 mm, bottom 19.4 mm; the plate top is Z = 26 mm, and the local underside Z = 24.5 mm. MX seating uses 5 mm from plate TOP to PCB top (3.5 mm below the 1.5 mm clip region). STEP uses XY aligned to the case and requires a +21 mm Z translation. The earlier 19.5/17.9 mm stack was incorrect and is superseded. See the [Cherry mechanical drawing](https://www.farnell.com/datasheets/1792245.pdf), mounting options on page 2.

The STEP uses a generic Raspberry Pi Pico, not the exact USB-C Orpheus board. Installed MX switch 3D models are missing; their native footprint geometry is present. Onshape now checks the exact PCB outline plus 20 nominal electronics envelopes against the case and each other. The USB-plug/controller bounding-box overlap is intentionally excluded because a plug engages the connector; exact connector mating is not modeled. Nominal checks passed, but these are not a tolerance analysis or an exact component assembly. Actual socket height, USB plug, OLED module, switch variant, and insert pilot still require confirmation. No physical prototype has been tested. Toggle 'Show electronics fit envelopes' in the case feature to inspect; keep it OFF for printing/exporting case parts.

KiCad ERC, DRC, connectivity, and schematic-to-PCB parity reports are included. No reported issues were suppressed to obtain a pass. Manufacturing exports are design outputs, not an instruction to order without the above checks.
