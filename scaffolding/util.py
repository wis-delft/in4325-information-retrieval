from pathlib import Path
from typing import Callable, Optional

import pandas as pd
import pyterrier as pt


DATASET = pt.datasets.get_dataset("irds:antique/test/non-offensive")
INDEX = pt.index.IterDictIndexer(
    str(Path.cwd()),
    meta={
        "docno": 32,
        "text": 131072,
    },
    type=pt.index.IndexingType.MEMORY,
).index(DATASET.get_corpus_iter())
BM25 = pt.BatchRetrieve(
    INDEX,
    wmodel="BM25",
    metadata=["docno", "text"],
    properties={"termpipelines": ""},
    controls={"qe": "off"},
)


def search(query: str) -> pd.DataFrame:
    return (BM25 % 10).search(query)


def evaluate(
    df: pd.DataFrame, rewrite_func: Optional[Callable[[str], str]] = None
) -> float:
    if rewrite_func is None:
        pl = BM25
    else:
        pl = pt.apply.query(lambda q: rewrite_func(q["query"])) >> BM25
    return pt.Experiment(
        [pl],
        df,
        DATASET.get_qrels(),
        eval_metrics=["map"],
    )["map"][0]


def evaluate_all(rewrite_func: Optional[Callable[[str], str]] = None) -> float:
    return evaluate(DATASET.get_topics(), rewrite_func)
