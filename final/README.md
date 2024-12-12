# Generate a Prop Rig

## usage
this tool creates a prop rig with three joints organized in a herichy placed according to three locators.

## Prerequisites
To use this python code, the environment variable must be defined in GitBash and maya must be opened uing the GitBash terminal.

    Follow This Setup:  
    #export ASSET=insert_your_asset_name   

    Environment Variables Description:  
    ASSET: The name of the asset in Maya you want to export.  


## overview
```python
- '--UI': Creates a user interface to easily click the following buttons: 'Create Group', 'Place Locators' and 'Build Rig'

- '--createGroup': Creates a group called 'GRP_{assetName}' for the selected geometry. PArented under GRP_{assetName}, will be and empty group GRP_rig and GRP_geom which holds the geometry. If no geometry is selected, program will print: "No object is selected. Script Ended."

- '--placeLocators': places three locators named: 'LOC_root', 'LOC_base' and 'LOC_move'

- '--def buildRig(self)': Creates a joint hierarchy with each joint at the matching locator position under GRP_rig. Each time the button is pressed again, it will not add new joints, but will move the existing joints to the correct locator position
```

## final setup
JNT_root
    ┗ JNT_base
              ┗ JNT_move

So the final asset structure will look like:

GRP_<ASSET>        # Asset name from environment variable set in Bash
    ┗ GRP_geom
            ┗ mesh1
            ┗ mesh2
            ┗ ...
    ┗ GRP_rig
             ┗JNT_root
                    ┗ JNT_base
                           ┗ JNT_move
