import time
import json
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk


import dictFactory
import Util as util
import os

current_path = os.path.dirname(__file__)

print(current_path)

with open(current_path+"/GeneratorConfig.json",'r',encoding='utf8') as fp:
    generator_Config = json.load(fp)

print(generator_Config.main)