# Databricks notebook source
# MAGIC %pip install "kedro[spark.SparkDataSet]~=0.18.2"

# COMMAND ----------

from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project

project_root = "/Workspace/Repos/tuan_lam@saveonfoods.com/iris_databricks" 
bootstrap_project(project_root)

with KedroSession.create(project_path=project_root) as session:
    session.run()
