import tensorflow as tf
import os
import pandas as pd 

_URLmin9 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_-9.zip'
_URLmin8 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_-8.zip'
_URLmin7 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_-7.zip'
_URLmin6 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_-6.zip'
_URLmin5 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_-5.zip'
_URLmin4 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_-4.zip'
_URLmin3 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_-3.zip'
_URLmin2 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_-2.zip'
_URLmin1 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_-1.zip'
_URL0 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_0.zip'
_URL1 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_1.zip'
_URL2 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_2.zip'
_URL3 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_3.zip'
_URL4 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_4.zip'
_URL5 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_5.zip'
_URL6 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_6.zip'
_URL7 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_7.zip'
_URL8 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_8.zip'
_URL9 = 'https://github.com/EMCBuiten/hope_zip_files/raw/master/x_9.zip'

_URLmin9_name = 'x_-9.zip'
_URLmin8_name = 'x_-8.zip'
_URLmin7_name = 'x_-7.zip'
_URLmin6_name = 'x_-6.zip'
_URLmin5_name = 'x_-5.zip'
_URLmin4_name = 'x_-4.zip'
_URLmin3_name = 'x_-3.zip'
_URLmin2_name = 'x_-2.zip'
_URLmin1_name = 'x_-1.zip'
_URL0_name = 'x_0.zip'
_URL1_name = 'x_1.zip'
_URL2_name = 'x_2.zip'
_URL3_name = 'x_3.zip'
_URL4_name = 'x_4.zip'
_URL5_name = 'x_5.zip'
_URL6_name = 'x_6.zip'
_URL7_name = 'x_7.zip'
_URL8_name = 'x_8.zip'
_URL9_name = 'x_9.zip'

	
df_min9 = pd.DataFrame()
df_min8 = pd.DataFrame()
df_min7 = pd.DataFrame()
df_min6 = pd.DataFrame()
df_min5 = pd.DataFrame()
df_min4 = pd.DataFrame()
df_min3 = pd.DataFrame()
df_min2 = pd.DataFrame()
df_min1 = pd.DataFrame()
df_0 = pd.DataFrame()
df_1 = pd.DataFrame()
df_2 = pd.DataFrame()
df_3 = pd.DataFrame()
df_4 = pd.DataFrame()
df_5 = pd.DataFrame()
df_6 = pd.DataFrame()
df_7 = pd.DataFrame()
df_8 = pd.DataFrame()
df_9 = pd.DataFrame()
dataframe_hole = pd.DataFrame()


def zip_to_csv (fn):
  i = fn.index('.')
  fn = fn[:i]
  fn = fn + ".csv"
  #fn.replace(".zip", ".csv")
  # print(fn)
  return fn

def slash(fn):
  fn = fn.replace('\\', '/')
  return fn
 
def convert_to_float(fn):
  fn = str(fn)
  fn = fn.replace(',', '.')
  fn = float(fn)
  return fn
  
def append_ext(fn):
  inx = fn.index('/')
  if fn[:inx] == "project_fotos_raw":
    fn =  fn[inx+1:] 
  return fn
  
def set_dataframes(base_dir):
	global df_min9
	global df_min8
	global df_min7
	global df_min6
	global df_min5
	global df_min4
	global df_min3
	global df_min2
	global df_min1
	global df_0
	global df_1
	global df_2
	global df_3
	global df_4
	global df_5
	global df_6
	global df_7
	global df_8
	global df_9
	csv_file = base_dir + "/" + zip_to_csv(_URLmin9_name)
	df_min9 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URLmin8_name)
	df_min8 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URLmin7_name)
	df_min7 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URLmin6_name)
	df_min6 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URLmin5_name)
	df_min5 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URLmin4_name)
	df_min4 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URLmin3_name)
	df_min3 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URLmin2_name)
	df_min2 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URLmin1_name)
	df_min1 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URL0_name)
	df_0 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URL1_name)
	df_1 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URL2_name)
	df_2 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URL3_name)
	df_3 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URL4_name)
	df_4 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URL5_name)
	df_5 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URL6_name)
	df_6 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URL7_name)
	df_7 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URL8_name)
	df_8 = pd.read_csv(csv_file, sep= ';')
	
	csv_file = base_dir + "/" + zip_to_csv(_URL9_name)
	df_9 = pd.read_csv(csv_file, sep= ';')

def load_zips():
	zip_dir_min9 = tf.keras.utils.get_file(_URLmin9_name, origin=_URLmin9, extract=True)
	zip_dir_min8 = tf.keras.utils.get_file(_URLmin8_name, origin=_URLmin8, extract=True)
	zip_dir_min7 = tf.keras.utils.get_file(_URLmin7_name, origin=_URLmin7, extract=True)
	zip_dir_min6 = tf.keras.utils.get_file(_URLmin6_name, origin=_URLmin6, extract=True)
	zip_dir_min5 = tf.keras.utils.get_file(_URLmin5_name, origin=_URLmin5, extract=True)
	zip_dir_min4 = tf.keras.utils.get_file(_URLmin4_name, origin=_URLmin4, extract=True)
	zip_dir_min3 = tf.keras.utils.get_file(_URLmin3_name, origin=_URLmin3, extract=True)
	zip_dir_min2 = tf.keras.utils.get_file(_URLmin2_name, origin=_URLmin2, extract=True)
	zip_dir_min1 = tf.keras.utils.get_file(_URLmin1_name, origin=_URLmin1, extract=True)
	zip_dir_0 = tf.keras.utils.get_file(_URL0_name, origin=_URL0, extract=True)
	zip_dir_1 = tf.keras.utils.get_file(_URL1_name, origin=_URL1, extract=True)
	zip_dir_2 = tf.keras.utils.get_file(_URL2_name, origin=_URL2, extract=True)
	zip_dir_3 = tf.keras.utils.get_file(_URL3_name, origin=_URL3, extract=True)
	zip_dir_4 = tf.keras.utils.get_file(_URL4_name, origin=_URL4, extract=True)
	zip_dir_5 = tf.keras.utils.get_file(_URL5_name, origin=_URL5, extract=True)
	zip_dir_6 = tf.keras.utils.get_file(_URL6_name, origin=_URL6, extract=True)
	zip_dir_7 = tf.keras.utils.get_file(_URL7_name, origin=_URL7, extract=True)
	zip_dir_8 = tf.keras.utils.get_file(_URL8_name, origin=_URL8, extract=True)
	zip_dir_9 = tf.keras.utils.get_file(_URL9_name, origin=_URL9, extract=True)
	base_dir = os.path.dirname(zip_dir_9)
	set_dataframes(base_dir)
	return base_dir


def get_dataframe():
	global dataframe_hole
	dataframe_hole = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9], ignore_index=True)
	dataframe_hole["path"]= dataframe_hole["path"].apply(slash)
	dataframe_hole["path"]= dataframe_hole["path"].apply(append_ext)
	dataframe_hole["x"]= dataframe_hole["x"].apply(convert_to_float)
	dataframe_hole["y"]= dataframe_hole["y"].apply(convert_to_float)
	return dataframe_hole

def get_dataframe_X():
	df = get_dataframe()
	return df.drop(columns=["y","rotation"])

def get_dataframe_Y():
	df = get_dataframe()
	return df.drop(columns=["x", "rotation"])

def get_dataframe_rotation():
	df = get_dataframe()
	return df.drop(columns=["x","y"])
