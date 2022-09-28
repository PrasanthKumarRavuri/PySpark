# Databricks notebook source
df6 = spark.read.format("csv").option("header",True).load("dbfs:/databricks-datasets/asa/airlines/2007.csv")

# COMMAND ----------

# MAGIC %fs ls databricks-datasets/asa/airlines/1987.csv

# COMMAND ----------

df6.show()

# COMMAND ----------


