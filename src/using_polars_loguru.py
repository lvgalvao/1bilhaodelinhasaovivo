import polars as pl
import time
from loguru import logger

start_time = time.time()

logger.info("Início do processamento dos dados")

# Ler o arquivo de dados
df = pl.scan_csv(
    "data/measurements.txt",
    separator=";",
    has_header=False,
    with_column_names=lambda cols: ["station_name", "measurement"],
)

# Agrupar dados
grouped = (
    df.group_by("station_name")
    .agg(
        pl.min("measurement").alias("min_measurement"),
        pl.mean("measurement").alias("mean_measurement"),
        pl.max("measurement").alias("max_measurement"),
    )
    .sort("station_name")
    .collect(streaming=True)
)

# Print resultados finais
logger.info("Resultados finais:")
print("{", end="")
for data in grouped.iter_rows():
    print(
        f"{data[0]}={data[1]:.1f}/{data[2]:.1f}/{data[3]:.1f}",
        end=", ",
    )
print("\b\b} ")

took = time.time() - start_time
logger.info(f"Processamento concluído em {took:.2f} segundos")
