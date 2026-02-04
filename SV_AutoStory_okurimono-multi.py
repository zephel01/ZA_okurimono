from Commands.PythonCommandBase import ImageProcPythonCommand
from Commands.Keys import Button, Hat, Direction, Stick
#from Commands.PythonCommands.KeyBoardTest import KeyBoardTest
from Commands.PythonCommands.ImageProcessingOnly.SV_AutoStory_matome import AutoStory_matome
import os
import cv2
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import numpy as np
import time
import math

class AutoStory(AutoStory_matome,ImageProcPythonCommand):
    NAME = 'SVストーリー自動化_おくりもの_ver2.0'

    def __init__(self,cam,gui=None):
        super().__init__(cam)
        self.cam = cam
        #self.gui = gui

    def do(self):
        

        #ストーリーをふしぎなおくりものを受け取れるところまで進めてpokemonhomeに受け取ったポケモンを預けた後データを削除し再びループします
        #データ削除を行うので使用する際は自己責任でお願いします
        #self.dleteData()がデータを削除する関数なので、最初はコメントアウトしておいて様子を見た方がいいかもしれません



        #事前準備
        #pokemonhomeに課金していないユーザーを使用する
        #testフォルダ内のsavedata.pngを削除したいユーザーの画像に差し替えておく（誤検知で別のデータを消してしまわないよう他ユーザーとはっきり区別のつくようなアイコンに変えておく）      
        #下記の変数に目を通し、必要であれば書き換えておく
        #新規データでゲームを開始し、言語選択画面からスタート

        #言語選択、日本語ROMの場合、上からJPN,ENG,ESP,FRE,GER,ITA,KOR,CHS,CHTの順にlang_list=0~7選択
        self.lang_list = [
            1
            #0, 1, 2, 3, 4, 5, 6, 7, 8,
            #7, 8
            #0, 1, 2, 3, 4,
            #0, 2 ,7, 8, 7, 8
            #8, 7, 6, 0, 7, 8, 1
        ]
        self.code_list = [
            [2, 4, 6, 8],
            #[2, 'W0RLDSARM0RTA1L'],
            #['L1KEAFLUTE'],  #1周目
            #['THA12022CHAMP','GETY0URMEW', 'E301PKQFSCNP24T6'],  #2周目
            #['THA12022CHAMP','GETY0URMEW'],  #3周目
            #['THA12022CHAMP']  #4周目

            
        ]                               #パスワード 'THA12022CHAMP', 'DARKTERA0006', 'GETY0URMEW, "23WCSGASTR0D0N"
                                        #リストの数がself.count_maxより小さい場合はリストの1番目のコードを打ち込みます

        self.count_max = 1              #何回繰り返すか
        self.version = "V"              #"S"がスカーレット、"V"がバイオレット
        self.name = "アオイ"
        #self.name = "バイオレット"


        test_mode = 0                   #セーブデータ消去のテストモードです HOME画面左端のソフトにカーソルを合わせた状態でスタート 0でoff、1でon
                                        #セーブデータ消去関数を使う場合は必ずここで何度かテストしてから使ってください
                                        #選択したバージョンかつ指定したデータにカーソルがあった状態で"ok”と表示されれば成功です
                                        #データの選択がうまくいかない場合はsavedata.pngの閾値を変更したり別の画像を使ってみてください
                                        



        #ここまで


        self.move_time = 2.0        #目的地に着いたときに余分に動く時間
        self.map = 0                #0でパルデアマップ 1でキタカミマップ
        self.map_3 = cv2.imread("./Template/SV/Auto_story/map_3.png", cv2.IMREAD_GRAYSCALE)
        self.map_kitakami = cv2.imread("./Template/SV/Auto_story/map_kitakami.png", cv2.IMREAD_GRAYSCALE)
        count = 1
        self.yasei_count = 0
        self.encount_timer_start = 0
        self.encount_timer_end = time.time()
        self.start_time = time.time()

        self.matome_init()

        if self.version == "S":
            print("バージョン:スカーレット")
        elif self.version == "V":
            print("バージョン:バイオレット")
        else:
            print("バージョンが指定されていません")
            self.finish()
        
        if test_mode == 1:
            print("セーブデータ選択テスト")
            self.pressRep(Button.B, wait=0.1, repeat=10, duration=0.1, interval=0.1)
            self.dleteData(test=True)
        
        for i in range(self.count_max):
            start = time.time()
            try:
                self.lang = self.lang_list[i]
            except:
                self.lang = self.lang_list[0]
            try:
                self.code = self.code_list[i]
            except:
                self.code = self.code_list[0]

            print(count, "周目開始", self.count_max, "周目まで続けます")
            self.lang_name = [
                "JPN", "ENG", "ESP", "FRA", "GER",
                "ITA", "KOR", "CHS", "CHT"
            ]
            print("lang:", self.lang_name[self.lang])
            print("code:", self.code)
            self.neutral()
            self.characterSetting()
            self.opening()
            self.firstpokemon()
            self.firstbattle()
            self.irienohoraana()
            self.todai()
            self.goToteburu_1()
            #self.receiveGift()
            #self.pokemonHome()
            #self.dleteData()
            #self.goToteburu_2()
            #self.teburucity()
            print(count, "周目終了")
            print(f"周回時間:{self.elapsed_time_str(time.time()-start)}", f"経過時間:{self.elapsed_time_str(time.time()-self.start_time)}\n")
            count += 1

    def characterSetting(self):
        #言語選択
        while not self.isContainTemplate('SV/Auto_story/language.png', 0.85, use_gray=False):
            self.wait(0.1)
        self.pressRep(Button.B, wait=0.1, repeat=10, duration=0.1, interval=0.1)
        #日本語
        self.pressRep(Direction.DOWN, wait=0.1, repeat=self.lang, duration=0.1, interval=0.1)
        self.press(Button.A,0.1,3.0)
        #キャラ選択
        self.press(Direction.RIGHT,0.1,0.3)
        self.press(Direction.RIGHT,0.1,0.3)
        self.press(Direction.RIGHT,0.1,0.3)
        self.press(Button.A,0.1,3.0)
        # self.KeyBoard_Init()
        # self.TypeString(self.name)
        #名前 カタカナ
        #self.press(Direction.LEFT,0.1,0.3)
        #self.press(Button.A,0.1,0.3)
        #アオイ
        #self.press(Direction.RIGHT,2.0,0.5)
        #self.press(Direction.LEFT,0.1,0.3)
        #self.press(Button.A,0.1,0.3)
        #self.press(Direction.DOWN,0.8,0.3)
        #self.press(Button.A,0.1,0.3)
        #self.press(Direction.UP,0.8,0.5)
        #self.press(Direction.DOWN,0.1,0.3)
        self.press(Button.A,0.1,0.3)
        if self.lang_name[self.lang] == "KOR" \
            or self.lang_name[self.lang] == "CHS" \
            or self.lang_name[self.lang] == "CHT":
            self.press(Button.PLUS,0.1,0.3)
        self.press(Button.PLUS,0.1,0.3)

    def receiveGift(self):
        for i in range(len(self.code)):
            if isinstance(self.code[i], int):
                print("\nおくりものを受け取ります", "インターネットで受け取る:", self.code[i], "番目")
            else:
                print("\nおくりものを受け取ります", "code:", self.code[i])
            self.openMenu()
            while not self.isContainTemplate('SV/Auto_story/selectPortal.png', 0.85):
                self.press(Direction.DOWN,0.05,0.5)
            while self.isContainTemplate('SV/Auto_story/selectPortal.png', 0.85):
                self.press(Button.A,0.1,0.5)
            while not self.isContainTemplate('SV/Auto_story/pokeportal.png', 0.85):
                self.wait(0.1)
            while not self.isContainTemplate('SV/Auto_story/mysterygift.png', 0.85):
                self.press(Direction.UP,0.05,0.5)
            while self.isContainTemplate('SV/Auto_story/mysterygift.png', 0.85):
                self.press(Button.A,0.1,2.0)
            if isinstance(self.code[i], int):
                # 「インターネットで受け取る」を選択
                # 初回接続時のみインターネット接続に必要な情報を受け取る
                self.press(Button.A,0.1,0.3)
                self.press(Button.A,0.1,0.3)
                self.press(Button.A,0.1,0.3)
                self.press(Button.A,0.1,0.3)
                self.press(Button.A,0.1,0.3)
                self.press(Button.A,0.1,0.3)
                self.wait(1.0)
                while not self.isContainTemplate(
                        'SV/Auto_story/internet_okurimono.png',
                        0.85, True, crop=[345, 155, 935, 185]):
                    self.press(Button.A,0.1,5.0)
                # ここから「指定した数字」番目の贈り物を選択
                if self.isContainTemplate(
                        'SV/Auto_story/internet_okurimono_cancel.png',
                        0.85, True, crop=[1135, 375, 1175, 525]):
                    self.press(Button.B,0.1,1.0)
                count = 1
                while count < self.code[i]:
                    self.press(Direction.DOWN,0.05,0.5)
                    count += 1
                # Aで受け取り（受け取り済みの場合はメッセージ表示）
                self.press(Button.A,0.1,4.5)
                # ポケモン受け取りなら図鑑に登録、B入力（アイテム等なら受け取ったアイテム一覧画面、Bで受け取っていない贈り物画面へ）
                self.press(Button.B,0.1,1.0)
                self.wait(5.0)
                while not self.isContainTemplate(
                        'SV/Auto_story/internet_okurimono.png',
                        0.85, True, crop=[345, 155, 935, 185]):
                    self.press(Button.B,0.1,2.0)
                if not self.isContainTemplate(
                        'SV/Auto_story/internet_okurimono_cancel.png',
                        0.85, True, crop=[1135, 375, 1175, 525]):
                    self.press(Button.B,0.1,1.2)
                # 一度インターネットで受け取る　を中止する
                self.press(Button.A,0.1,1.0)
            else:
                while not self.isContainTemplate('SV/Auto_story/serialcode.png', 0.85):
                    self.press(Direction.DOWN,0.05,0.5)
                count = 0
                while True:
                    flag = False
                    while not (self.isContainTemplate('SV/Auto_story/code_ok_black.png', 0.85) or self.isContainTemplate('SV/Auto_story/code_ok_white.png', 0.85)):
                        self.press(Button.A,0.05,0.5)
                    while (self.isContainTemplate('SV/Auto_story/code_ok_black.png', 0.85) or self.isContainTemplate('SV/Auto_story/code_ok_white.png', 0.85)):
                        self.press(Button.B,0.05,0.7)
                    self.typeCode(self.code[i])
                    while not self.isContainTemplate('SV/Auto_story/receive.png', 0.86, crop=[311,159,398,274], use_gray=False):
                        self.press(Button.PLUS,0.05,0.5)
                        if self.isContainTemplate('SV/Auto_story/error.png', 0.86, crop=[1138,649,1280,720], use_gray=False):
                            self.wait(0.5)
                            self.press(Button.B,0.1,1.5)
                            if not self.isContainTemplate('SV/Auto_story/serialcode.png', 0.85):
                                flag = True
                                count += 1
                                break
                            else:
                                print("おくりものを受け取れませんでした")
                                self.finish()
                    if flag:
                        if count == 3:
                            print("おくりものを受け取れませんでした")
                            self.finish()
                        else:
                            print("おくりものを受け取れなかったのでやり直します", count, "/", 3)
                            continue
                    else:
                        break   
                self.pressRep(Button.A, wait=1.0, repeat=20, duration=0.1, interval=0.3)
                while not self.isContainTemplate('SV/Auto_story/finish_okurimono.png', 0.85, crop=[844,400,1018,700], use_gray=False):
                    self.press(Button.B,0.1,0.8)
                self.press(Button.B,0.1,0.5)
                self.press(Button.B,0.1,0.5)
                #while not self.isContainTemplate('SV/Auto_story/finish_okurimono_1.png', 0.85, crop=[810,576,1090,714], use_gray=False):
                while not self.isContainTemplate('SV/Auto_story/serialcode.png', 0.85):
                    self.press(Button.B,0.1,0.8)
                self.wait(0.5)
            self.press(Button.B,0.1,1.8)
            self.press(Button.A,0.1,0.1)
        self.temochiIrekae_test(1)
        self.report()

    def pokemonHome(self):
        save_flag = 0
        while not (self.chkReturnHome()):
            self.press(Button.HOME,0.05,1.5)
        while not (self.isContainTemplate('SV/Auto_story/select_home_black1.png', 0.8) or self.isContainTemplate('SV/Auto_story/select_home_white1.png', 0.8)):
            self.press(Hat.RIGHT,0.1,1.0)
        #終了する
        #起動
        self.renda(Button.A, 10.0)
        while not self.isContainTemplate('SV/Auto_story/home_login.png',0.85, use_gray=True, show_value=False):
            self.press(Button.A,0.1,0.5)
        while True:
            error_flag = 0
            while not self.isContainTemplate('SV/Auto_story/pokemonhome.png',0.85, use_gray=True, show_value=False):
                self.wait(0.1)
                if self.isContainTemplate('SV/Auto_story/errormessage.png',0.85, use_gray=True, show_value=False):
                    self.renda(Button.A, 5.0)
                if self.isContainTemplate('SV/Auto_story/errorNoOperation.png',
                        0.85, use_gray=True, show_value=False, crop=[350, 100, 720, 320]):
                    self.renda(Button.A, 5.0)
                if self.isContainTemplate('SV/Auto_story/errorInternet.png',
                        0.85, use_gray=True, show_value=False, crop=[350, 100, 720, 320]):
                    self.renda(Button.A, 5.0)
                if self.isContainTemplate('SV/Auto_story/errorDns.png',
                        0.85, use_gray=True, show_value=False, crop=[350, 100, 720, 320]):
                    self.press(Button.A,0.1,5.0)
                    while not self.isContainTemplate(
                            'SV/Auto_story/errorDns.png', 0.85, use_gray=True,
                            show_value=False, crop=[350, 100, 720, 320]):
                        self.press(Button.A,0.1,5.0)
                    self.press(Button.B,0.1,3.0)
                if self.isContainTemplate('SV/Auto_story/home_login.png',
                                          0.85, use_gray=True, show_value=False):
                    self.press(Button.A,0.1,0.5)
            #メインメニュー
            self.press(Button.A,0.1,2.0)
            self.press(Button.A,0.1,1.0)
            self.press(Button.A,0.1,1.0)
            while not self.isContainTemplate('SV/Auto_story/homebox.png',0.85, use_gray=True, show_value=False):
                self.wait(0.1)
                if self.isContainTemplate('SV/Auto_story/errormessage.png',0.85, use_gray=True, show_value=False):
                    self.renda(Button.A, 5.0)
                    error_flag = 1
                    break
            if error_flag == 1:
                continue
            self.wait(1.0)
            #ボックス操作 フリーボックスの一番右下へおく
            self.pressRep(Direction.LEFT, wait=0.6, repeat=6, duration=0.1, interval=0.6)
            #self.pressRep(Direction.DOWN, wait=0.6, repeat=1, duration=0.1, interval=0.6)
            x = 0
            while not self.isContainTemplate('SV/Auto_story/homebox_2.png',0.85, use_gray=True, show_value=False):
                self.wait(0.1)
                x += 1
                if x > 5:
                    if save_flag == 1:
                        x = 0
                        print("ポケモン確認")
                        break
                    else:
                        error_flag = 1
                        break
            if error_flag == 1:
                while not (self.chkReturnHome()):
                    self.press(Button.HOME,0.05,1.5)
                self.pressRep(Button.Y, wait=0.1, repeat=5, duration=0.1, interval=0.1)
                self.renda(Button.A, 12.0)
                continue
            if len(self.code) > 1:
                while not self.isContainTemplate('SV/Auto_story/home_hukusu.png', 0.82, use_gray=False):
                    self.press(Button.ZL,0.1,0.7)
                self.press(Button.A,0.1,1.0)
                self.pressRep(Direction.RIGHT, wait=0.6, repeat=len(self.code)-1, duration=0.1, interval=0.6)
                self.press(Button.A,0.1,1.0)
                self.pressRep(Direction.DOWN, wait=0.6, repeat=4, duration=0.1, interval=0.6)
                self.pressRep(Direction.LEFT, wait=0.6, repeat=len(self.code), duration=0.1, interval=0.6)
                self.press(Button.A,0.1,1.0)
            else:
                self.press(Button.Y,0.1,1.0)
                self.pressRep(Direction.DOWN, wait=0.6, repeat=4, duration=0.1, interval=0.6)
                self.press(Hat.LEFT,0.1,0.3)
                self.press(Button.Y,0.1,1.0)
            #セーブ
            self.press(Button.PLUS,0.1,1.0)
            self.press(Button.A,0.1,0.1)
            self.press(Button.A,0.1,0.5)
            while not self.isContainTemplate('SV/Auto_story/homesave.png',0.85, use_gray=True, show_value=False):
                self.wait(0.1)
                if self.isContainTemplate('SV/Auto_story/errormessage.png',0.85, use_gray=True, show_value=False):
                    self.renda(Button.A, 5.0)
                    error_flag = 1
                    save_flag = 1
                    break
            if error_flag == 1:
                continue
            else:
                break
        self.press(Button.A,0.1,0.5)
        self.press(Button.HOME,0.1,2.0)
        while not (self.chkReturnHome()):
            self.wait(0.1)
        self.press(Button.X,0.1,1.0)
        self.press(Button.A,0.1,2.0)

    def dleteData(self, test=False):
        while True:
            self.press(Direction.LEFT, 0.05, 0.3)
            self.press(Direction.DOWN, 0.05, 0.3)
            self.press(Direction.LEFT, 0.05, 0.3)
            self.press(Button.A, 0.05, 1.2)
            self.pressRep(Direction.DOWN, wait=0.3, repeat=6, duration=0.1, interval=0.3)
            self.press(Button.A, 0.05, 0.5)
            self.press(Direction(Stick.LEFT, 270),duration=1.0, wait=0.3)
            self.press(Button.A, 0.05, 2.2)
            #SVにカーソル
            for i in range(10):
                self.press(Direction.DOWN, 0.2, 0.8)
                if self.isContainTemplate('SV/Auto_story/test/'+self.version+'/select_data_white.png',0.9, use_gray=False, show_value=False) \
                or self.isContainTemplate('SV/Auto_story/test/'+self.version+'/select_data_black.png',0.9, use_gray=False, show_value=False):
                    break
            else:
                self.press(Button.HOME, 0.1, 1.5)
                while not (self.chkReturnHome()):
                    self.wait(0.1)
                continue
            self.press(Button.A, 0.1, 1.0)
            #アカウントを変える場合は変更が必要
            if self.isContainTemplate('SV/Auto_story/test/'+self.version+'/savedata_white2.png',0.9, use_gray=False, show_value=False)\
            or self.isContainTemplate('SV/Auto_story/test/'+self.version+'/savedata_black2.png',0.9, use_gray=False, show_value=False):
                for i in range(10):
                    if self.isContainTemplate('SV/Auto_story/test/savedata2.png',0.9, use_gray=False, show_value=False):
                        break
                    self.press(Direction.DOWN, 0.2, 0.8)
                else:
                    self.press(Button.HOME, 0.1, 1.5)
                    while not (self.chkReturnHome()):
                        self.wait(0.1)
                    continue
                self.wait(0.5)
                check = 0
                for i in range (0, 5):
                    if self.isContainTemplate('SV/Auto_story/test/savedata2.png',0.9, use_gray=False, show_value=False):
                        check += 1
                if check == 5:
                    print("ok")
                    if test:
                        self.finish()
                    self.press(Button.A, 0.1, 3.5)
                    self.press(Direction.UP, 0.1, 0.5)
                    self.press(Button.A, 0.1, 2.5)
                    self.press(Button.A, 0.1, 0.5)
                    self.press(Button.HOME, 0.1, 1.2)
                    while not (self.chkReturnHome()):
                        self.wait(0.1)
                    self.press(Direction.RIGHT, 0.1, 0.5)
                    self.renda(Button.A, 5.0)
                    break
                else:
                    self.press(Button.HOME, 0.1, 1.5)
                    while not (self.chkReturnHome()):
                        self.wait(0.1)
                    continue 
            else:
                self.press(Button.HOME, 0.1, 1.5)
                while not (self.chkReturnHome()):
                    self.wait(0.1)
                continue

    def typeCode(self, code):
        self.keyboard= ["1234567890",
                        "QWERTYUIOP",
                        "ASDFGHJKL",
                        "ZXCVBNM"
                        ] 
        x_pos, y_pos = 0, 0
        for i in range (len(code)):
            key = code[i]
            y_1 = [s for s in self.keyboard if key in s][0]
            y = self.keyboard.index(y_1)
            x = y_1.index(key)
            X_d, y_d = x - x_pos, y - y_pos
            if X_d > 0:
                direction_x = Direction.RIGHT
            else:
                direction_x = Direction.LEFT
            if y_d > 0:
                direction_y = Direction.DOWN
            else:
                direction_y = Direction.UP
            self.pressRep(direction_x, wait=0.1, repeat=abs(X_d), duration=0.1, interval=0.1)
            self.pressRep(direction_y, wait=0.1, repeat=abs(y_d), duration=0.1, interval=0.1)
            x_pos += X_d
            y_pos += y_d
            self.press(Button.A,0.1,0.1)

    def temochiIrekae_test(self,x=1):
        print("手持ちを", x, "匹にする")
        while True:
            temochi = self.temochiCheck()
            print("現在手持ち", temochi , "匹")
            if temochi == x:
                self.returnTofield(button=Button.B)
                break
            if temochi < x:
                self.press(Button.MINUS,0.1,0.5)
                self.pressRep(Direction.DOWN, wait=0.5, repeat=x-2, duration=0.1, interval=0.3)
                self.press(Button.A,0.1,0.5)
                self.press(Direction.LEFT, 0.1, 0.5)
                self.pressRep(Direction.DOWN, wait=0.5, repeat=temochi, duration=0.1, interval=0.3)
                self.press(Button.A,0.1,0.5)
                continue
            else:
                self.press(Direction.LEFT, 0.1, 0.5)
                self.pressRep(Direction.DOWN, wait=0.5, repeat=x, duration=0.1, interval=0.1)
                self.press(Button.MINUS,0.1,0.5)
                self.press(Direction.DOWN, 1.0, 0.5)
                self.press(Button.A,0.1,0.5)
                self.press(Direction.RIGHT, 0.1, 0.5)
                count = 0
                while not self.isContainTemplate('SV/Auto_story/box_ichiran.png', 0.85, use_gray=False):
                    self.press(Direction.UP, 0.1, 0.5)
                    count += 1
                    if count % 8 == 0:
                        break
                if count % 8 == 0:
                    continue
                self.pressRep(Button.A, wait=0.5, repeat=3, duration=0.1, interval=0.5)
                continue

        

    
