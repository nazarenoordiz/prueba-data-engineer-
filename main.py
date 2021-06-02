import pandas as pd
from os import path
import sqlite3
import datetime as DT
import io
import numpy as np
from pandas.core.tools.datetimes import to_datetime



df = pd.read_csv('clientes.csv', error_bad_lines=False, sep=";")


# df.to_csv("client3es.csv")

now = pd.Timestamp('now')

df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])
df['age'] = (now - df['fecha_nacimiento']).astype('<m8[Y]')

labels = [1, 2, 3, 4, 5, 6]

df['age_group'] = pd.cut(df['age'], bins=[0, 20, 30, 40, 50, 60, 100], labels=labels)


df['fecha_vencimiento'] = pd.to_datetime(df['fecha_vencimiento'])
df['delinquency'] = (now - df['fecha_vencimiento']).astype('<m8[D]')




with open("output/clientes.xlsx", "w") as clientes_file:

  Clientes_Columnas = ['fiscal_id', 'first_name', 'last_name', 'gender', 'fecha_nacimiento', 'age','age_group', 'fecha_vencimiento','delinquency', 'deuda', 'direccion']

  Clientes_csv = df[Clientes_Columnas]

  Clientes_Columnas_Ingles = ['fiscal_id', 'first_name', 'last_name', 'gender', 'birth_date', 'age','age_group', 'due_date','delinquency', 'due_balance', 'address']

  Clientes_csv = Clientes_csv.to_csv("output/clientes.xlsx", index=False, header=Clientes_Columnas_Ingles)


with open("output/emails.xlsx", "w") as mail_file:



  Emails_Columnas =  ['fiscal_id', 'correo', 'estatus_contacto', 'prioridad']

  Email_csv = df[Emails_Columnas]

  Email_Columnas_Ingles = ['fiscal_id', 'email', 'status', 'priority']

  Email_csv = Email_csv.to_csv("output/emails.xlsx", index=False, header=Email_Columnas_Ingles)

with open("output/phones.xlsx", "w") as phone_file:



  Phones_Columnas =  ['fiscal_id', 'telefono', 'estatus_contacto', 'prioridad']

  Phones_csv = df[Emails_Columnas]

  Phones_Columnas_Ingles = ['fiscal_id', 'phone', 'status', 'priority']

  Phones_csv = Phones_csv.to_csv("output/phones.xlsx", index=False, header=Phones_Columnas_Ingles)




con = sqlite3.connect('database.db3')
phones_wb = pd.read_csv("output/phones.xlsx")
emails_wb = pd.read_csv("output/emails.xlsx")
clientes_wb = pd.read_csv("output/clientes.xlsx")


clientes_wb.to_sql('customers', con, index=False)

emails_wb.to_sql('emails', con, index=False)

phones_wb.to_sql('phones', con, index=False)

con.commit()
con.close()


