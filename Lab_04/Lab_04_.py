import arcpy

arcpy.env.workspace = 'I:\GEOG676\python_env'
folder_path = r'I:\GEOG676\Lab_04'
gdb_name = 'Lab4_stuff.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r'I:\GEOG676\Lab_04\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

#connect to the campus gdb and copy the buildings feature layer to my gdb
campus = r'I:\GEOG676\Lab_04\Campus.gdb'
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

#Reprojectiing
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

#Buffering
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + 'Garage_Points_buffered', 150)

#Intersecting
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_Intersection', 'All')

#Create a table to be read in excel
arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_Intersection.dbf', 'I:\GEOG676\Lab_04', 'nearbyBuildings.csv')

