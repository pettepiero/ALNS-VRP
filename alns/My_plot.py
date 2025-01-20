import matplotlib.pyplot as plt


def plot_solution(
    data,
    solution,
    name="CVRP solution",
    idx_annotations=True,
    figsize=(12, 10),
    save=False,
    folder_name=None,
):
    """
    Plot the routes of the passed-in solution.
    """
    fig, ax = plt.subplots(figsize=figsize)
    cmap = plt.get_cmap("Set2", data["vehicles"])
    cmap

    for idx, route in enumerate(solution.routes):
        ax.plot(
            [data["node_coord"][loc][0] for loc in route.customers_list],
            [data["node_coord"][loc][1] for loc in route.customers_list],
            color=cmap(idx),
            marker=".",
            label=f"Vehicle {idx}",
        )

    for i in range(1, data["dimension"]):
        customer = data["node_coord"][i]
        ax.plot(customer[0], customer[1], "o", c="tab:blue")
        if idx_annotations:
            ax.annotate(i, (customer[0], customer[1]))

    # for idx, customer in enumerate(data["node_coord"][:data["dimension"]]):
    #     ax.plot(customer[0], customer[1], "o", c="tab:blue")
    #     ax.annotate(idx, (customer[0], customer[1]))

    # Plot the depot
    kwargs = dict(zorder=3, marker="X")

    for i in range(data["dimension"], data["dimension"] + data["n_depots"]):
        depot = data["node_coord"][i]
        ax.plot(depot[0], depot[1], c="tab:red", **kwargs, label=f"Depot {i}")
        if idx_annotations:
            ax.annotate(i, (depot[0], depot[1]))

    # for idx, depot in enumerate(data["depots"]):
    #     ax.scatter(*data["node_coord"][depot], label=f"Depot {depot}", c=cmap(idx), **kwargs)
    #     ax.annotate(idx, (data["node_coord"][depot][0], data["node_coord"][depot][1]))

    ax.scatter(*data["node_coord"][0], c="tab:red", label="Depot 0", **kwargs)

    ax.set_title(
        f"{name}\n Total distance: {solution.cost},\n Total unassigned: {len(solution.unassigned)}"
    )
    ax.set_xlabel("X-coordinate")
    ax.set_ylabel("Y-coordinate")
    ax.legend(frameon=False, ncol=3)

    if save:
        plt.savefig(f"{folder_name}/{name}")
        plt.close()
