Move Materials to Looks Extension for NVIDIA Omniverse
======================================================

An Omniverse Kit extension that moves all materials in your USD stage to the /Looks folder, ensuring a cleaner and more organized scene hierarchy. This extension is especially useful when working with complex scenes containing numerous materials nested within object hierarchies.

Table of Contents
-----------------

*   [Introduction](#introduction)
    
*   [Features](#features)
    
*   [Installation](#installation)
    
*   [Usage](#usage)
    
*   [Code Overview](#code-overview)
    
*   [Contributing](#contributing)
    
*   [License](#license)
    
*   [About the Author](#about-the-author)
    

Introduction
------------

In large USD scenes, materials are often scattered throughout the object hierarchy, making it difficult to manage and edit them efficiently. This extension automates the process of collecting all materials and moving them to a centralized /Looks folder, updating material bindings accordingly to maintain the integrity of your scene.

Features
--------

*   **Automated Material Organization:** Collects all UsdShade.Material instances and moves them to the /Looks folder.
    
*   **Binding Updates:** Automatically updates all material bindings to reference the new material locations.
    
*   **Conflict Resolution:** Handles name conflicts by appending an index to duplicate material names.
    
*   **User-Friendly Interface:** Provides a simple UI with a single button to execute the operation.
    

Installation
------------

### Prerequisites

*   **NVIDIA Omniverse Code** or **Omniverse Create**
    
*   **Python 3.7+**
    

### Steps

1.  bashCopy codegit clone https://github.com/yourusername/MoveMaterialsToLooks.git
    
2.  Copy the MoveMaterialsToLooks extension folder into your Omniverse extensions directory. The default user extensions directory is usually located at:
    
    *   Windows: %LOCALAPPDATA%\\Kit\\Shared\\Extensions\\
        
    *   Linux: ~/.local/share/Kit/Shared/Extensions/
        
3.  **Reload Extensions in Omniverse**
    
    *   Open Omniverse Code or Create.
        
    *   Go to Window > Extensions to open the Extensions Manager.
        
    *   Click on the gear icon and select Reload Extensions.
        
    *   Search for "Move Materials to Looks" in the Extensions Manager.
        
    *   Enable the extension by toggling it on.
        

Usage
-----

1.  Load the USD file containing the materials you wish to organize.
    
2.  **Launch the Extension**
    
    *   If not already open, go to Window > Move Materials to /Looks to open the extension's UI.
        
3.  **Execute the Operation**
    
    *   In the extension window, click the **Execute** button.
        
    *   The extension will process the scene, moving all materials to the /Looks folder and updating bindings.
        
    *   A confirmation message will appear in the console upon completion.
        
4.  **Verify the Changes**
    
    *   Check the **Stage** window to confirm that all materials are now under the /Looks folder.
        
    *   Ensure that all objects still display the correct materials.
        

Code Overview
-------------

Below is the main code for the extension, formatted for clarity:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pythonCopy codeimport omni.ext  import omni.ui as ui  from pxr import Usd, UsdShade, Sdf  import omni.usd  import omni.kit.commands  class MoveMaterialsToLooksExtension(omni.ext.IExt):      def on_startup(self, ext_id):          # Called when the extension is enabled          print("[MoveMaterialsToLooks] Extension starting up")          # Create a UI window for the extension          self._window = ui.Window("Move Materials to /Looks", width=300, height=100)          with self._window.frame:              with ui.VStack():                  # Add a label and a button to the UI                  ui.Label("Move all materials to the /Looks folder.", alignment=ui.Alignment.CENTER)                  ui.Button("Execute", clicked_fn=self._on_execute_button_click)      def on_shutdown(self):          # Called when the extension is disabled          print("[MoveMaterialsToLooks] Extension shutting down")          if self._window:              # Destroy the UI window              self._window.destroy()              self._window = None      def _on_execute_button_click(self):          # Called when the "Execute" button is clicked          self.move_materials_to_looks()      def move_materials_to_looks(self):          # Get the current USD stage          stage = omni.usd.get_context().get_stage()          if not stage:              print("No stage is open.")              return          # Define the /Looks folder if it doesn't exist          looks_path = Sdf.Path('/Looks')          if not stage.GetPrimAtPath(looks_path):              stage.DefinePrim(looks_path, 'Scope')  # You can use 'Xform' if preferred          # Collect all materials not already in /Looks          materials_to_move = []          for prim in stage.Traverse():              if prim.IsA(UsdShade.Material):                  material_path = prim.GetPath()                  if not material_path.HasPrefix(looks_path):                      materials_to_move.append(prim)          # Move each material and update bindings          for material_prim in materials_to_move:              material_path = material_prim.GetPath()              material_name = material_path.name              # Handle name conflicts in /Looks              new_material_name = material_name              new_material_path = looks_path.AppendChild(new_material_name)              index = 1              while stage.GetPrimAtPath(new_material_path):                  new_material_name = f"{material_name}_{index}"                  new_material_path = looks_path.AppendChild(new_material_name)                  index += 1              # Move the material              result = omni.kit.commands.execute('MovePrim',                                                 path_from=str(material_path),                                                 path_to=str(new_material_path))              if not result:                  print(f"Failed to move material {material_path} to {new_material_path}")                  continue              # Update material bindings              for prim in stage.Traverse():                  binding_api = UsdShade.MaterialBindingAPI(prim)                  bound_material = binding_api.GetDirectBinding().GetMaterial()                  if bound_material and bound_material.GetPath() == material_path:                      binding_api.Bind(UsdShade.Material(stage.GetPrimAtPath(new_material_path)))          print("Materials have been moved to the /Looks folder.")   `

Contributing
------------

Contributions are welcome! If you have suggestions for improvements or encounter any issues, please open an [issue](https://github.com/yourusername/MoveMaterialsToLooks/issues) or submit a pull request.

### Steps to Contribute

1.  Click on the **Fork** button at the top right corner of the repository page.
    
2.  bashCopy codegit clone https://github.com/yourusername/MoveMaterialsToLooks.git
    
3.  bashCopy codegit checkout -b feature/YourFeature
    
4.  **Make Your Changes**
    
5.  bashCopy codegit add .git commit -m "Add YourFeature"git push origin feature/YourFeature
    
6.  Go to the original repository and open a pull request from your feature branch.
    

License
-------

This project is licensed under the [MIT License](LICENSE).

About the Author
----------------

**Devin Lavigne**

Co-founder of [Houseal Lavigne](https://www.hlplanning.com/), an award-winning planning, zoning, and geospatial firm specializing in urban planning and GIS services. With a passion for integrating technology into urban development, Devin brings innovative solutions to complex planning challenges.

Connect with me:

*   [LinkedIn](https://www.linkedin.com/in/devinlavigne)
    
*   [Personal Website](https://www.devinlavigne.com/)
    

**Disclaimer:** This extension is provided "as is" without warranty of any kind. Use it at your own risk, and always back up your data before running scripts that modify your scenes.

**Note:** Replace https://github.com/yourusername/MoveMaterialsToLooks.git and other placeholder URLs with your actual GitHub repository links.
