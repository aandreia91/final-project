Program for Cultural Heritage Final Project

Object Records at the Fogg Museum

This project shows the number of records of different categories from the “Objects” section of the Fogg Museum. Through a Harvard API key 2332 pages of data were scrapped and using Python they were converted into json files.

Each json file contains the whole database of the objects and all the information. For this project, only the section “people”, inside “records” were chosen to be analyzed. Once compressing all json files into one, the file was exported to Tableau for the creation of graphs, representing:

-	The artists name
-	The artists birthplace
-	The artists deathplace
-	The artists gender
-	The artists culture
-	The display dates

After creating graphs, each data was exported as an Excel file, so the data can be retrieved without the need to run the Tableau Software.

To run the data and directly see the finished graphs, open the Final Project_PCH.twb, but you need Tableau to open it.
To view the data on Tableau, the file finaldump.json.zip should be exported, and once in Tableau each category under “people” must be matched with the number of records.
To view the data without running Tableau, download the fogg_data_excel.zip.
To view each individual page in json, select the following files: foggdata_json1.zip, foggdata_json2.zip and foggdata_json3.zip
To view a still image of what will happen if the data is exported to Tableau, select the graphs.png

Any other files were created to support the exported data.
