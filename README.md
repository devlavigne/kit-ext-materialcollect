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

1.  bashCopy codegit clone https://github.com/devlavigne/kit-ext-materialcollect.git
    
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
        

Contributing
------------

Contributions are welcome! If you have suggestions for improvements or encounter any issues, please open an [issue](https://github.com/devlavigne/kit-ext-materialcollect/issues) or submit a pull request.

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

    

**Disclaimer:** This extension is provided "as is" without warranty of any kind. Use it at your own risk, and always back up your data before running scripts that modify your scenes.
