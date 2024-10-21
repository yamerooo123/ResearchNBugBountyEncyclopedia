**Research by Suphawith Phusanbai**

<h1>Pymol</h1>

Open-source foundation of the user-sponsored PyMOL molecular visualization system.

GitHub repo: https://github.com/schrodinger/pymol-open-source

**Tested on:**

Distributor ID: Ubuntu

Description:    Ubuntu 22.04.5 LTS

Release:        22.04

Codename:       jammy

<h1>Findings</h1>

1. RCE through the Run Script function

<h1>Details</h1>

The software implements serveral dangerous Python functions without input sanitization. For instance, a file with PYM file extension is treated the same as a Python, allowing the attackers to insert a malicious PYM file with reverse shell payload. This could potentially lead to RCE.

