# libraries & dataset
from typing import Any, List, Union

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def density_plot(
    xs: Union[List[Any], pd.DataFrame],
    shade: bool = True,
    bw: float = None,
    color: str = "olive",
) -> None:
    """Density plot."""
    sns.set(style="darkgrid")
    sns.kdeplot(data=xs, shade=shade, bw=bw, color=color, legend=True)
    plt.show()


if __name__ == "__main__":
    density_plot([1, 1, 3, 66, 3, 21, 2], bw=None)
    density_plot(pd.DataFrame({"a": [1, 1, 4, 55, 2, 11]})["a"])
    density_plot(pd.DataFrame({"a": [1, 1, 4, 55, 2, 11]}))
