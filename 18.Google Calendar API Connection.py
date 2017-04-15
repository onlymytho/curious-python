#!/usr/bin/env python
# coding: utf-8
# 참고 : https://opentutorials.org/course/2581
#
# 예제 내용
# * 기본 위젯을 사용하여 기본 창을 생성
# * 다양한 레이아웃 위젯 사용

from __future__ import print_function

import sys
import httplib2
import os
import re

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QLabel, QSpacerItem, QLineEdit, QTextEdit, QPushButton, QGroupBox, QTableWidgetItem, QTableWidget
from PyQt5.QtWidgets import QBoxLayout, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout




# 구글 캘린더 API를 불러오기 위한 사전 작업
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'  # 같은 디렉토리 내에 있고, 구글 API 대시보드에서 받을 수 있음.
APPLICATION_NAME = 'Google Calendar Handling Program'

# 구글 캘린더 API 사용자 정보 획득
def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

# 구글 캘린더 API를 활용해 일정 정보 받아오기
events = []
event_start_date = []
event_start_time = []
event_end_date = []
event_end_time = []
event_summary = []

def get_events():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 50 events')
    eventsResult = service.events().list(
        calendarId='balmbees.com_6iidih380qg63vn7hsa4b0v5qc@group.calendar.google.com',
        timeMin=now,
        maxResults=50,
        singleEvents=True,
        orderBy='startTime'
        ).execute()
    events_dict = eventsResult.get('items', [])
    if not events_dict:
        print('No upcoming events found.')
    for event in events_dict:
        start_date = event['start'].get('dateTime').split('T')[0]
        start_time_pre = event['start'].get('dateTime')
        start_time = str(re.split('[T + :]', start_time_pre)[1])+":"+re.split('[T + :]', start_time_pre)[2]

        end_date = event['end'].get('dateTime').split('T')[0]
        end_time_pre = event['end'].get('dateTime')
        end_time = str(re.split('[T + :]', end_time_pre)[1])+":"+re.split('[T + :]', end_time_pre)[2]

        summary = event['summary']

        event_start_date.append(start_date)
        event_start_time.append(start_time)
        event_end_time.append(end_time)
        event_summary.append(summary)

    events.append(event_start_date)
    events.append(event_start_time)
    events.append(event_end_time)
    events.append(event_summary)
    print('Getting events is done.')



# 프로그램 뷰 생성하기
class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        print ("Creating view.")
        self.setWindowTitle(APPLICATION_NAME)
        self.setFixedWidth(800)
        self.setFixedHeight(480)

        layout_base = QGridLayout(self)
        self.setLayout(layout_base)

        # # 구글 캘린더 API를 활용해 일정 정보 받아오는 부분 미리 실행
        get_events()

        # 그룹 QGridLayout
        grp_1 = QGroupBox("Events")
        layout_base.addWidget(grp_1, 1,1)
        grp_1_layout = QGridLayout()
        grp_1_layout.setSpacing(10)

        ## QtTableView 호출
        tableWidget = QTableWidget()
        tableWidget.setRowCount(len(event_start_date))
        tableWidget.setColumnCount(len(events))

        for i in range(0,len(event_start_date)):
            for n in range(0, len(events)):
                tableWidget.setItem(i, n, QTableWidgetItem(events[n][i]))
                print (str(n+1) + ", " + str(i+1) + ", " + events[n][i])
        grp_1.setLayout(grp_1_layout)
        grp_1_layout.addWidget(tableWidget, 1, 0)

        # 그룹 컨트롤 영역
        grp_2 = QGroupBox("ControlBox")
        layout_base.addWidget(grp_2, 2,1)
        grp_2_layout = QGridLayout()
        grp_2_layout.setSpacing(10)

        grp_2.btns = []
        grp_2.btns_text = ["동기화", "크기", "동기화"]
        for i in grp_2.btns_text:
            grp_2.btns.append(QPushButton(i))

        ## grp_2 QGridLayout에 Listview와 QLineEdit 삽입
        grp_2.setLayout(grp_2_layout)
        ### addWidget(*Widget, row, column, rowspan, colspan)
        grp_2_layout.addWidget(QLineEdit(), 1, 1)
        for i in grp_2.btns:
            i.setFixedSize(60, 30)
            i.setStyleSheet("border:1px solid #dfdfdf")
            grp_2_btn_layout.addWidget(i)


        print ("Creating view is done.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    print ("Let's Go")
    form.show()
    print ('Running...')
    exit(app.exec_())
