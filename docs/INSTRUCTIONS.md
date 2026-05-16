# How to preview the documentation

The docs site is automatically deployed as a preview for every pull request. Once a PR is opened, a GitHub Actions workflow builds the site and deploys it to Cloudflare Pages. A bot will post a comment on the PR with the preview URL — no extra steps needed.

The preview reflects the exact state of the branch and updates on every new commit. It has no effect on the production site hosted on GitHub Pages.

# How to execute code examples

To run the code examples in this repository, follow these steps:

1. **Install uv**: If you don't have uv installed, follow the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).

2. **Install dependencies**: Navigate to the root directory of the repository and install the required dependencies.

    ```sh
    uv sync --group dev
    ```

3. **Run the example**: Use the following command to run a specific design pattern example. Replace `<category>` and `<pattern_name>` with the pattern you want to execute.

    ```sh
    uv run python <category>/<pattern_name>/<pattern_name>.py
    ```

    For example, to run the Singleton example:

    ```sh
    uv run python creational/singleton/singleton.py
    ```
