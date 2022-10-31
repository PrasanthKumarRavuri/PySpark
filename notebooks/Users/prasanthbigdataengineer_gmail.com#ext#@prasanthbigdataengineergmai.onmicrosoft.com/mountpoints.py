# Databricks notebook source
# MAGIC %md
# MAGIC ### BLOB Storage

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

dbutils.fs.mount(
  source = "wasbs://<container-name>@<storage-account-name>.blob.core.windows.net",
  mount_point = "/mnt/iotdata",
  extra_configs = {"fs.azure.account.key.<storage-account-name>.blob.core.windows.net":dbutils.secrets.get(scope = "<scope-name>", key = "<key-name>")})

# COMMAND ----------

dbutils.fs.mount(
  source = "wasbs://blobcontainer@blobstorageazure137.blob.core.windows.net",
  mount_point = "/mnt/blobcontainer",
  extra_configs = {"fs.azure.account.key.blobstorageazure137.blob.core.windows.net":"wdlFMQdcxpCBE8lIPXRE0D0oHe8iq0W4SsoBtMhRh3P39zzA0ls6ln6y9OFuiB3x+bi97MXqJSPK+AStFBsOPw=="})

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

df = spark.read.format("csv").option("header",True).load("/mnt/blobcontainer")

# COMMAND ----------

df.show()

# COMMAND ----------

dbutils.fs.unmount("/mnt/blobcontainer")

# COMMAND ----------

dbutils.fs.mount(
  source = "wasbs://blobcontainer@blobstorageazure137.blob.core.windows.net",
  mount_point = "/mnt/blobcontainer1",
  extra_configs = {"fs.azure.account.key.blobstorageazure137.blob.core.windows.net":dbutils.secrets.get(scope = "adb-scope", key = "akv-blob-account-key")})

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

# MAGIC %fs ls /mnt/blobcontainer1

# COMMAND ----------

df1 = spark.read.format("csv").option("header",True).load("/mnt/blobcontainer1")

# COMMAND ----------

df1.show()

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.fs.unmount("/mnt/blobcontainer1")

# COMMAND ----------

# MAGIC %md
# MAGIC ### GEN-2 BLOB

# COMMAND ----------

# MAGIC %md
# MAGIC #### method1(by creating mountpoint)

# COMMAND ----------

dbutils.fs.mount(
  source = "wasbs://adlsgen2container@adlsgen2storage137.blob.core.windows.net",
  mount_point = "/mnt/adlsgen2container",
  extra_configs = {"fs.azure.account.key.adlsgen2storage137.blob.core.windows.net":dbutils.secrets.get(scope = "adb-scope", key = "akv-GEN2-BLOB")})

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

# MAGIC %fs ls /mnt/adlsgen2container

# COMMAND ----------

# MAGIC %md
# MAGIC #### method2(without creating mount point)

# COMMAND ----------

spark.conf.set("fs.azure.account.key.adlsgen2storage137.dfs.core.windows.net","2HaEio5vU5D5DSYinnVAmpFYv7ZpCnsY8YclUgflAEa1pBzM7w4UgpwWOqu/hle3TAFziybvrhiM+AStZByJ9Q==")
spark.conf.set("fs.azure.createRemoteFileSystemDuringInitialization", "true")

# COMMAND ----------

dbutils.fs.ls("abfss://adlsgen2container@adlsgen2storage137.dfs.core.windows.net/landing/sales/")

# COMMAND ----------

# MAGIC %md
# MAGIC #### method3(by creating mount point with service principle)

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": <client-id>,
"fs.azure.account.oauth2.client.secret": <service-credential>,
"fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<directory-id>/oauth2/token"}

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://<file_system>@<storage-account-name>.dfs.core.windows.net/",
  mount_point = "/mnt/mymount",
  extra_configs = configs)

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": "7596e134-dc62-45d3-81ba-8f74712971a4",
"fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="adb-scope",key="akv-GEN2-APP-key"),
"fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/2c34584c-7a60-48b7-9a8c-0a50b4c51d4f/oauth2/token"}

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://adlsgen2container@adlsgen2storage137.dfs.core.windows.net/",
  mount_point = "/mnt/mymount",
  extra_configs = configs)

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

# MAGIC %fs ls /mnt/mymount/

# COMMAND ----------


