# Foo

```yaml
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Install uv
        uses: astral-sh/setup-uv@v3
```

# Bar

```yaml
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4.0

      - name: Install uv
        uses: astral-sh/setup-uv@v2.0
```
