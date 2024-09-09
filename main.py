import tkinter as tk
import customtkinter as ck

import pandas as pd
import numpy as np
import pickle5 as pickle

import mediapipe as mp
import cv2

from PIL import Image, ImageTk

from landmark import lm


window = tk.Tk()
window.geometry("580x700")
