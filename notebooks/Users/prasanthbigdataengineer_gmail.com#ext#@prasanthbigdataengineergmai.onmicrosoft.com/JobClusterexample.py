# Databricks notebook source
# MAGIC %fs ls /databricks-datasets/asa/

# COMMAND ----------

df2 = spark.read.csv("dbfs:/FileStore/tables/emp.csv",header=True)

# COMMAND ----------

df2.show()

# COMMAND ----------


