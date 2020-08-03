# 
#   file: tbComponentLoad.sql
#	author: andromeda
#   desc: Load the CSV data into dbAlrosParts.main_tbcomponent table
#
LOAD DATA LOCAL INFILE "/home/alros.server/Public/Projekte/Python/Tutorial/Server/Django/alrosSite/alrosParts/SQL/tbComponent.csv"
INTO TABLE master_tbcomponent
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, compName, compTotal, compDesc, compPackage, compDist, compPartNum);
