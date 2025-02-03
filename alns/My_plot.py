import matplotlib.pyplot as plt

def plot_solution(
    solution,
    name="CVRP solution",
    idx_annotations=False,
    figsize=(12, 10),
    save=False,
    save_path="./outputs/plots",
    cordeau: bool = True,
):
    """
    Plot the routes of the passed-in solution. If cordeau is True, the first customer is ignored.
        Parameters:
            solution: CvrptwState
                The solution to be plotted.
            name: str
                The name of the plot.
            idx_annotations: bool
                If True, the customer indices are plotted.
            figsize: tuple
                The size of the plot.
            save: bool
                If True, the plot is saved in "./plots".
            cordeau: bool
                If True, the first customer is ignored.

    """
    df = solution.nodes_df
    start_idx = 1 if cordeau else 0
    fig, ax = plt.subplots(figsize=figsize)
    cmap = plt.get_cmap("Set2", len(solution.routes))
    cmap
    # Plot the routes
    for idx, route in enumerate(solution.routes):
        ax.plot(
            [df.loc[loc, "x"].item() for loc in route.customers_list],
            [df.loc[loc, "y"].item() for loc in route.customers_list],
            color=cmap(idx),
            marker=".",
            label=f"Vehicle {route.vehicle}",
        )

    # Plot the customers
    for i in range(start_idx, solution.n_customers + 1):
        customer = df.loc[i, ["x", "y"]]
        # customer = customer.values[0]
        ax.plot(customer.iloc[0], customer.iloc[1], "o", c="tab:blue")
        if idx_annotations:
            ax.annotate(i, (customer[0], customer[1]))

    # Plot the depot
    kwargs = dict(zorder=3, marker="X")

    for i, dep in enumerate(solution.depots["depots_indices"]):
        coords = solution.depots["coords"][i]
        ax.plot(coords[0], coords[1], c="tab:red", **kwargs, label=f"Depot {dep}")
        if idx_annotations:
            ax.annotate(dep, (coords[0], coords[1]))

    ax.set_title(
        f"{name}\n Total distance: {solution.cost}\n Total unassigned: {len(solution.unassigned)}"
    )
    ax.set_xlabel("X-coordinate")
    ax.set_ylabel("Y-coordinate")
    ax.legend(frameon=False, ncol=3)

    if save:
        plt.savefig(f"{save_path}/{name}.png")
        plt.close()
