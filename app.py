import plotly.express as px
from PIL import Image
import streamlit as st
import pickle
import os
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# outer join for nonactive customers
all_customers_df = pd.DataFrame(
    {
        "Customer": ['King Abdulaziz Medical City- NGHA R',
                     'Prince Sultan Military Medical City',
                     'NGHA - Jeddah',
                     'Security Forces Hospitals',
                     'King Saud University Hospital',
                     'MODA/KFAFH - Jeddah',
                     'Alhada Armed Forces Hospital',
                     'KFSHRC-JED : King Faisal Speciality',
                     'KFSHRC-RUH:King Faisal Speciality',
                     'Jazan Health Affairs',
                     'Prince Sultan Cardiac Center',
                     'Jeddah Health Affairs',
                     'King Fahad Military Medical Complex',
                     'King Fahad Medical City',
                     'King Salman Armed Forces Hospital',
                     'King Fahad Hospital - Dammam',
                     'King Abdulaziz Hospital - NGHA Ahsa',
                     'NGHA - Medina',
                     'King Fahad University Hospital',
                     'KING ABDULLAH MEDICAL CITY – MAKKAH',
                     'MOE - King Abdulaziz University Medical Services Center',
                     'King Saud Medical City',
                     'Asir Health Affairs',
                     'Armed Forces Hospitals SR',
                     'Qassim Cluster',
                     'Al-Ahsa Health Cluster',
                     'Madina Health Affairs',
                     'SFH - Makkah',
                     'MINISTRY OF HEALTH',
                     'NGHA - Dammam',
                     'E1 Cluster',
                     'Royal Commission (Yanbo)',
                     'Royal Commission for Jubail and Yan',
                     'Najran Health Affairs',
                     'Kharj Armed Forces Hospital',
                     'King Khalid Eyes Spi Hospital',
                     'Mecca Health Affairs',
                     'Dhahran Armed Forces Hospital',
                     'King Khalid University',
                     'Northern Area Armed Forces Hospital',
                     'PNU-King Abdullah University Hospital',
                     'Tabuk Health Affairs',
                     'Taif Health Affairs',
                     'MOI - Security Forces Hospital',
                     'GENERAL INTELLIGENCE PRESIDENCY',
                     'Jubail Armed Forces Hospital',
                     'Wadi Aldawasir Armed Forces Hosp.',
                     'Pr. Mohammed Bin Abdulaziz Hospital',
                     'Hail Health Affairs',
                     'Najran Armed Forces Hospital',
                     'Medina Armed Forces Hospital',
                     'Ministry of Interior',
                     'Hafar Al Batin Health Affairs',
                     'Bisha Health Affairs',
                     'Jazan Armed Forces Hospital',
                     'King Faisal Hospital in Taif',
                     'Al Bahah Health Affairs',
                     'PSS - Presidency of State Security',
                     'Sharurah Armed Forces Hospital',
                     'Riyadh Health Affairs',
                     'MOH - Makkah Healthcare Cluster',
                     'King Fahd Hospital in Al-Baha',
                     'Border Guard',
                     'SAUDI RED CRESCENT',
                     'Qassim Armed Forces Hospital',
                     'Charitable Association for Rheumati',
                     'King Salman Specialist Hospital',
                     'Special Security Forces',
                     'Association Medication Charity',
                     'Northern Health Affairs',
                     'Prince Saud Bin Jalawy Hospital - Ahasa',
                     'University of Hail',
                     'MOE - Prince Sattam University',
                     'King Salman Hospital',
                     'Al Jouf Health Affairs',
                     'SWCC - Jeddah',
                     'SWCC - Jubail',
                     'King Fahad Hospital - Hufof',
                     'MOE - Im. Mohammed Ibn Saud Univer.',
                     'Al Qunfudhah Health Affairs',
                     'MOH - Mental Health Hospital',
                     'Alyamamah Hospital',
                     'Tabuk University',
                     'Ahsa Health Affairs',
                     'Imam Abdulrahman Alfaisal Hospital',
                     'MOH - Khamis Mushait',
                     'Jazan University',
                     'Special Emergency Forces',
                     'King Khalid Hospital Hail',
                     'King Fahad Security College',
                     'Maternity and Children Hospital  Al-Hassa',
                     'Heart Center',
                     'Al Iman General Hospital',
                     'MOE - Islamic University',
                     'Ministry of Labor and Social Dev.',
                     'Al Qurayyat Health Affairs',
                     'HRSD - Health Association',
                     'MOH - Qasim Health Directorate',
                     'King Abdulaziz City for Science',
                     'SWCC - Shuaiba',
                     'ROYAL CLINICS',
                     'Maternity and Children Hospital in',
                     'MINISTRY OF DEFENCE',
                     'MOE - Najran University',
                     'SWCC - Khobar',
                     'MOH - Ahad Rafidah Hospital',
                     'King Faisal Hospital in Al-Ahsa',
                     'MOE - Um AlQura University',
                     'Bisha University',
                     'General Administration of Prison Health',
                     'MOE - AlJouf University',
                     'SWCC - Shuqaiq',
                     'Pr. Abdulrahman Institute',
                     'Mikhwah Hospital',
                     'General Directorate of Investigation',
                     'General Directorate of Civil Defence',
                     'Albaha University',
                     'General Security Aviation Command',
                     'MOE - King Faisal University',
                     'Majmaa University',
                     'Qassim University',
                     'MOE - Taiba University',
                     'Saudi Royal Guard',
                     'Equine Hospital Frusiya Club',
                     'Dawadmi Hospital',
                     'Mueafat Health Association',
                     'Riyadh Specialized Dental Center',
                     'Facilities Security Forces',
                     'Northern Border University',
                     'Pr. Meshari Bin Saud Hospital',
                     'MODA - Prince Sultan Military Colle',
                     'Technical and Vocational Training C Training Corporation',
                     'Eradah Complex for Mental Health in',
                     'General Administration of Technical and Vocational Training in Qassim',
                     'Asir-General Directorate of Technic',
                     'Technical and Vocational Training Corporation-Makkah',
                     'SWCC - Yanbu',
                     'MCH Al Kharj',
                     'Al Amal Mental Health Complex',
                     'Rabig University',
                     'MOH - Abha Mental Health Hospital',
                     'Institute of Public Administration',
                     'Howtat Bani Tamim General Hospita',
                     'King Khaled Hospital',
                     'General Administration of Technical and Vocational Trainin hail',
                     'Ad Diriyah Hospital',
                     'University of Jeddah',
                     'MNGHA King Saud University For Health Sciences',
                     'MOH - Eastern Health Directorate',
                     'KING SALMAN KIDNEY CENTER',
                     'Saudi Electronic University',
                     'Hail General Hospital',
                     'King Abdulaziz Port  - Dammam',
                     'Hotat Sdair Hospital',
                     'MOH - Alhayit Hospital',
                     'MOH - AlMahani Hospital',
                     'Technical and Vocational Training jouf',
                     'Jazan-General Directorate of Techni',
                     'General Administration of Technical and Vocational Training Tabuk',
                     'General Administration for Vocation baha',
                     'Technical and Vocational Training Corporation in Najran',
                     'Technical and Vocational Training Corporation in Arar',
                     'General Administration of Technical and Vocational Training Dammam',
                     'MOH - King Khalid Hospital',
                     'MODA - King Faisal Air College',
                     'Technical and Vocational',
                     'MOI - Public Security',
                     'MOE - department of education',
                     'Public Health Authority',
                     "Directorate General of Prisons Health Care Administration",
                     "HRSD - Tarabot Association for Pati Care",
                     "Arfa Multiple Sclerosis Society",
                     "Salaam Medical Association",
                     "College of Technology - Dowadmi",
                     "College of Technology - Kharj",
                     "College of Technology - Majma'a",
                     "College of Technology - Quiae'eia",
                     'College of Technology - Riyadh',
                     'College of Technology - Wadi Addwas',
                     'College of Technology - Zulfi',
                     'College of Technology for Girls- Do',
                     'College of Technology for Girls- Ri',
                     'College of Telecom',
                     'First Secondary Industrial Institut',
                     'Qassim- Directorate of Technical',
                     'Royal Industrial Secondary Institut',
                     'Secondary Industrial Institute',
                     'Erada Hospital and Mental Health Kharj',
                     'Al Ghaat Hospital',
                     'AlQuwayiyah Hospital',
                     'Central Security Hospitals',
                     'Dental Center in Hail',
                     'KFSHRC-Madina : King Faisal Speciality',
                     'King Khalid Hospital (Najran)',
                     'MODA - Air Defense Force',
                     'MOE - Health Science Research Cente',
                     'MOE - King Abdulaziz University',
                     'MOH - General Department of Stock C',
                     'MOH - King Abdulaziz Specialist',
                     'MOH - Medical Supply Operations Center',
                     'MOH - Second Health Cluster in Riya',
                     'MOH - Therapeutic Services',
                     'MOH - Wadi Dawaser Hospital',
                     'PNU-The Simulation and Skills Development Center',
                     'Rawaidah Al-ard hospital',
                     'Royal Saudi Strategic Missile Force',
                     'Saudi Airlines Medical Services Co.',
                     'Saudi Data &Al Authority',
                     'Shaqra University',
                     'Taif University',
                     'University of Hafr Al-Batin',
                     'General Administration Of Education'
                     ],

    }
)

st.sidebar.header("Health Entities Classification")

page = st.sidebar.selectbox(
    "Select", ["Introduction", "Health Entities Classification", "أعلى الجهات الصحية تصنيفاً"])

st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")


img = Image.open("nupco logo.png")
st.sidebar.image(img)

l = ['Prince Sultan Military Medical City', 'Security Forces Hospitals',
     'NGHA - Jeddah', 'King Abdulaziz Medical City- NGHA R',
     'Prince Sultan Cardiac Center',
     'King Salman Armed Forces Hospital',
     'KFSHRC-RUH:King Faisal Speciality', 'Jazan Health Affairs',
     'Alhada Armed Forces Hospital',
     'KFSHRC-JED : King Faisal Speciality',
     'King Fahad Hospital - Dammam', 'MODA/KFAFH - Jeddah',
     'King Fahad Medical City', 'King Fahad Military Medical Complex',
     'Jeddah Health Affairs', 'KING ABDULLAH MEDICAL CITY – MAKKAH',
     'King Saud University Hospital', 'NGHA - Medina',
     'King Saud Medical City', 'King Fahad University Hospital']


if page == "Introduction":  # write here introduction

    st.header("Health Entities Classification")

    st.subheader("introduction")


if page == "أعلى الجهات الصحية تصنيفاً":
    st.subheader("مستشفى قوى الأمن بالرياض")
    st.subheader("TOP CUSTOMERS")
    for x in l:
        st.text("* "+x)


if page == "Health Entities Classification":

    uploaded_file1 = st.file_uploader("Choose Order list csv file")
    if uploaded_file1 is not None:
        df = pd.read_csv(uploaded_file1, sep=",")

    uploaded_file2 = st.file_uploader("Choose Order tracker list csv file")
    if uploaded_file2 is not None:
        track_df = pd.read_csv(uploaded_file2, sep=',')

    st.text("")
    st.text("")
    if st.button('Classify Health Entities'):

        if (uploaded_file2 is not None) and (uploaded_file1 is not None):

            customers = ['NUPCO Marketplace', 'Madinah Cardiac Center',
                         'Medical Store', 'NUPCO Marketplace', 'Minstry of Health']

            sh_program = ['Shared Program']

            # selecting rows based on conditions

            df = df[df['Order Type'].isin(sh_program) == False]
            df = df[df.Customer.isin(customers) == False]

            df.loc[(df.Customer == 'KING ABDULLAH MEDICAL CITY Ã¢â‚¬â€œ MAKKAH'),
                   'Customer'] = 'KING ABDULLAH MEDICAL CITY – MAKKAH'
            df.loc[(df.Customer == 'KING ABDULLAH MEDICAL CITY â€“ MAKKAH'),
                   'Customer'] = 'KING ABDULLAH MEDICAL CITY – MAKKAH'

            # let's find active clients
            co_status = ['Order Received', 'Fulfilment In Progress', 'Order Delivered',
                         'Dispatched', 'PO Issued', 'Pay On Account',
                         'PO Initiated', 'NUPCO Operator Pending', 'NUPCO_OPERATOR_RETURNED',
                         'Pay On Account Delivered', 'Pay On Account Shipped']

            # selecting rows based on condition
            co_df = df.loc[df['Status'].isin(co_status)]

            customers_co = co_df.groupby('Customer', as_index=False)
            customers_co2 = customers_co['Total Price'].sum()
            customers_co2 = pd.DataFrame(customers_co2)
            customers_co2 = customers_co2.rename(
                {'Total Price': 'Total_price_of_confirmed_orders'}, axis=1)

            customers_co2.sort_values("Total_price_of_confirmed_orders", axis=0, ascending=False,
                                      inplace=True, na_position='last')

            co_df = pd.merge(customers_co2, all_customers_df,
                             on='Customer', how="outer")
            co_df.Total_price_of_confirmed_orders.fillna(value=0, inplace=True)

            co_df.loc[(co_df["Total_price_of_confirmed_orders"]
                       >= 300000000), "Class"] = "A"
            co_df.loc[(co_df["Total_price_of_confirmed_orders"] < 300000000) & (
                co_df["Total_price_of_confirmed_orders"] >= 100000000), "Class"] = 'B'
            co_df.loc[(co_df["Total_price_of_confirmed_orders"] < 100000000) & (
                co_df["Total_price_of_confirmed_orders"] >= 50000000), "Class"] = 'C'
            co_df.loc[(co_df["Total_price_of_confirmed_orders"] < 50000000) & (
                co_df["Total_price_of_confirmed_orders"] >= 10000000), "Class"] = 'D'
            co_df.loc[(co_df["Total_price_of_confirmed_orders"] < 10000000) & (
                co_df["Total_price_of_confirmed_orders"] >= 1000000), "Class"] = 'E'
            co_df.loc[(co_df["Total_price_of_confirmed_orders"]
                       < 1000000), "Class"] = 'F'
            co_df.loc[(co_df["Total_price_of_confirmed_orders"]
                       == 0), "Class"] = 'G'

            co_df.loc[(co_df["Class"] == 'A'), "CO_KPI"] = 70
            co_df.loc[(co_df["Class"] == 'B'), "CO_KPI"] = 60
            co_df.loc[(co_df["Class"] == 'C'), "CO_KPI"] = 45
            co_df.loc[(co_df["Class"] == 'D'), "CO_KPI"] = 30
            co_df.loc[(co_df["Class"] == 'E'), "CO_KPI"] = 15
            co_df.loc[(co_df["Class"] == 'F'), "CO_KPI"] = 10
            co_df.loc[(co_df["Class"] == 'G'), "CO_KPI"] = 0

            co_kpi = co_df.drop(
                ['Total_price_of_confirmed_orders', 'Class'], axis=1)

            df_kpi2 = df.groupby("Customer")["Order Number"].count()

            df_kpi2.sort_values(ascending=False, inplace=True)
            df_kpi2 = pd.DataFrame(df_kpi2)
            df_kpi2 = df_kpi2.rename(columns={'Order Number': 'Total_Orders'})

            df_kpi2 = pd.merge(df_kpi2, all_customers_df,
                               on='Customer', how="outer")
            df_kpi2.Total_Orders.fillna(value=0, inplace=True)

            # let's find rejected orders
            ro_status = ['Approver Rejected', 'Cancelled', 'Release Order Cancelled',
                         'CANCELLED_BY_HOSPITAL_AFTER_PO_ISSUED', 'Rejected', 'QUOTATION_EXPIRED', 'Cancelling', ]

            # selecting rows based on condition
            ro_df = df.loc[df['Status'].isin(ro_status)]

            df_kpi2_2 = ro_df.groupby("Customer")["Order Number"].count()
            df_kpi2_2.sort_values(ascending=False, inplace=True)
            df_kpi2_2 = pd.DataFrame(df_kpi2_2)
            df_kpi2_2 = df_kpi2_2.rename(
                columns={'Order Number': 'Cancel_Orders'})

            df_kpi2 = pd.merge(df_kpi2, df_kpi2_2, on='Customer', how="outer")
            df_kpi2.Cancel_Orders.fillna(value=-1, inplace=True)

            df_kpi2['Percentage'] = (
                df_kpi2['Cancel_Orders'] / df_kpi2['Total_Orders']*100).round(2)

            df_kpi2.loc[(df_kpi2["Percentage"] >= 0) & (
                df_kpi2["Percentage"] <= 5), "Cancel_KPI"] = 10
            df_kpi2.loc[(df_kpi2["Percentage"] > 5) & (
                df_kpi2["Percentage"] <= 10), "Cancel_KPI"] = 9
            df_kpi2.loc[(df_kpi2["Percentage"] > 10) & (
                df_kpi2["Percentage"] <= 15), "Cancel_KPI"] = 8
            df_kpi2.loc[(df_kpi2["Percentage"] > 15) & (
                df_kpi2["Percentage"] <= 20), "Cancel_KPI"] = 7
            df_kpi2.loc[(df_kpi2["Percentage"] > 20) & (
                df_kpi2["Percentage"] <= 25), "Cancel_KPI"] = 6
            df_kpi2.loc[(df_kpi2["Percentage"] > 25) & (
                df_kpi2["Percentage"] <= 30), "Cancel_KPI"] = 5
            df_kpi2.loc[(df_kpi2["Percentage"] > 30) & (
                df_kpi2["Percentage"] <= 35), "Cancel_KPI"] = 4
            df_kpi2.loc[(df_kpi2["Percentage"] > 35) & (
                df_kpi2["Percentage"] <= 40), "Cancel_KPI"] = 3
            df_kpi2.loc[(df_kpi2["Percentage"] > 40) & (
                df_kpi2["Percentage"] <= 45), "Cancel_KPI"] = 2
            df_kpi2.loc[(df_kpi2["Percentage"] > 45) & (
                df_kpi2["Percentage"] < 51), "Cancel_KPI"] = 1
            df_kpi2.loc[(df_kpi2["Percentage"] >= 51), "Cancel_KPI"] = 0

            df_kpi2.Cancel_KPI.fillna(value=0, inplace=True)

            cancel_kpi = df_kpi2.drop(
                ['Total_Orders', 'Cancel_Orders', 'Percentage'], axis=1)

            track_df = track_df.rename(columns={'Hospital': 'Customer'})

            customers = ['NUPCO Marketplace', 'Madinah Cardiac Center',
                         'Medical Store', 'NUPCO Marketplace', 'Minstry of Health']

            # selecting rows based on conditions

            track_df = track_df[track_df.Customer.isin(customers) == False]

            track_df.loc[(track_df.Customer == 'KING ABDULLAH MEDICAL CITY Ã¢â‚¬â€œ MAKKAH'),
                         'Customer'] = 'KING ABDULLAH MEDICAL CITY – MAKKAH'
            track_df.loc[(track_df.Customer == 'KING ABDULLAH MEDICAL CITY â€“ MAKKAH'),
                         'Customer'] = 'KING ABDULLAH MEDICAL CITY – MAKKAH'

            # let's find average time of PA
            PA_status = ['Pending Approval']
            PA_to_status = ['Awaiting Supplier Review']
            # selecting rows based on condition
            PA_df = track_df.loc[track_df['From Status'].isin(
                PA_status) & track_df['To Status'].isin(PA_to_status)]

            PA_df.groupby("To Status")["To Status"].count()

            PA_df["Status Created"] = PA_df["Status Created"].apply(
                lambda x: x.replace("/", "-"))
            PA_df["Status Closed"] = PA_df["Status Closed"].apply(
                lambda x: x.replace("/", "-"))
            PA_df["Order Created"] = PA_df["Order Created"].apply(
                lambda x: x.replace("/", "-"))

            # calculate date different.
            PA_df["Status Created"] = pd.to_datetime(
                PA_df["Status Created"], format="%d-%m-%Y")
            PA_df["Status Closed"] = pd.to_datetime(
                PA_df["Status Closed"], format="%d-%m-%Y")
            PA_df["DAYSDIFF"] = pd.to_datetime(
                PA_df["Status Closed"]) - pd.to_datetime(PA_df["Status Created"])
            PA_df["DAYSDIFF"] = PA_df["DAYSDIFF"].astype('timedelta64[D]')

            PA_df_sum = PA_df.groupby("Customer", as_index=False)[
                "DAYSDIFF"].sum()
            PA_df_sum = pd.DataFrame(PA_df_sum)
            PA_df_sum = PA_df_sum.rename(columns={'DAYSDIFF': 'sum'})

            PA_df_count = PA_df.groupby("Customer", as_index=False)[
                "DAYSDIFF"].count()
            PA_df_count = pd.DataFrame(PA_df_count)
            PA_df_count = PA_df_count.rename(columns={'DAYSDIFF': 'Count'})

            PA_customer = pd.merge(
                PA_df_sum, PA_df_count, on='Customer', how="outer")
            #co_df.Total_price_of_confirmed_orders.fillna(value=0, inplace=True)

            PA_customer = pd.merge(
                PA_customer, customers_co2, on='Customer', how="outer")

            del PA_customer["Total_price_of_confirmed_orders"]

            PA_customer['average_PA'] = (
                PA_customer['sum'] / PA_customer['Count'])
            PA_customer["average_PA"].fillna(value=0, inplace=True)

            PA_customer = pd.merge(
                PA_customer, all_customers_df, on='Customer', how="outer")

            PA_customer.sort_values(
                "average_PA", axis=0, ascending=False, inplace=True, na_position='last')

            PA_customer.loc[(PA_customer["average_PA"] >= 0) & (
                PA_customer["average_PA"] <= 5), "KPI_Degree_PA"] = 5
            PA_customer.loc[(PA_customer["average_PA"] > 5) & (
                PA_customer["average_PA"] <= 10), "KPI_Degree_PA"] = 4
            PA_customer.loc[(PA_customer["average_PA"] > 10) & (
                PA_customer["average_PA"] <= 15), "KPI_Degree_PA"] = 3
            PA_customer.loc[(PA_customer["average_PA"] > 15) & (
                PA_customer["average_PA"] <= 20), "KPI_Degree_PA"] = 2
            PA_customer.loc[(PA_customer["average_PA"] > 20) & (
                PA_customer["average_PA"] <= 25), "KPI_Degree_PA"] = 1
            PA_customer.loc[(PA_customer["average_PA"] > 25),
                            "KPI_Degree_PA"] = 0

            PA_customer.KPI_Degree_PA.fillna(value=0, inplace=True)
            PA_customer.sort_values(
                "KPI_Degree_PA", axis=0, ascending=False, inplace=True, na_position='last')

            PA_customer2 = pd.DataFrame()
            PA_customer2 = PA_customer

            PA_kpi = PA_customer.drop(['sum', 'Count', 'average_PA'], axis=1)

            # let's find active clients
            ARO_status = ['Awaiting Release Order']
            ARO_to_status = ['NUPCO Operator Pending']
            # selecting rows based on condition
            ARO_df = track_df.loc[track_df['From Status'].isin(
                ARO_status) & track_df['To Status'].isin(ARO_to_status)]

            #df["text"] = df["text"].astype(str)
            ARO_df["Status Created"] = ARO_df["Status Created"].apply(
                lambda x: x.replace("/", "-"))
            ARO_df["Status Closed"] = ARO_df["Status Closed"].apply(
                lambda x: x.replace("/", "-"))
            ARO_df["Order Created"] = ARO_df["Order Created"].apply(
                lambda x: x.replace("/", "-"))

            ARO_df.groupby("To Status")["To Status"].count()

            ARO_df["Status Created"] = pd.to_datetime(
                ARO_df["Status Created"], format="%d-%m-%Y")
            ARO_df["Status Closed"] = pd.to_datetime(
                ARO_df["Status Closed"], format="%d-%m-%Y")
            ARO_df["DAYSDIFF"] = ARO_df["Status Closed"] - \
                ARO_df["Status Created"]
            ARO_df["DAYSDIFF"] = ARO_df["DAYSDIFF"].astype('timedelta64[D]')

            ARO_customer_sum = ARO_df.groupby("Customer")["DAYSDIFF"].sum()
            RO_customer_sum = pd.DataFrame(ARO_customer_sum)

            # -----------------

            # ARO_customer_sum = ARO_customer_sum.rename(
            #     columns={'DAYSDIFF': 'sum'})
            ARO_customer_sum.columns = ["sum"]
            # -------------------------

            ARO_customer_count = ARO_df.groupby("Customer")["DAYSDIFF"].count()
            ARO_customer_count = pd.DataFrame(ARO_customer_count)
            # ARO_customer_count = ARO_customer_count.rename(
            #     columns={'DAYSDIFF': 'Count'})

            ARO_customer_count.columns = ["Count"]

            ARO_customer = pd.merge(
                ARO_customer_sum, ARO_customer_count, on='Customer', how="outer")
            #co_df.Total_price_of_confirmed_orders.fillna(value=0, inplace=True)

            ARO_customer = pd.merge(
                ARO_customer, all_customers_df, on='Customer', how="outer")

            ARO_customer.columns = ['Customer', 'sum', 'Count']
            # st.dataframe(ARO_customer)
            #pd.to_numeric(ARO_customer['sum'], downcast = 'integer')
            ARO_customer['average_ARO'] = (
                ARO_customer['sum'] / ARO_customer['Count'])

            ARO_customer.sort_values(
                "average_ARO", axis=0, ascending=False, inplace=True, na_position='last')

            ARO_customer.loc[(ARO_customer["average_ARO"] >= 0) & (
                ARO_customer["average_ARO"] <= 10), "KPI_Degree_ARO"] = 15
            ARO_customer.loc[(ARO_customer["average_ARO"] > 10) & (
                ARO_customer["average_ARO"] <= 20), "KPI_Degree_ARO"] = 12
            ARO_customer.loc[(ARO_customer["average_ARO"] > 20) & (
                ARO_customer["average_ARO"] <= 30), "KPI_Degree_ARO"] = 9
            ARO_customer.loc[(ARO_customer["average_ARO"] > 30) & (
                ARO_customer["average_ARO"] <= 40), "KPI_Degree_ARO"] = 6
            ARO_customer.loc[(ARO_customer["average_ARO"] > 40) & (
                ARO_customer["average_ARO"] <= 50), "KPI_Degree_ARO"] = 3
            ARO_customer.loc[(ARO_customer["average_ARO"]
                              > 50), "KPI_Degree_ARO"] = 0

            ARO_customer.groupby("KPI_Degree_ARO")["KPI_Degree_ARO"].count()
            ARO_customer.KPI_Degree_ARO.fillna(value=0, inplace=True)
            ARO_kpi = ARO_customer.drop(
                ['sum', 'Count', 'average_ARO'], axis=1)
            KPIs_dataset = pd.DataFrame()
            KPIs_dataset['Customer'] = co_df["Customer"]

            KPIs_dataset = pd.merge(
                KPIs_dataset, co_kpi, on='Customer', how="outer")

            KPIs_dataset = pd.merge(
                KPIs_dataset, cancel_kpi, on='Customer', how="outer")

            KPIs_dataset = pd.merge(
                KPIs_dataset, PA_kpi, on='Customer', how="outer")

            KPIs_dataset = pd.merge(
                KPIs_dataset, ARO_kpi, on='Customer', how="outer")

            KPIs_dataset["Degree_out_of_100"] = KPIs_dataset.apply(
                lambda row: row['CO_KPI': 'KPI_Degree_ARO'].sum(), axis=1)
            #KPIs_dataset.loc[KPIs_dataset['Customer'].str.contains('King Abdulaziz Medical City- NGHA R')]

            KPIs_dataset.sort_values(
                "Degree_out_of_100", axis=0, ascending=False, inplace=True, na_position='last')

            KPIs_dataset.loc[(KPIs_dataset["Degree_out_of_100"] <= 100) & (
                KPIs_dataset["Degree_out_of_100"] >= 80), "CLASS"] = 'A'
            KPIs_dataset.loc[(KPIs_dataset["Degree_out_of_100"] < 80) & (
                KPIs_dataset["Degree_out_of_100"] >= 60), "CLASS"] = 'B'
            KPIs_dataset.loc[(KPIs_dataset["Degree_out_of_100"] < 60) & (
                KPIs_dataset["Degree_out_of_100"] >= 40), "CLASS"] = 'C'
            KPIs_dataset.loc[(KPIs_dataset["Degree_out_of_100"] < 40) & (
                KPIs_dataset["Degree_out_of_100"] >= 20), "CLASS"] = 'D'
            KPIs_dataset.loc[(KPIs_dataset["Degree_out_of_100"]
                              < 20), "CLASS"] = 'F'
            # KPIs_dataset.head(66)

            st.text("")
            st.text("")
            st.dataframe(KPIs_dataset.head(10))

            csv = KPIs_dataset.to_csv().encode('utf-8')

            st.text("")
            st.text("")

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='KPIs_dataset.csv',
                mime='text/csv',
            )

        else:
            st.header("Upload 2 Files")
