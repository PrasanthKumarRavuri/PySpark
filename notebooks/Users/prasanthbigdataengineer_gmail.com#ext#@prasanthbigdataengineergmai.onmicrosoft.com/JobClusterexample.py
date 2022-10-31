# Databricks notebook source
# MAGIC %fs ls /databricks-datasets/asa/

# COMMAND ----------

df1 = spark.read.csv("dbfs:/FileStore/tables/emp.csv",header=True)

# COMMAND ----------

df1.show()

# COMMAND ----------

