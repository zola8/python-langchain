import sys


def list_internal_structure():
  # Garbage collection info (before object)
  _gc_next = ...  # 8 bytes
  _gc_prev = ...  # 8 bytes

  # PyObject info
  ob_refcnt = ...  # 8 bytes
  ob_type = ...  # 8 bytes

  # PyVarObject info
  ob_size = ...  # 8 bytes

  # PyListObject info
  ob_item = ...  # 8 bytes
  allocated = ...  # 8 bytes


def main():
  a = [0, 0, 0]
  print(sys.getsizeof(a))
  list_internal_structure()


if __name__ == '__main__':
  main()
