

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"
        self.tools = [GraduatedColorsRenderer]


class GraduatedColorsRenderer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Graduated Color Renderer"
        self.description = "create a graduated colored map based on a specific attribute of a layer"
        self.canRunInBackground = False
        self.category = "MapTools"

    def getParameterInfo(self):
        """Define parameter definitions"""
        #original project name
        param0 = arcpy.Parameter(
            displayName="Input ArcGIS Pro Project Name",
            name="aprxInputName",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        #parameter of which layer you want to classify to create a color map
        param1 = arcpy.Parameter(
            displayName="Layer to Classify",
            name="LayertoClassify",
            datatype="GPLayer",
            parameterType="Required",
            direction="Input"
        )
        #output folder location
        param2 = arcpy.Parameter(
            displayName="Output Location",
            name="OutputLocation",
            datatype="DEFolder",
            direction="Input"
        )
        #output project name
        param3 = arcpy.Parameter(
            displayName="Output Project Name",
            name="OutputProjectName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        #Define Progressor Variables
        readTime = 3
        start = 0
        max = 100
        step = 33

        #Setup Progressor
        arcpy.SetProgressor("step", "Validating Project File...", start, max, step)
        time.sleep(readTime)
        arcpy.AddMessage("Validating Project File...")

        #assign the variable project, Project File for map production submodule
        project = arcpy.mp.ArcGISProject(parameters[0].valueAsText)

        #Where to get the first map from the .aprx/arcgis project aprx, define campus as an object from a map
        campus = project.ListMaps('Map')[0]

        #Increment the Progressor for 33%
        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Finding your map layer...")
        time.sleep(readTime)
        arcpy.AddMessage("Finding your map layer...")

        #Loop through the layers of the map
        for layer in campus.listLayers():
            #Check the layer's symbology
            if layer.isFeatureLayer:
                #Copy the layer's symbology
                symbology = layer.symbology
                #Make sure the symbology has rendere attribute
                if hasattr(symbology, 'renderer'):
                    #Check the layer name
                    if layer.name == parameters[1].valueAsText: #will check if the layer name mathces the input layer

                        #Increment the Progressor for 33%
                        arcpy.SetProgressorPosition(start + step)
                        arcpy.SetProgressorLabel("Calculating and classifying...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Calculating and classifying...")

                        #Update the Copy's Renderer to "Graduated Colors Renderer"
                        symbology.updateRenderer('GraduatedColorsRenderer')

                        #Tell arcpy which field we want to base our chloropleth off of
                        symbology.renderer.classificationsField = "Shape_Area"

                        #Increment the Progressor for 66%
                        arcpy.SetProgressorPosition(start + step*2)
                        arcpy.SetProgressorLabel("Cleaning up...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Cleaning up...")

                        #Set how many classes on the map
                        symbology.renderer.breakCount = 5

                        #Set the color ramp on map
                        symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]

                        #Set the layer's actual symbology equal to the Copy's symbology
                        layer.symbology = symbology

                        arcpy.AddMessage("Finish Generating Layer...")
                    else:
                        print("No feature layers found")

        #Increment the Progressor for 99%
        arcpy.SetProgressorPosition(start + step*3)
        arcpy.SetProgressorLabel("Saving...")
        time.sleep(readTime)
        rcpy.AddMessage("Saving...")

        #Tell where to save the new copy and how to name it with parameters 2 and 3
        project.saveACopy(parameters[2].valueAsText + "\\" + parameters[3].valueAsText + "aprx")

        return







        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
