import arcpy

#assign bands
source = r"I:\GEOG676\lab_7"
band1 = arcpy.sa.Raster(source + r"\Band_1.tif") # blue
band2 = arcpy.sa.Raster(source + r"\Band_2.tif") # green
band3 = arcpy.sa.Raster(source + r"\Band_3.tif") # red
band4 = arcpy.sa.Raster(source + r"\Band_4.tif") # NIR
combined = arcpy.CompositeBands_management([band1, band2, band3], source + r"\output_combined.tif")

#Make Hillshade
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(source + r"/DEM.tif", source + r"\output_hillshade.tif", azimuth, altitude, shadows, z_factor)

#Make Slope
output_measurement = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(source + r"\DEM.tif", source + r"\output_slopes.tif",output_measurement, z_factor)

print("success!")
