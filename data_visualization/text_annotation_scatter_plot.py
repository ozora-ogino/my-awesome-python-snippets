from typing import Any, Dict

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def text_annotation_scatter_plot(
    df: pd.DataFrame,
    x: str,
    y: str,
    text: str,
    scatter_kws: Dict[str, Any] = None,
):
    """Scatter plot with text annotation.

    Args:
        df (pd.DataFrame): Input data.
        x (str): Column name for x axis.
        y (str): Column name for y axis.
        text (str): Column name for text annotation.
        scatter_kws (Dict[str, Any], optional): Scatter kwarg. Defaults to None.
    """
    sns.regplot(data=df, x=x, y=y, fit_reg=False, marker="o", scatter_kws=scatter_kws)
    for line in range(len(df)):
        plt.text(
            df[x][line],
            df[y][line] + 0.01,  # Offset.
            df[text][line],
            horizontalalignment="center",
            size="small",  # Text size.
            color="black",  # Text color.
        )
    plt.show()


if __name__ == "__main__":
    _df = pd.DataFrame(
        {
            "x": [0, 1, 2, 3, 4],
            "y": [2, 5, 1, 4, 0],
            "size": [23, 100, 20, 31, 42],
            "text": ["A", "B", "C", "D", "E"],
            "color": ["#BA61FF", "#BA61FF", "#91FF61", "#91FF61", "#91FF61"],
        }
    )
    _scatter_kws = {"s": _df["size"], "c": _df["color"], "color": None}
    text_annotation_scatter_plot(_df, "x", "y", "text", _scatter_kws)
