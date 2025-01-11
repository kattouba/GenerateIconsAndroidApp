### README: Android Icon Generator Utility

#### Description
This utility script generates icon files for Android applications compatible with the BeeWare framework. It creates icons in various sizes and shapes (square, round, and adaptive) to meet Android specifications. Users provide an input image, and the script generates the required icons automatically.

---

#### Features
- Generates square, round, and adaptive icons.
- Supports input image formats such as PNG, JPG, and other common formats.
- Outputs PNG files in multiple resolutions required for Android applications.

---

#### Usage
1. Run the script:
   ```bash
   python3 GenerateIconsAndroidApp.py
   ```
2. When prompted, provide the path to your input image file.
3. The script will generate the icons and save them in the current working directory.

---

#### Output
The generated files will be named using the format:
- `icon-square-<size>.png`
- `icon-round-<size>.png`
- `icon-adaptive-<size>.png`

---

#### Prerequisites
1. Python 3.6 or higher.
2. Install required Python libraries:
   ```bash
   pip install pillow
   ```

---

#### Notes
- Ensure the input image has sufficient resolution for resizing to large sizes (e.g., 1280x1280 pixels or higher).
- Generated files will overwrite existing files with the same names in the current directory.

---

#### License
This utility is released under the GNU General Public License v2.

---

#### Credits
This utility is the creation of **Studio KATEB & Papa**.
