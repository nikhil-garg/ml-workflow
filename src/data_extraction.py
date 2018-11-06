"""
Created on Wed Sep 12 2018

@author: Fabien Tarrade fabien.tarrade@axa.ch
"""

import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
import CCDA_Standard_Functions as sf

# extraction of eform from the SQL database
# These are example functions based on an actual project

def eforms_extr():
    """

    :return:
    """
    con_forms = sf.sql_connection('webformulare', '', '')
    df_sql_db = sf.sql_getdf("""
          select 
              a.reporting_id,
              a.form_uuid,
              a.ajila_process_id,
              a.tracking_id,
              a.currenttime,
              a.form_type,
              convert(varchar(max),convert(varbinary(max),a.data)) as form
        FROM
          dbo.forms_reporting a
        WHERE
           a.description = 'FORMDATA'
                      AND
           a.form_type = '0025'""",con_forms)
    return df_sql_db


def merging(df1, df2):
    """

    :param df1:
    :param df2:
    :return:
    """
    df_xml = pd.concat([df1, df2]).drop_duplicates().reset_index(drop=True)
    return df_xml


def pandas_display():
    """
    function to setup pandas parameters for interactive session
    """

    options = {
        'display': {
            'max_columns': 550,
            'width': 3000,
            'max_colwidth': -1,
            'expand_frame_repr': False,  # Don't wrap to multiple pages
            'max_rows': 200,
            'max_seq_items': 50,         # Max length of printed sequence
            'precision': 4,
            'show_dimensions': False
        },
        'mode': {
            'chained_assignment': None   # Controls SettingWithCopyWarning
        }
    }

    for category, option in options.items():
        for op, value in option.items():
            print('{}.{}'.format(category, op), value)
            pd.set_option('{}.{}'.format(category, op), value)


def xml2df(df_xml):
    """

    :param df_xml:
    :return:
    """
    dic_path = {'anliegen': './metadata/PATH',
                'mitteilung': './metadata/PATH'
                }

    dic_type = {'sc_dat_von': 'date',
                'ort_datum': 'date'}

    for var, path in dic_path.items():
        # print(var,': ', path)
        df_xml[var] = df_xml['form'].apply(lambda x: get_content_xml(x, path))

        if df_xml[var].dtype == 'object':
            # droping leading and traing space, no impact on the content but harmonize and avoid crashes
            df_xml[var] = df_xml[var].str.strip()

        if var in dic_type:
            # print("casting variable with the right type")
            if dic_type[var] == 'date':
                    # transforming string in datetime with the YYY-mm-dd patern
                df_xml[var] = pd.to_datetime(df_xml[var], format='%Y-%m-%d')
    return df_xml


def get_content_xml(xml, xpath):
    """

    :param xml:
    :param xpath:
    :return:
    """
    root = ET.fromstring(xml.encode('cp1252').decode('utf8'))
    elem = root.findall(xpath)

    val = ''
    if len(elem) == 1:
        val = elem[0].text
    elif len(elem) > 1:
        print("Warning: more than one value !!")

    return val


def load_data(file_data=None):
    """"
    Function to read the pandas data frame stored in a pickle file

    Parameters
    ----------
    :param file_data: path to file
    """
    if file_data is None:
        df = pd.read_pickle("./data/DEFAULT_DATA")
    else:
        df = pd.read_pickle(file_data)

    return df


def save_data(file_data, data, data_type='df'):
    """
    Function that saves data of different types.

    Parameters
    ----------
    :param data: data to be saved
    :param file_data: path
    :param type: 'df', 'np'
    """
    if data_type == 'df':
        data.to_pickle(file_data)
    if data_type == 'np':
        np.save(file_data, data)
