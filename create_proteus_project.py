import os
import xml.etree.ElementTree as ET

def create_proteus_project(spice_netlist_path, project_name):
    # Check if the SPICE netlist file exists
    if not os.path.isfile(spice_netlist_path):
        raise FileNotFoundError(f"SPICE netlist file '{spice_netlist_path}' not found.")

    # Create the Proteus project XML structure
    project = ET.Element('ProteusProject')
    project.set('Name', project_name)
    project.set('Type', 'SPICE')

    spice_netlist = ET.SubElement(project, 'SPICENetlist')
    spice_netlist.text = spice_netlist_path

    # Additional project configuration can be added here

    # Create an XML tree and write to a .pdsprj file
    project_tree = ET.ElementTree(project)
    project_file_path = f'{project_name}.pdsprj'
    project_tree.write(project_file_path)
    print(f"Proteus project '{project_name}' created successfully at '{project_file_path}'.")

# Example usage
# create_proteus_project('example_netlist.sp', 'MyProteusProject')