# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render
from dj.models import database_try
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import firebase_admin
import gmplot
import json
from firebase_admin import credentials,firestore
from firebase_admin import db
cred = credentials.Certificate('dj/team5-6ba3b-firebase-adminsdk-cukqn-ed12ccb9a0.json')
default_app = firebase_admin.initialize_app(cred,{'databaseURL':'https://team5-6ba3b.firebaseio.com'})
db = firestore.client()
class indexPage(TemplateView):
    def get(self, request, **kwargs):
        return render(request,'index.html')

class CenterHead(TemplateView):
    def get(self, request, **kwargs):
        return render(request,'centrehead.html')

class StatePage(TemplateView):
    def get(self, request, **kwargs):
        return render(request,'statehead.html')

class ProjectPage(TemplateView):
    def get(self, request, **kwargs):
        return render(request,'projecthead.html')


class Authentication(TemplateView):
    def get(self, request, **kwargs):
        self.un=request.GET['username']
        self.ps=request.GET['password']
        if self.un=="admin" and self.ps=="admin":
            '''
                query the database and get all the tables
                machine wise analytics, go to history of the usage database
                do a bar chart for a hobli, the machine and its count

                heat map of the currently used machines
                '''
            machine_table = db.collection(u'machine').get()
            machine_table = [doc.to_dict() for doc in machine_table]
            machine_table = pd.DataFrame(machine_table)
            j=json.loads(machine_table.to_json())
            print(j)
            l = len(j.values())
            print(l)
            # machine_table = pd.DataFrame({"Mech_id":[1,2,3,4,5,6],"Description":["A","B","C","D","E","E"]})

            State = db.collection(u'state').get()
            State = [doc.to_dict() for doc in State]
            State = pd.DataFrame(State)
            # State = pd.DataFrame({"State_id":[1,1,2,2],"Centre_id":[5,6,7,8],"State_name":["A","A","B","B"]})

            Centre = db.collection(u'hobli').get()
            Centre = [doc.to_dict() for doc in Centre]
            Centre = pd.DataFrame(Centre)

            # Centre = pd.DataFrame({"Centre_id":[5,6,7,8,8,8],"Centre":["AA","BB","CC","DD","DD","DD"],"Mech_id":[1,2,3,4,5,6],"Status":['U','N','U','N','U','N']})

            machines = pd.merge(Centre, machine_table, on=['machine_id'], how='inner')

            GPS = db.collection(u'GPS').get()
            GPS = [doc.to_dict() for doc in GPS]
            GPS = pd.DataFrame(GPS)

            hobli_choice = "Gulbarga"  # choose
            new_db = pd.merge(Centre[Centre.hobli_name == hobli_choice], machine_table, on=['machine_id'], how='inner')
            print(new_db)
            new_db.hobli_name.value_counts().plot.bar()
            plt.ylabel("number of machines")
            plt.xlabel("Machines")
            # plt.show()
            plt.savefig("media/mech_wise_mech_freq.png")

            return render(request, 'centre_analytics.html')
        else:
            return render(request,"error.html")


class Authentication2(TemplateView):
    def get(self, request, **kwargs):
        self.un=request.GET['username']
        self.ps=request.GET['password']
        if self.un=="admin" and self.ps=="admin":
            '''
                query the database and get all the tables
                district wise machines being used and taluk wise machines being used (count)
                also the machines not being used

                gps tracking of the individual machines
                '''
            machine_table = db.collection(u'machine').get()
            machine_table = [doc.to_dict() for doc in machine_table]
            machine_table = pd.DataFrame(machine_table)
            # machine_table = pd.DataFrame({"Mech_id":[1,2,3,4,5,6],"Description":["A","B","C","D","E","E"]})

            State = db.collection(u'state').get()
            State = [doc.to_dict() for doc in State]
            State = pd.DataFrame(State)
            # State = pd.DataFrame({"State_id":[1,1,2,2],"Centre_id":[5,6,7,8],"State_name":["A","A","B","B"]})

            Centre = db.collection(u'hobli').get()
            Centre = [doc.to_dict() for doc in Centre]
            Centre = pd.DataFrame(Centre)

            # Centre = pd.DataFrame({"Centre_id":[5,6,7,8,8,8],"Centre":["AA","BB","CC","DD","DD","DD"],"Mech_id":[1,2,3,4,5,6],"Status":['U','N','U','N','U','N']})

            machines = pd.merge(Centre, machine_table, on=['machine_id'], how='inner')

            GPS = db.collection(u'GPS').get()
            GPS = [doc.to_dict() for doc in GPS]
            GPS = pd.DataFrame(GPS)

            # GPS = pd.DataFrame({"id":[x for x in range(5)],"Mech_id":[1,2,3,4,5],"Lat":[45,46,47,48,49],"Long":[45,46,47,48,49]})

            state_choice = "Karnataka"
            new_state = State[State.state_name == state_choice]
            new_db = pd.merge(new_state, Centre, on=["centre_id"], how='inner')
            # print(new_db)
            new_db.hobli_name.value_counts().plot.bar()
            plt.ylabel("Number of machines")
            plt.xlabel("Centers")
            # plt.save_fig("centre_wise_mech_freq.png")
            plt.savefig("media/State_wise_mech_freq.png")

            new_state = State[State.state_name == state_choice]
            new_db = pd.merge(new_state, Centre, on=["centre_id"], how='inner')
            new_db = pd.merge(new_db, machine_table, on=["machine_id"], how='inner')
            # print(new_db)
            new_db.machine_name.value_counts().plot.bar()
            plt.xlabel("State : " + state_choice)
            plt.ylabel("frequency")
            plt.savefig("media/State_wise_mech_freq.png")
            print("swmf")
            '''unused = new_db[new_db.status == 'U']
            used = new_db[new_db.status == 'N']
            unused.machine_name.value_counts().plot.bar()
            plt.xlabel("machines")
            plt.ylabel("count")
            plt.savefig("media/unused_stats.png")

            used.machine_name.value_counts().plot.bar()
            plt.xlabel("machines")
            plt.ylabel("count")
            plt.savefig("media/used_stats.png")
            '''
            latitudes = GPS.lat.tolist()  # [34.0522 for x in range(500)]#GPS["Lat"]
            longitudes = GPS.long.tolist()  # [-118.2437 for x in range(500)]#GPS["Long"]
            gmap = gmplot.GoogleMapPlotter(latitudes[0], longitudes[0], 10)
            # Overlay our datapoints onto the map
            gmap.heatmap(latitudes, longitudes)
            gmap.draw("dj/templates/my_heatmap.html")
            return render(request, 'state_analytics.html')
        else:
            return render(request, "error.html")

class Authentication3(TemplateView):

    def get(self, request, **kwargs):
        self.un = request.GET['username']
        self.ps = request.GET['password']
        if self.un == "admin" and self.ps == "admin":
            return render(request,'l1.html')
        else:
            return render(request, "error.html")
class Myheat(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'my_heatmap.html')

class Display(TemplateView):
    def get(self, request, **kwargs):
        self.usn = request.GET['usn']
        name = request.GET['name']
        ob=database_try(artist=name,usn=self.usn)
        ob.save()
        return render(request, 'display.html',{'name':name,'usn':self.usn})

class display2(TemplateView):
    def get(self, request, **kwargs):
        all_data=database_try.objects.all()
        pic="Screenshot(2).png"
        return render(request, 'database.html', {'all_data':all_data,'pic1':pic})



# Create your views here.
