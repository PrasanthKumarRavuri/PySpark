# Databricks notebook source
# MAGIC %fs ls dbfs:/databricks-datasets/asa/airlines/2007.csv

# COMMAND ----------

df1 = spark.read.format("csv").option("header",True).load("dbfs:/databricks-datasets/asa/airlines/2007.csv")

# COMMAND ----------

df1.show()

# COMMAND ----------


