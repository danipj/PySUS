u"""
Created on 16/08/16
by fccoelho
license: GPL V3 or Later
"""
import os
from utilities._readdbc import ffi, lib
from dbfread import DBF
from tempfile import NamedTemporaryFile
import pandas as pd


def read_dbc(filename, encoding='utf-8'):
    """
    Opens a DATASUS .dbc file and return its contents as a pandas
    Dataframe.
    :param filename: .dbc filename
    :param encoding: encoding of the data
    :return: Pandas Dataframe.
    """
    with NamedTemporaryFile() as tf:
        dbc2dbf(filename, tf.name.encode())
        dbf = DBF(tf.name, encoding=encoding)
        df = pd.DataFrame(list(dbf))
    return df


def dbc2dbf(infile, outfile):
    """
    Converts a DATASUS dbc file to a DBF database.
    :param infile: .dbc file name
    :param outfile: name of the .dbf file to be created.
    """
    p = ffi.new('char[]', os.path.abspath(infile))
    q = ffi.new('char[]', os.path.abspath(outfile))

    lib.dbc2dbf([p], [q])

    print(os.path.exists(outfile))

if __name__ == "__main__":
    dbc2dbf(b'/tmp/DNRJ2014.dbc', b'/tmp/output.dbf')

