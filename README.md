# Pre-commit Hook for Uncrustify

This project provides a pre-commit hook for [pre-commit](https://github.com/pre-commit/pre-commit) that runs [Uncrustify](https://github.com/uncrustify/uncrustify) on C/C++ files. The hook is cross-platform and supports both Unix-like systems and Windows.

## Features

- Detects the Uncrustify version.
- Uses the `--max-passes` option if the Uncrustify version is 3.00 or higher.
- Implements the `--max-passes` functionality if the Uncrustify version is lower than 3.00.

## Installation

1. Install [pre-commit](https://pre-commit.com/#install) if you haven't already.
2. Add the following configuration to your `.pre-commit-config.yaml` file:

```yaml
- repo: https://github.com/mdeweerd/pre-commit-uncrustify-hook
  rev: v1.0.0  # Replace with the latest version
  hooks:
    - id: uncrustify
      args:
        - -c
        - uncrustify.cfg
        - --max-passes=4
```

3. Run `pre-commit install` to set up the git hook scripts.

## Usage

The hook will automatically run Uncrustify on C/C++ files when you commit changes. It will use the configuration specified in `uncrustify.cfg`.

## Configuration

You can customize the Uncrustify configuration by modifying the `uncrustify.cfg` file in the root of your project.

## Examples

### Example 1: Using `--max-passes`

If you want to use the `--max-passes` option, you can specify it in your `.pre-commit-config.yaml` file:

```yaml
- repo: https://github.com/mdeweerd/pre-commit
  rev: v1.0.0  # Replace with the latest version
  hooks:
    - id: uncrustify
      args:
        - -c
        - uncrustify.cfg
        - --max-passes=4
```

### Example 2: Using Other Uncrustify Options

You can specify other Uncrustify options in your `.pre-commit-config.yaml` file. For example:

```yaml
- repo: https://github.com/mdeweerd/pre-commit
  rev: v1.0.0  # Replace with the latest version
  hooks:
    - id: uncrustify
      args:
        - -c
        - uncrustify.cfg
        - --indent=spaces=4
        - --newlines=1
```

## License

This project is licensed under the GPLv3 License. See the [LICENSE](LICENSE) file for details.
