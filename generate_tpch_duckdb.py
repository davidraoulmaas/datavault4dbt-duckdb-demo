import os
import duckdb

def generate_tpch_duckdb(
        db_folder: str = 'dbt', 
        db_file: str = 'duckdb_sample_data.db'
    ) -> None:
    
    sql = """
        INSTALL tpch;
        LOAD tpch;
        CALL dbgen(sf = 1);
    """
    conn = duckdb.connect(os.path.join(db_folder,db_file))
    conn.execute(sql)
    conn.close()

if __name__ == "__main__":
    generate_tpch_duckdb()