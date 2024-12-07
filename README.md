[![PyPI](https://img.shields.io/pypi/v/cloudpath.svg)](https://pypi.python.org/pypi/cloudpath/#history)

# 🗂️ Cloudpath

Optimized pathlib backend for Google Cloud.

A filesystem abstraction similar to `pathlib` that is extensible to new
filesystems. Comes with support for local filesystems and GCS buckets.

```python
path = cloudpath.Path('gs://bucket/path/to/file.txt')

# String operations
path.parent                           # gs://bucket/path/to
path.name                             # file.txt
path.stem                             # file
path.suffix                           # .txt

# File operations
path.read(mode='r')                   # Content of the file as string
path.read(mode='rb')                  # Content of the file as bytes
path.write(content, mode='w')         # Write string to the file
path.write(content, mode='wb')        # Write bytes to the file
with path.open(mode='r') as f:        # Create a file pointer
  pass

# File system checks
path.parent.glob('*')                 # Get all sibling paths
path.exists()                         # True
path.isdir()                          # False
path.isfile()                         # True

# File system changes
(path.parent / 'foo').mkdir()         # Creates directory including parents
path.remove()                         # Deletes a file or empty directory
path.parent.rmtree()                  # Deletes directory and its content
path.copy(path.parent / 'copy.txt')   # Makes a copy
path.move(path.parent / 'moved.txt')  # Moves the file
```
