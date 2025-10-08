"""
Fix for DuckDB connection in ibis

The error message indicates an issue with connecting to DuckDB.
Instead of using the generic `ibis.connect()` method with a URI,
you should use the specific DuckDB backend connector.
"""

import ibis

# Initialize ibis for interactive mode
ibis.options.interactive = True

# INCORRECT way (causing the error):
# con = ibis.connect("duckdb:///Users/vamsi_mbmax/Developer/VAM_Documents/01_vam_PROJECTS/LEARNING/proj_Productivity/dev_proj_Productivity/practise_prod_python_tools/data/birthdays.ddb")

# CORRECT way - use the specific DuckDB backend connector:
con = ibis.duckdb.connect('data/birthdays.ddb')

# Now you can query your data
# For example:
if ibis.options.interactive:
    print("Connection successful!")
    # You can uncomment and use the following to view data:
    # tbl = con.table('birthdays')
    # print(tbl.head())
