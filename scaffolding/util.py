from pathlib import Path
from typing import Callable

import pandas as pd
import pyterrier as pt

if not pt.started():
    pt.init()

DATASET = pt.datasets.get_dataset("irds:antique/test/non-offensive")
IDX_PATH = Path("index").absolute()
if not (IDX_PATH / "data.properties").is_file():
    pt.index.IterDictIndexer(
        str(IDX_PATH),
        meta={
            "docno": 32,
            "text": 131072,
        },
    ).index(DATASET.get_corpus_iter())

BM25 = pt.BatchRetrieve(
    str(IDX_PATH),
    wmodel="BM25",
    metadata=["docno", "text"],
    properties={"termpipelines": ""},
    controls={"qe": "off"},
)


def search(query: str) -> pd.DataFrame:
    return (BM25 % 10).search(query)


def evaluate(df: pd.DataFrame, rewrite_func: Callable[[str], str] = None) -> float:
    if rewrite_func is None:
        pl = BM25
    else:
        pl = pt.apply.query(lambda q: rewrite_func(q["query"])) >> BM25
    return pt.Experiment(
        [pl],
        df,
        DATASET.get_qrels(),
        eval_metrics=["map"],
    )[
        "map"
    ][0]


def evaluate_all(rewrite_func: Callable[[str], str] = None) -> float:
    return evaluate(DATASET.get_topics(), rewrite_func)
