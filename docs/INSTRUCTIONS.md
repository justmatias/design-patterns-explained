# How to execute code examples

To run the code examples in this repository, follow these steps:

1. **Install uv**: If you don't have uv installed, follow the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).

2. **Install dependencies**: Navigate to the root directory of the repository and install the required dependencies.

    ```sh
    uv sync --group dev
    ```

3. **Run the example**: Use the following command to run a specific design pattern example. Replace `<category>` and `<pattern_name>` with the pattern you want to execute.

    ```sh
    uv run python creational/<pattern_name>/<pattern_name>.py
    ```

    For example, to run the Singleton example:

    ```sh
    uv run python creational/singleton/singleton.py
    ```
