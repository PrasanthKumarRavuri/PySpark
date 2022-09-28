# Databricks notebook source
# MAGIC %fs ls dbfs:/databricks-datasets/asa/airlines

# COMMAND ----------

df1 = spark.read.csv("dbfs:/databricks-datasets/asa/airlines/2007.csv",header=False)

# COMMAND ----------

display(df1)

# COMMAND ----------

df1.count()

# COMMAND ----------

df1.write.format("delta").mode("overwrite").saveAsTable("airlines1")

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from airlines1

# COMMAND ----------

# MAGIC %fs ls /user/hive/warehouse/airlines1

# COMMAND ----------

spark.conf.get("spark.sql.warehouse.dir")

# COMMAND ----------

# MAGIC %sh ls

# COMMAND ----------

# MAGIC %fs ls file:/root/

# COMMAND ----------


