import pathlib
import tensorflow as tf


class CloudPath(pathlib.PosixPath):

  def open(path, mode='r', *args, **kwargs):
    filename = str(path)
    # Appending requires a specific encoding on CNS.
    if 'a' in mode and filename.startswith('/cns/'):
      filename += '%r=3.2'
    # Not supported by GFile. Forward so it works at least for local files.
    if mode.startswith('x'):
      return pathlib.PosixPath.open(path, mode)
    return tf.io.gfile.GFile(path, mode)

  def mkdir(path, mode=0o777, parents=False, exist_ok=False):
    if mode != 0o777:
      raise NotImplementedError(mode)
    if not parents and not path.parent.exists():
      raise FileNotFoundError(path)
    if not exist_ok and path.exists():
      raise FileExistsError(path)
    tf.io.gfile.makedirs(path)

  def rmdir(path):
    # Pathlib requires the directory to be empty but we don't.
    tf.io.gfile.rmtree(path)

  def iterdir(path):
    for filename in tf.io.gfile.listdir(path):
      yield pathlib.Path(filename)

  def glob(path, pattern):
    for filename in tf.io.gfile.glob(path / pattern):
      yield pathlib.Path(filename)

  def exists(path):
    return tf.io.gfile.exists(path)

  def is_dir(path):
    return tf.io.gfile.isdir(path)

  def is_file(path):
    return path.exists() and not path.is_dir()


pathlib.Path = CloudPath
