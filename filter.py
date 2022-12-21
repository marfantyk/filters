import polars as pl

csvFile = "./data/input/thrombophilia_risk.tsv"

df = pl.read_csv(csvFile, sep="\t")

df.head(3)