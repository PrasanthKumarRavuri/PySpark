%fs ls dbfs:/databricks-datasets/asa/airlines/2007.csv
df1 = spark.read.format("csv").option("header",True
                                     df1.show()
                                     ).load("dbfs:/databricks-datasets/asa/airlines/2007.csv")
df1.show()
