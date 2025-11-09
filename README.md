# Datavault4dbt on DuckDB demo

#### Introduction
This repository was made for Datavault2.0 training sessions. It is basically a fork of [datavault4dbt-snowflake-demo](https://github.com/ScalefreeCOM/datavault4dbt-snowflake-demo), but doesn't require any cloud services and can be run locally. 

To make it work, this repository uses an [unofficial version of datavault4dbt](https://github.com/davidraoulmaas/datavault4dbt) that supports duckdb.

```yaml
  - git: "https://github.com/davidraoulmaas/datavault4dbt.git"
    revision: 0.1.0
```

There are currently no plans to contribute to the official package. However, if there arises any need for official duckdb support, e.g. in context of [motherduck](https://motherduck.com), we are kind of ready.

#### Prerequisites
- Python: ">=3.9, <=3.12"

#### Setup
```bash
pip install poetry
poetry install --no-root
poetry run python generate_tpch_duckdb.py
cd dbt
dbt deps
dbt build
```

### Further reading
- [Blog Post](https://davidmaas.de/blog/datavault4dbtonduckdb)
- [datavault4dbt-snowflake-demo/README.md](https://github.com/ScalefreeCOM/datavault4dbt-snowflake-demo/blob/main/README.md)
- [Exploring datavault4dbt - Part 1](https://www.scalefree.com/blog/tools/exploring-datavault4dbt-a-practical-series-on-the-dbt-package-for-data-vault-2-0-vol-1-the-staging-layer/)
- [Exploring datavault4dbt - Part 2](https://www.scalefree.com/blog/tools/exploring-datavault4dbt-a-practical-series-on-the-dbt-package-for-data-vault-2-0-vol-2-standard-entities-in-the-raw-vault/)

#### 

#### Initial motiviation
This repository is meant to explore data vault 2.0 modelling, following ["Building a scalable data warehouse with data vault 2.0"](https://www.amazon.de/-/en/Building-Scalable-Data-Warehouse-Vault/dp/0128025107). There seem to be very helpful macros in [datavault4dbt](https://github.com/ScalefreeCOM/datavault4dbt), so I will try to use this package locally.  Since it supports PostgreSQL, I expect it to work on DuckDB as well (see [PostgreSQL Compatibility](https://duckdb.org/docs/stable/sql/dialect/postgresql_compatibility.html)). If DuckDB doesn't work, I will include a PostgreSQL docker container to connect to.
