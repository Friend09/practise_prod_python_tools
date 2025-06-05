# PySpark Quick Start Guide

## 🎉 Installation Complete!

Your PySpark environment is now set up and ready to use. Here's what was installed:

- ✅ **Java 17** (required for Spark 4.0.0)
- ✅ **Apache Spark 4.0.0**
- ✅ **PySpark 4.0.0**
- ✅ **Jupyter Lab** with all necessary dependencies
- ✅ **Supporting libraries**: pandas, numpy, matplotlib, seaborn

## 🚀 Quick Start

### Option 1: Use Jupyter Notebook (Recommended)
```bash
# Activate virtual environment
source .venv/bin/activate

# Set environment variables
source .env_pyspark

# Start Jupyter Lab
jupyter lab notebooks/pyspark_crash_course.ipynb
```

### Option 2: Python Script
```bash
# Activate virtual environment
source .venv/bin/activate

# Run the test script
python pyspark_setup.py
```

### Option 3: Interactive Python
```bash
# Activate virtual environment and set environment
source .venv/bin/activate && source .env_pyspark

# Start Python
python

# Then in Python:
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()
```

## 📚 Learning Path

The **PySpark Crash Course Notebook** covers:

1. **Environment Setup** - Getting started with PySpark
2. **RDDs** - Resilient Distributed Datasets (low-level API)
3. **DataFrames** - High-level structured data API
4. **Data Loading/Saving** - CSV, JSON, Parquet formats
5. **Data Transformations** - Filtering, grouping, joining
6. **SQL Operations** - Using SQL queries on DataFrames
7. **Machine Learning** - MLlib for ML workflows
8. **Performance Optimization** - Caching, partitioning, broadcasting
9. **Best Practices** - Production-ready tips and tricks

## 🔧 Environment Variables

The following environment variables are set automatically:

```bash
export JAVA_HOME=/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home
export SPARK_HOME=/opt/homebrew/Cellar/apache-spark/4.0.0/libexec
export PYSPARK_PYTHON=python3
export PATH=$SPARK_HOME/bin:$PATH
```

## 📊 Sample Code

Here's a quick example to get you started:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

# Create SparkSession
spark = SparkSession.builder \
    .appName("QuickStart") \
    .getOrCreate()

# Create sample data
data = [("Alice", 25, 75000),
        ("Bob", 30, 85000),
        ("Charlie", 35, 95000)]

df = spark.createDataFrame(data, ["name", "age", "salary"])

# Show data
df.show()

# Basic operations
print(f"Count: {df.count()}")
print(f"Average salary: {df.agg(avg('salary')).collect()[0][0]}")

# SQL query
df.createOrReplaceTempView("employees")
result = spark.sql("SELECT name FROM employees WHERE salary > 80000")
result.show()

# Clean up
spark.stop()
```

## 🛠️ Troubleshooting

### Common Issues:

1. **Java Version Error**: Make sure Java 17 is installed and JAVA_HOME is set correctly
2. **Memory Issues**: Adjust Spark configuration for your system:
   ```python
   spark = SparkSession.builder \
       .appName("MyApp") \
       .config("spark.executor.memory", "2g") \
       .config("spark.driver.memory", "1g") \
       .getOrCreate()
   ```
3. **Port Conflicts**: If you see port binding errors, restart your terminal

### Useful Commands:
```bash
# Check Java version
java -version

# Check Spark installation
spark-shell --version

# Monitor Spark jobs
# Open http://localhost:4040 in browser when Spark is running
```

## 📖 Additional Resources

- [Official PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
- [Spark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [MLlib Guide](https://spark.apache.org/docs/latest/ml-guide.html)
- [Spark Configuration](https://spark.apache.org/docs/latest/configuration.html)

## 🎯 Next Steps

1. **Complete the Crash Course Notebook** - Work through all sections
2. **Practice with Real Data** - Try loading your own datasets
3. **Explore Spark Streaming** - Real-time data processing
4. **Learn Delta Lake** - ACID transactions for data lakes
5. **Deploy to Cloud** - AWS EMR, Databricks, or Google Dataproc

Happy Sparking! 🚀✨
