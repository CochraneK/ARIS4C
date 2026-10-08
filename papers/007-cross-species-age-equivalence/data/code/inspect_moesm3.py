# -*- coding: utf-8 -*-
"""Stage2: inspect MOESM3 xlsx structure (sheets, dims, head rows). Small stdout."""
import importlib, sys

try:
    import openpyxl
    print("openpyxl", openpyxl.__version__)
    wb = openpyxl.load_workbook("data/suppl/43587_2023_462_MOESM3_ESM.xlsx", read_only=True)
    for ws in wb.worksheets:
        print("SHEET", repr(ws.title), ws.max_row, "rows x", ws.max_column, "cols")
    wb.close()
except ImportError as e:
    print("NO openpyxl:", e)
    for m in ["pandas", "xlrd"]:
        try:
            importlib.import_module(m)
            print(m, "available")
        except ImportError:
            print(m, "missing")
    sys.exit(1)
