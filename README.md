# HANCESTRO parsing

Run simple script to load HANCESTRO into BioCypher and parse contents.

```bash
git clone https://github.com/biocypher/hancestro.git
cd hancestro
poetry install
poetry run python parse_hancestro.py
```

Currently, labels and IDs are swapped in the read-in process in BioCypher. This
can be deactivated.