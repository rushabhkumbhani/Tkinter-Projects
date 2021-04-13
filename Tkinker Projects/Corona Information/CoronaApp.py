def scrap():
    def notifyme(title, message):
        notification.notify(
            title = title,
            message = message,
            timeout = 20
        )
    url = "https://www.worldometers.info/coronavirus/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    tablebody = soup.find("tbody")
    ttt = tablebody.find_all("tr")
    notifycountry = country_data.get()
    if notifycountry == "":
        notifycountry = "india"

    countries, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases = [], [], [], [], [], [], []
    serious, totalcases_permillion, totaldeaths_permilliom, totaltests, totaltests_permillion = [], [], [], [], []

    headers = ['countries', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_recovered', 'active_cases', 'serious', 'totalcases_permillion', 'totaldeaths_permilliom', 'totaltests', 'totaltests_permillion'] 

    for i in ttt:
        id = i.find_all("td")
        if id[0].text.strip().lower() == notifycountry:
            total_cases1 = id[1].text.strip().replace(',', '')
            total_deaths1 = id[3].text.strip()
            new_cases1 = id[2].text.strip()
            new_deaths1 = id[4].text.strip()

            notifyme("CoronaVirus details in {}".format(notifycountry), "Total Cases: {}\nTotal Deaths: {}\nNew Cases: {}\nNew Deaths: {}".format(total_cases1, total_deaths1, new_cases1, new_deaths1))


        countries.append(id[0].text.strip())
        total_cases.append(id[1].text.strip().replace(',', ''))
        new_cases.append(id[2].text.strip()) 
        total_deaths.append(id[3].text.strip())
        new_deaths.append(id[4].text.strip()) 
        total_recovered.append(id[5].text.strip())
        active_cases.append(id[6].text.strip())
        serious.append(id[7].text.strip())
        totalcases_permillion.append(id[8].text.strip())
        totaldeaths_permilliom.append(id[9].text.strip())
        totaltests.append(id[10].text.strip())
        totaltests_permillion.append(id[11].text.strip())

    df = pd.DataFrame(list(zip(countries, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases, serious, totalcases_permillion, totaldeaths_permilliom, totaltests, totaltests_permillion)), columns = headers)
    sor = df.sort_values('total_cases', ascending = False)
    for k in formatlist:
        if k == 'html':
            path2 = '{}/alldata.html'.format(path)
            sor.to_html(r'{}'.format(path2))
        if k == 'csv':
            path2 = '{}/alldata.csv'.format(path)
            sor.to_csv(r'{}'.format(path2))
        if k == 'json':
            path2 = '{}/alldata.json'.format(path)
            sor.to_json(r'{}'.format(path2))
    if len(formatlist) != 0:
        messagebox.showinfo('Notification', 'Corona Data is Saved {}'.format(path2), parent = root)
def download():
    global path
    if len(formatlist) != 0:
        path = filedialog.askdirectory()
    else:
        pass
    scrap()
    formatlist.clear()
    InHtml.configure(state = 'normal')
    InCsv.configure(state = 'normal')
    InJson.configure(state = 'normal')


def inhtml():
    formatlist.append('html')
    InHtml.configure(state = 'disabled')

def incsv():
    formatlist.append('csv')
    InCsv.configure(state = 'disabled')

def injson():
    formatlist.append('json')
    InJson.configure(state = 'disabled')


import plyer
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import *
from tkinter import messagebox, filedialog

root = Tk()
root.title("Corona Virus Information")
root.geometry("850x600+200+80")
root.configure(bg = "Light Grey")
formatlist = []
path = ''

################################ Labels

IntroLabel = Label(root, text = "CoronaVirus Information", font = ("MV Boli", 30, "bold"), bg = "Black", fg = "Orange", width = 37)
IntroLabel.place(x=0, y=0)

EntryLabel = Label(root, text = "Country Name: ", font = ("MV Boli", 20, "bold"), bg = "light grey", fg = "black", width = 15)
EntryLabel.place(x=10, y=100)

FormatLabel = Label(root, text = "Download in: ", font = ("MV Boli", 20, "bold"), bg = "light grey", fg = "black", width = 13)
FormatLabel.place(x=10, y=200)

################################ EntryBox

country_data = StringVar()
ent1 = Entry(root, textvariable = country_data, font = ("MV Boli", 20, "bold"), relief = RIDGE, bd = 2, width = 15)
ent1.place(x=300, y=100)

################################ Buttons

InHtml = Button(root, text = "Html", bg = "black", font = ("MV Boli", 15, "bold"), fg = "white", relief = RIDGE, activebackground = "cyan", activeforeground = "black")
InHtml.place(x=300, y=200, command = inhtml())

InCsv = Button(root, text = "Csv", bg = "black", font = ("MV Boli", 15, "bold"), fg = "white", relief = RIDGE, activebackground = "cyan", activeforeground = "black")
InCsv.place(x=400, y=200, command = incsv())

InJson = Button(root, text = "Json", bg = "black", font = ("MV Boli", 15, "bold"), fg = "white", relief = RIDGE, activebackground = "cyan", activeforeground = "black")
InJson.place(x=500, y=200, command = injson())

Submit = Button(root, text = "Submit", bg = "black", font = ("MV Boli", 15, "bold"), fg = "white", relief = RIDGE, activebackground = "cyan", activeforeground = "black")
Submit.place(x=400, y=400, command = download())

root.mainloop()