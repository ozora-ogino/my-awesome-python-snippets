from typing import Dict

import pandas as pd
import seaborn as sns


def scatter_plot(df: pd.DataFrame, x: str, y: str, scatter_kws: Dict):
    """
    Example: https://github.com/ozora-ogino/my-awesome-python-snippets/pull/4
    """
    sns.regplot(data=df, x=x, y=y, fit_reg=False, marker="o", scatter_kws=scatter_kws)


if __name__ == "__main__":
    import numpy as np

    _df = pd.DataFrame(
        {
            "width": np.random.randn(1000) * 100,
            "height": np.random.randn(1000) * 100,
            "size": np.random.randn(1000) * 100,
        }
    )
    _scatter_kws = {"s": _df["size"], "color": "#69b3a2", "alpha": 0.4}
    scatter_plot(_df, "width", "height", _scatter_kws)
