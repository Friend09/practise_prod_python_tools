#!/usr/bin/env python3
"""
PySpark Setup and Test Script
This script sets up the environment and tests PySpark installation.
"""

import os
import sys
from pathlib import Path


def setup_environment():
    """Set up environment variables for PySpark"""
    print("Setting up PySpark environment...")

    # Set environment variables
    os.environ['JAVA_HOME'] = (
        '/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home'
    )
    os.environ['SPARK_HOME'] = (
        '/opt/homebrew/Cellar/apache-spark/4.0.0/libexec'
    )
    os.environ['PYSPARK_PYTHON'] = sys.executable

    print(f"✅ JAVA_HOME: {os.environ.get('JAVA_HOME')}")
    print(f"✅ SPARK_HOME: {os.environ.get('SPARK_HOME')}")
    print(f"✅ PYSPARK_PYTHON: {os.environ.get('PYSPARK_PYTHON')}")


def test_pyspark():
    """Test PySpark installation"""
    print("\n" + "=" * 50)
    print("Testing PySpark Installation")
    print("=" * 50)

    try:
        from pyspark.sql import SparkSession
        from pyspark.sql.functions import avg

        # Create SparkSession
        spark = SparkSession.builder \
            .appName("PySpark Test") \
            .config("spark.sql.adaptive.enabled", "true") \
            .getOrCreate()

        print(f"✅ Spark Version: {spark.version}")
        print(f"✅ Spark Context: {spark.sparkContext}")
        print(f"✅ Application Name: {spark.sparkContext.appName}")

        # Test with sample data
        data = [
            ("Alice", 25, 75000),
            ("Bob", 30, 85000),
            ("Charlie", 35, 95000),
        ]

        df = spark.createDataFrame(data, ["name", "age", "salary"])

        print("\n📊 Sample DataFrame:")
        df.show()

        print("📈 Basic operations:")
        print(f"   Count: {df.count()}")
        print(f"   Average salary: {df.agg(avg('salary')).collect()[0][0]:.2f}")

        # Test SQL
        df.createOrReplaceTempView("employees")
        result = spark.sql(
            "SELECT name, salary FROM employees WHERE salary > 80000"
        )
        print("\n🔍 SQL Query result (salary > 80000):")
        result.show()

        # Clean up
        spark.stop()
        print("\n✅ PySpark test completed successfully!")
        return True

    except Exception as e:
        print(f"❌ PySpark test failed: {str(e)}")
        return False


def create_env_file():
    """Create a .env file with PySpark environment variables"""
    env_content = (
        "# PySpark Environment Variables\n"
        "export JAVA_HOME=/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home\n"
        "export SPARK_HOME=/opt/homebrew/Cellar/apache-spark/4.0.0/libexec\n"
        "export PYSPARK_PYTHON=python3\n"
        "export PATH=$SPARK_HOME/bin:$PATH\n"
    )

    env_file = Path(".env_pyspark")
    with open(env_file, "w") as f:
        f.write(env_content)

    print(f"\n📝 Created {env_file} with environment variables")
    print("To use these variables, run: source .env_pyspark")


def main():
    """Main function"""
    print("🚀 PySpark Setup and Test")
    print("=" * 30)

    # Setup environment
    setup_environment()

    # Test PySpark
    success = test_pyspark()

    # Create env file
    create_env_file()

    if success:
        print("\n🎉 Setup completed successfully!")
        print("\nNext steps:")
        print(
            "1. Open the Jupyter notebook: "
            "jupyter lab notebooks/pyspark_crash_course.ipynb"
        )
        print(
            "2. Or run: source .env_pyspark && jupyter lab"
        )
        print("3. Start learning PySpark! 📚")
    else:
        print(
            "\n⚠️  Setup completed with issues. "
            "Check the error messages above."
        )


if __name__ == "__main__":
    main()
