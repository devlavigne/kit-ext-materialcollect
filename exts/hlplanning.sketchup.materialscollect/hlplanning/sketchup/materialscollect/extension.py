import omni
import omni.ext
import omni.ui as ui
from pxr import Usd, UsdShade, Sdf
import omni.usd
import omni.kit.commands

class MoveMaterialsToLooksExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        print("[MoveMaterialsToLooks] Extension starting up")

        # Create a window with a button
        self._window = ui.Window("Move Materials to /Looks", width=300, height=100)
        with self._window.frame:
            with ui.VStack():
                ui.Label("Move all materials to the /Looks folder.", alignment=ui.Alignment.CENTER)
                ui.Button("Execute", clicked_fn=self._on_execute_button_click)

    def on_shutdown(self):
        print("[MoveMaterialsToLooks] Extension shutting down")
        if self._window:
            self._window.destroy()
            self._window = None

    def _on_execute_button_click(self):
        self.move_materials_to_looks()

    def move_materials_to_looks(self):
        # Get the current stage
        stage = omni.usd.get_context().get_stage()
        if not stage:
            print("No stage is open.")
            return

        # Define the /Looks folder if it doesn't exist
        looks_path = Sdf.Path('/Looks')
        if not stage.GetPrimAtPath(looks_path):
            stage.DefinePrim(looks_path, 'Scope')  # Use 'Scope' or 'Xform' based on preference

        # Collect all materials that need to be moved
        materials_to_move = []
        for prim in stage.Traverse():
            if prim.IsA(UsdShade.Material):
                material_path = prim.GetPath()
                if not material_path.HasPrefix(looks_path):
                    materials_to_move.append(prim)

        # Move materials to /Looks and update bindings
        for material_prim in materials_to_move:
            material_path = material_prim.GetPath()
            material_name = material_path.name

            # Generate a unique name to avoid conflicts
            new_material_name = material_name
            new_material_path = looks_path.AppendChild(new_material_name)
            index = 1
            while stage.GetPrimAtPath(new_material_path):
                new_material_name = f"{material_name}_{index}"
                new_material_path = looks_path.AppendChild(new_material_name)
                index += 1

            # Move the material using the Omni command
            result = omni.kit.commands.execute('MovePrim',
                                               path_from=str(material_path),
                                               path_to=str(new_material_path))
            if not result:
                print(f"Failed to move material {material_path} to {new_material_path}")
                continue  # Skip updating bindings if move failed

            # Update material bindings to point to the new material path
            for prim in stage.Traverse():
                binding_api = UsdShade.MaterialBindingAPI(prim)
                bound_material = binding_api.GetDirectBinding().GetMaterial()
                if bound_material and bound_material.GetPath() == material_path:
                    # Rebind to the new material path
                    binding_api.Bind(UsdShade.Material(stage.GetPrimAtPath(new_material_path)))

        print("Materials have been moved to the /Looks folder.")
