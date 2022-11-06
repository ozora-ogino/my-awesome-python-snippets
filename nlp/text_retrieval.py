"""
Text similarity methods for text retrieval.
Distance base algorithms + fasttext are implemented.
"""
import os
from typing import Any, Callable, List

import fasttext
import fasttext.util
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def jaccard_similarity(xs: List[Any], ys: List[Any]) -> float:
    """Calculate Jaccard similarity."""
    set_intersection = set.intersection(set(xs), set(ys))
    num_intersection = len(set_intersection)
    set_union = set.union(set(ys), set(xs))
    num_union = len(set_union)
    # For avoiding zero division error.
    if num_union == 0:
        return 1
    return float(num_intersection) / num_union


def dice_similarity(xs: List[Any], ys: List[Any]) -> float:
    """Calculate Dice similarity."""
    set_intersection = set.intersection(set(xs), set(ys))
    num_intersection = len(set_intersection)
    # For avoiding zero division error.
    if len(xs) + len(ys) == 0:
        return 1.0
    return float(2.0 * num_intersection) / (len(xs) + len(ys))


def simpson_similarity(xs: List[Any], ys: List[Any]) -> float:
    """Calculate Simpson similarity."""
    set_intersection = set.intersection(set(xs), set(ys))
    num_intersection = len(set_intersection)
    # For avoiding zero division error.
    if min([len(xs), len(ys)]) == 0:
        return 1.0
    return float(num_intersection) / min([len(xs), len(ys)])


def fasttext_similarity() -> float:
    if not os.path.exists("cc.en.300.bin"):
        fasttext.util.download_model("en", if_exists="ignore")

    ft = fasttext.load_model("cc.en.300.bin")

    def _fasttext_similarity(xs: List[Any], ys: List[Any]):
        """Calculate cosine similarity based on FastText."""
        xs_vec = np.array(([ft.get_word_vector(x) for x in xs])).sum(axis=0) / len(xs)
        ys_vec = np.array(([ft.get_word_vector(y) for y in ys])).sum(axis=0) / len(ys)
        sim = cosine_similarity(xs_vec.reshape(1, -1), ys_vec.reshape(1, -1))
        return sim[0][0]

    return _fasttext_similarity


def similarity_search(text: str, target: str, similarity_func: Callable) -> str:
    """Search and extract most similar parts with `target` phrase from `text`."""
    # Preprocess texts.
    text = text.replace(".", "").replace(",", "").split()
    target = target.replace(".", "").replace(",", "").lower().split()
    # Validate length.
    if len(target) > len(text):
        raise RuntimeError("Target length must be lower than text's length.")

    candidates = [text[idx : idx + len(target)] for idx in range(len(text) - len(target) + 1)]
    max_idx = np.argmax([similarity_func([word.lower() for word in x], target) for x in candidates])
    return " ".join(candidates[max_idx])


if __name__ == "__main__":
    test_sets = [
        ("Hello World, I'm so happy and enjoy today.", "hello world"),
        (
            "Google Drive, part of Google Workspace, is a safe place to back up and access all your files from any device",
            "google drive",
        ),
        (
            "Google Drive, part of Google Workspace, is a safe place to back up and access all your files from any device",
            "google workspace",
        ),
        (
            "Google Drive, part of Google Workspace:2020, is a safe place to back up and access all your files from any device",
            "google workspace",
        ),
    ]
    fasttext_similarity_func = fasttext_similarity()
    for (_text, _target) in test_sets:
        print("text:", _text)
        print("target:", _target)
        print()
        print("Jaccard:", similarity_search(_text, _target, jaccard_similarity))
        print("DICE:", similarity_search(_text, _target, dice_similarity))
        print("Simpton:", similarity_search(_text, _target, simpson_similarity))
        print("FastText:", similarity_search(_text, _target, fasttext_similarity_func))
        print("=" * 50)
