import pandas as pd
import glob
import numpy as np
from config import regional_data_path
from config import national_data_path

class DataLoader(object):
    _instance = None
    _regional_data = None
    _national_data = None
    _empty_region_data = {
            1 : None,
            2 : None,
            3 : None,
            4 : None,
            5 : None,
            6 : None,
            7 : None,
            8 : None,
            9 : None,
            10 : None,
            11 : None,
            12 : None,
            13 : None,
            14 : None,
            15 : None,
            16 : None,
            17 : None,
            18 : None,
            19 : None,
            20 : None,
            21 : None,
            22 : None
    }
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataLoader, cls).__new__(cls)
            cls._regional_data = cls.__load_regional_data(cls, cls._empty_region_data)
            cls._national_data = cls.__load_national_data(cls)
        return cls._instance
    
    @classmethod
    def get_regional_data(self):
        return self._regional_data
    
    @classmethod
    def get_national_data(self):
        return self._national_data


    def __load_regional_data(self, region_data):
        df = pd.read_csv(regional_data_path).drop_duplicates()
        
        for key, value in region_data.items():
            df_t = df.loc[df['codice_regione'] == key]
            df_t['ratio_positivi_tamponi'] = round(100 * df_t['totale_positivi'] / df_t['tamponi'], 2)
            df_t = df_t.replace([np.inf, -np.inf], np.nan)
            df_t.fillna(0, inplace = True)
            region_data[key] = df_t

        # Hack needed due to the split of region in two provinces
        #data,stato,codice_regione,denominazione_regione,lat,long,
        region_data[4] = pd.concat([region_data[21],region_data[22]])
        
        df_t = region_data[4].groupby(['data', 'stato',])[
                    'ricoverati_con_sintomi',
                    'terapia_intensiva',
                    'totale_ospedalizzati',
                    'isolamento_domiciliare',
                    'totale_positivi',
                    'variazione_totale_positivi',
                    'nuovi_positivi',
                    'dimessi_guariti',
                    'deceduti',
                    'totale_casi',
                    'tamponi'].apply(lambda x : x.astype(int).sum()).reset_index()
        df_t['denominazione_regione'] = 'Trentino Alto Adige'
        df_t['lat'] = '46.06893511'
        df_t['long'] = '11.12123097'
        df_t['ratio_positivi_tamponi'] = round(100 * df_t['totale_positivi'] / df_t['tamponi'], 2)
        print (df_t)
        region_data[4] = df_t
        return region_data

    def __load_national_data(self):
        df = pd.read_csv(national_data_path).drop_duplicates()
        df['ratio_positivi_tamponi'] = round(100 * df['totale_positivi'] / df['tamponi'], 2)
        df = df.replace([np.inf, -np.inf], np.nan)
        df.fillna(0, inplace = True)
        return df