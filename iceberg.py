from pyspark.sql import SparkSession

from pyspark.sql import SparkSession

hdfs_url = "hdfs://10.0.17.76:8020"  # Your HDFS NameNode
warehouse_path = f"{hdfs_url}/iceberg-warehouse" # Root directory for all Iceberg data

spark = (
    SparkSession.builder
    .appName("IcebergHadoopCatalog")
    .config("spark.hadoop.fs.defaultFS", hdfs_url)
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    
    # Configure the 'iceberg' catalog to use Hadoop type
    .config("spark.sql.catalog.iceberg", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.iceberg.type", "hadoop")
    .config("spark.sql.catalog.iceberg.warehouse", warehouse_path)
    
    # Optional: Keep spark_catalog as Hive if you have other Hive tables, 
    # but set it to 'hadoop' too if you ONLY use Iceberg and no Hive metastore.
    # If you don't have Hive Metastore, you might need to disable spark_catalog or set it to hadoop as well.
    .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog")
    .config("spark.sql.catalog.spark_catalog.type", "hadoop") 
    .config("spark.sql.catalog.spark_catalog.warehouse", warehouse_path)

    .config("datanucleus.schema.autoCreateTables", "true")
    .config("datanucleus.autoCreateSchema", "true")
    .config("datanucleus.fixedDatastore", "false")
    
    .getOrCreate()
)   


catalog_name = "iceberg"
db_name = "glif"
table_name = "glif_txns"


spark.sql(f"CREATE DATABASE IF NOT EXISTS {catalog_name}.{db_name}")





  























# import sys
# import pkg_resources
# import pyspark
# from pyspark.sql import SparkSession

# # Build Spark session with Delta & Iceberg configurations
# spark = SparkSession.builder \
#     .appName("CheckLibraryVersions") \
#     .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension, org.apache.iceberg.spark.SparkSessionExtensions") \
#     .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog") \
#     .config("spark.sql.catalog.spark_catalog.type", "hive") \
#     .getOrCreate()

# print("="*60)
# print("PYTHON AND SPARK ENVIRONMENT VERSIONS")
# print("="*60)
# print(f"Python Version: {sys.version.split()[0]}")
# print(f"PySpark Version: {pyspark.__version__}")

# # List of libraries to check
# libraries = [
#     "delta-spark",
#     "confluent-kafka",
#     "scikit-learn",
#     "pandas",
#     "torch",
#     "transformers",
#     "spacy",
#     "nltk",
#     "iceberg"
# ]

# print("\n" + "="*60)
# print("ADDITIONAL LIBRARY VERSIONS")
# print("="*60)

# for lib in libraries:
#     try:
#         version = pkg_resources.get_distribution(lib).version
#         print(f"{lib:<25} : {version}")
#     except pkg_resources.DistributionNotFound:
#         # Fallback check for iceberg-spark-runtime if the python wrapper isn't explicitly installed
#         if lib == "iceberg":
#             try:
#                 # Retrieve from Java SparkContext
#                 sc = spark.sparkContext
#                 manifest = sc.getConf().get("spark.jars", "")
#                 if "iceberg" in manifest.lower():
#                     print(f"{lib:<25} : (Provided via Spark Jars: {manifest.split('/')[-1]})")
#                 else:
#                     print(f"{lib:<25} : Not found in Python environment or Spark Jars")
#             except Exception:
#                 print(f"{lib:<25} : Not found")
#         else:
#             print(f"{lib:<25} : Not found")

# spark.stop()
# print("="*60)





# ============================================================
# PYTHON AND SPARK ENVIRONMENT VERSIONS
# ============================================================
# Python Version: 3.10.12
# PySpark Version: 4.1.2

# ============================================================
# ADDITIONAL LIBRARY VERSIONS
# ============================================================
# delta-spark               : 4.3.1
# confluent-kafka           : 2.15.0
# scikit-learn              : 1.7.2
# pandas                    : 2.3.3
# torch                     : 2.13.0+cpu
# transformers              : 5.14.1
# spacy                     : 3.8.14
# nltk                      : 3.10.0
# iceberg                   : Not found in Python environment or Spark Jars
