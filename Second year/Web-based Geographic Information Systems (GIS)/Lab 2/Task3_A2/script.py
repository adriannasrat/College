from qgis.core import QgsVectorLayer, QgsProject, QgsSymbol, QgsRendererCategory, QgsCategorizedSymbolRenderer
from qgis.utils import iface
import os
base_path = "/Users/adrian/Documents/DU/Andra året/GIS/Lab 2 - GIS/Lab_02/Task3_A2"
road_path = os.path.join(base_path, "ROAD_CENTERLINES.shp")
road_layer = QgsVectorLayer(road_path, "road", "ogr")
if road_layer.isValid():
    symbol = QgsSymbol.defaultSymbol(road_layer.geometryType())
    symbol.setColor(QColor("black"))
    road_layer.renderer().setSymbol(symbol)
    QgsProject.instance().addMapLayer(road_layer)
    
    building_path = os.path.join(base_path, "BUILDINGS.shp")
building_layer = QgsVectorLayer(building_path, "Building", "ogr")
if building_layer.isValid():
    symbol = QgsSymbol.defaultSymbol(building_layer.geometryType())
    symbol.setColor(QColor("orange"))
    building_layer.renderer().setSymbol(symbol)
    QgsProject.instance().addMapLayer(building_layer)
    
    sidewalks_path = os.path.join(base_path, "SIDEWALKS.shp")
sidewalks_layer = QgsVectorLayer(sidewalks_path, "sidewalks", "ogr")
if sidewalks_layer.isValid():
    symbol = QgsSymbol.defaultSymbol(sidewalks_layer.geometryType())
    symbol.setColor(QColor("red"))
    sidewalks_layer.renderer().setSymbol(symbol)
    QgsProject.instance().addMapLayer(sidewalks_layer)
    
    intersections_path = os.path.join(base_path, "INTERSECTIONS.shp")
intersections_layer = QgsVectorLayer(intersections_path, "Intersections", "ogr")
if intersections_layer.isValid():
    symbol = QgsSymbol.defaultSymbol(intersections_layer.geometryType())
    symbol.setColor(QColor("gray"))
    intersections_layer.renderer().setSymbol(symbol)
    QgsProject.instance().addMapLayer(intersections_layer)

csv_output_path = os.path.join(base_path, "task3_a2", "Intersections.csv")
QgsVectorFileWriter.writeAsVectorFormat(intersections_layer, csv_output_path, "utf-8", intersections_layer.crs(), "CSV")
print("Intersections exported to:", csv_output_path)