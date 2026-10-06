# NEXUS case v1.2

[Editable Onshape case](https://cad.onshape.com/documents/93b46cd1c225a7c1c0317dbe/w/328820a536ad539164365b4e/e/89c11f70e4b29e71ba5d3f40).

The document contains four printable bodies: base, top plate, and two OLED side clamps. Download the stored tabs `NEXUS-case-v1.2.step` and `NEXUS-case-v1.2-print-parts.zip`. The ZIP contains separate binary STL parts in millimetres, Fine resolution. Older v1/v1.1 exports and the legacy notes are superseded; do not print those versions.

The custom case feature includes 'Show electronics fit envelopes'. It is OFF for fabrication exports. Enable it for inspection only: the extra bodies are nominal clearance envelopes, not real components or printable parts. The feature automatically checks interference before removing/hiding those bodies. See [FIT-CHECK.md](FIT-CHECK.md) for corrections, checks, and limitations.

## Key dimensions

- Enclosure: 76 x 78 x 26 mm; walls 3 mm; floor 2.4 mm.
- Six MX centers: X=18.95,38,57.05; Y=19,38.05; pitch 19.05 mm.
- Default switch opening: 14.1 mm square. Local plate thickness: 1.5 mm.
- Plate top Z=26; local underside Z=24.5; PCB top/bottom Z=21/19.4. The earlier PCB stack was 1.5 mm too low.
- OLED window: 32 x 10.5 mm; module pocket: 40 x 15.5 mm, centered at (38,60.5). Pocket ceiling Z=24.5. Actual module fit is not confirmed.
- Clamp screw centers: (14,60.5),(62,60.5); clamp top Z=18.2. Choose gentle nonconductive foam for the actual OLED stack; do not compress glass or electronics.
- Four M3 case posts: X=6.5/69.5, Y=6.5/71.5; insert pilot diameter defaults to 4.2 mm and MUST match the insert supplier's recommended hole.
- Rear cable slot: 16 mm wide, bottom Z=5. Exact cable housing/connector alignment still needs confirmation.

## Assembly

Trial-print a switch opening and insert hole first. Print the base floor down, plate outer face down, and clamps flat; drop exported parts to the slicer bed because they retain assembly coordinates. Install inserts; clip switches into the plate; solder the PCB at the correct switch seating height. Install the underside controller sockets/module and trim leads carefully. Fit optional underside pullups only if needed. Solder low-profile insulated OLED wires directly to J1: no vertical header. Retain the OLED using the two clamps, foam, and M2x8 screws. Verify all clearances and USB cable access before closing with four M3x16 screws. Optional foot recesses suit approximately 8 mm adhesive feet.

This is not a fabrication release. Exact component dimensions, lead/solder clearances, printing tolerances, and physical fit remain unverified. Firmware and physical testing remain outstanding.

![Nominal fit with plate hidden](fit-v1.2.jpg)
