# VSCode Theme Desaturator
This script reduces the saturation of all colors in a Visual Studio Code theme file. It processes the theme file and generates a new file with reduced color saturation, making it easier on the eyes.

## Features
- Processes a Visual Studio Code theme JSON file.
- Reduces the saturation of all colors by a specified factor.
- Handles various color formats (#RGB, #RRGGBB, #AARRGGBB).

## Prerequisites
- Python 3.6 or higher
  > to check if you have, type `python` in Powershell.


## How to desaturate a theme
1. Download the script into some folder.

2. Install the required Python package: (using any terminal e.g. powershell)

   `pip install colormath`

3. Navigate into the theme folder of your Visual Studio Code installation, find and make a copy of the theme file you want to desaturate into the same folder you downloaded the script. Name the copy **your_theme.json**.
   
   > in Windows 10, the default theme locations for Visual Studio Code are: `C:\Users\username\AppData\Local\Programs\Microsoft VS Code\resources\app\extensions` and `C:\Users\username\.vscode\extensions`
   
   E.g.

   > ![image](https://github.com/user-attachments/assets/5789bf46-e4e9-495f-86ff-4c56507c080a)
   
   > Sidenote: You can also open the theme file in any text editor or preferrably in VS Code itself if you want to change just a few colors.

4. Run the script with command:

   `python reduce_saturation.py`

    > The script will process the theme file and create a new file `your_theme_saturation_reduced.json` with reduced saturation.

   > Before running the script you can adjust the desaturation amount by opening the `reduce_saturation.py` script in any text editor and modifying the `saturation_reduction_factor` variable, a line that looks like this:
   
   `saturation_reduction_factor = 0.5  # Adjust this factor (0.0 to 1.0) to control the level of saturation reduction`


6. Replace the theme with your new one:

   1. Move the freshly generated `your_theme_saturation_reduced.json` file into the same folder as the original theme file.
   2. Locate and open the original theme's `package.json` file, and edit it's `"path":` variable to use your new theme.

      Like this:

      ![image](https://github.com/user-attachments/assets/2741c87e-864d-4dba-b9ac-68c6715c14e3)


   

## Error Handling
You should check the validity of the theme file in [JSONLint](https://jsonlint.com/).

## License
This project is licensed under the MIT License.
