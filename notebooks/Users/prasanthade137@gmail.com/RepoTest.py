# Databricks notebook source
df4 = spark.read.format("csv").option("header",True).load("dbfs:/databricks-datasets/asa/airlines/1987.csv")

# COMMAND ----------

# MAGIC %fs ls databricks-datasets/asa/airlines/1987.csv

# COMMAND ----------

df4.show()

# COMMAND ----------
