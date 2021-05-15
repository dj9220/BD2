from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save, pre_save
from . import models as model
import csv, io
import pandas as pd

file =pd.read_csv('checks/shop/check1.csv', delimiter=',')
products = []
for i in range(len(file)):
 products.append(model.Check(
     product=file[i][0]

        ))

