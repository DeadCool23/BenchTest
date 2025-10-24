import matplotlib.pyplot as plt
from matplotlib.figure import Figure

ACTIX_COLOR = "#613DFF"
AXUM_COLOR = "#FF2222"

PERCENTILES = [0.5, 0.75, 0.9, 0.95, 0.99]

def plot_resources_graph(
    ax, 
    data: tuple[list[int], list[list[int]]], 
    y_label: str,
    label: str,
    color: str
):
    x = data[0]
    y_min = data[1][0]
    y_med = data[1][1]
    y_max = data[1][2]

    yerr = [y_med - y_min, y_max - y_med]

    ax.errorbar(x, y_med, yerr=yerr, fmt='none', ecolor=color, elinewidth=1, capsize=2, alpha=0.7)
    ax.plot(
        x, 
        y_med, 
        color=color, 
        marker="_", 
        markersize=12,
        markeredgecolor="black",
        label=label
    )

    ax.set_xlabel("Количество пользователей")
    ax.set_ylabel(y_label)
    ax.grid(True)
    ax.legend()

def plot_resources_cmp_graph(axum_data: tuple[list[int], list[list[int]]], actix_data: tuple[list[int], list[list[int]]], y_label: str) -> Figure:
    fig, ax = plt.subplots(figsize=(18, 5))

    plot_resources_graph(
        ax,
        axum_data,
        y_label,
        "Axum",
        AXUM_COLOR,
    )
    plot_resources_graph(
        ax,
        actix_data,
        y_label,
        "Actix",
        ACTIX_COLOR,
    )
    ax.set_title(f"График {y_label}")

    plt.tight_layout()
    return fig

def plot_time_graph(ax, axum_data: tuple[list[int], list[int]], actix_data: tuple[list[int], list[int]]):
    ax.plot(axum_data[0], axum_data[1], marker='o', linestyle='-', label="Axum", color=AXUM_COLOR)
    ax.plot(actix_data[0], actix_data[1], marker='o', linestyle='-', label="Actix", color=ACTIX_COLOR)
    ax.set_xlabel("Количество пользователей")
    ax.set_ylabel("Среднее время отклика (мс)")
    ax.set_title("График времени отклика")
    ax.legend()
    ax.grid(True)

def plot_histogram(ax, axum_data: list[int], actix_data: list[int]):
    ax.hist(axum_data, bins=10, alpha=0.6, label="Axum", color=AXUM_COLOR)
    ax.hist(actix_data, bins=10, alpha=0.6, label="Actix", color=ACTIX_COLOR)
    ax.set_xlabel("Среднее время отклика (мс)")
    ax.set_ylabel("Количество наблюдений")
    ax.set_title("Распределение время отклика")
    ax.legend()
    ax.grid(True)


def plot_percentiles(ax, axum_data: list[int], actix_data: list[int]):
    axum_perc = axum_data.quantile(PERCENTILES)
    actix_perc = actix_data.quantile(PERCENTILES)

    ax.scatter(PERCENTILES, axum_perc, color=AXUM_COLOR, label="Axum", s=80)
    ax.scatter(PERCENTILES, actix_perc, color=ACTIX_COLOR, label="Actix", s=80)
    ax.set_xticks(PERCENTILES)
    ax.set_xticklabels([f"p{int(p*100)}" for p in PERCENTILES])
    ax.set_ylabel("Среднее время отклика (мс)")
    ax.set_title("Перцентили время отклика")
    ax.legend()
    ax.grid(True)

def time_cmp_plot(axum_data: tuple[list[int], list[int]], actix_data: tuple[list[int], list[int]]) -> Figure:
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    plot_time_graph(axes[0], axum_data, actix_data)
    plot_histogram(axes[1], axum_data[1], actix_data[1])
    plot_percentiles(axes[2], axum_data[1], actix_data[1])

    plt.tight_layout()
    return fig