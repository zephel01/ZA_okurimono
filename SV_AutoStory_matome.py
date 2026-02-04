from Commands.PythonCommandBase import ImageProcPythonCommand
from Commands.Keys import Button, Hat, Direction, Stick
import os
import cv2
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import numpy as np
import time
import math

class AutoStory_matome(ImageProcPythonCommand):
    def __init__(self,cam,gui=None):
        super().__init__(cam)
        self.cam = cam
        #self.gui = gui

    def chkMod32(self):
        self.is_mod32 = hasattr(
            self.keys, "hold_buttons"
        )

    def matome_init(self):
        self.chkMod32()
        self.maru_mode = 2
        #0:maru.png,閾値0.82で判定、1:self.marufile,閾値0.82で判定、
        #2:初回成功までmaru.png,閾値self.initmaruThで判定、
        #  初回判定成功時にself.marufileをキャプチャし、
        #  self.maru_modeを2→1に変更して動作する
        self.marufile = 'SV/Auto_story/test/'+self.version+'/capmaru'
        self.initmaruTh = 0.7

    def neutral(self, wait=0.1):
        if self.is_mod32:
            self.keys.neutral()
        else:
            btns = self.keys.holdButton
            self.keys.holdButton = []
            #btns = self.keys.hold_buttons
            #self.keys.hold_buttons = []
            self.keys.format.resetAllButtons()
            self.keys.format.resetAllDirections()
            self.keys.inputEnd(btns, unset_hat=True)
        self.wait(wait)

    def chkReturnHome(self):
        ret = self.isContainTemplate('SV/Auto_story/home_black.png', 0.8) \
            or self.isContainTemplate('SV/Auto_story/home_white.png', 0.8) \
            or self.isContainTemplate('SV/Auto_story/home_black2.png', 0.8) \
            or self.isContainTemplate('SV/Auto_story/home_white2.png', 0.8)
        return ret

    def opening(self):
        start = time.time()
        print("ストーリー開始")
        while not self.isContainTemplate('SV/Auto_story/opening.png', 0.9):
            self.press(Button.A,0.1,0.1)
        print("自宅")
        self.neutral()
        self.press(Direction.DOWN,3.0,1.0)
        while not self.isContainTemplate('SV/Auto_story/opening.png', 0.9):
            self.wait(0.1)
        while True:
            self.neutral()
            self.press(Direction.LEFT,4.0,0.1)
            while not self.isContainTemplate('SV/Auto_story/menu.png', 0.8, crop=[1120,660,1280,720],show_value=False):
                self.press(Button.X,0.1,1.5)
            self.press(Button.A,0.1,1.5)
            #話のはやさ
            self.press(Direction.RIGHT,0.05,0.3)
            self.press(Direction.DOWN,0.05,0.3)
            #わざ覚えスキップ
            self.press(Direction.RIGHT,0.05,0.3)
            self.press(Direction.DOWN,0.05,0.3)
            #ボックス
            self.press(Direction.RIGHT,0.05,0.3)
            self.press(Direction.DOWN,0.05,0.3)
            #ニックネーム
            self.press(Direction.RIGHT,0.05,0.3)
            self.press(Direction.DOWN,0.05,0.3)
            self.press(Direction.DOWN,0.05,0.3)
            self.press(Direction.DOWN,0.05,0.8)
            #カメラサポート
            self.press(Direction.DOWN,0.05,0.8)
            self.press(Direction.DOWN,0.05,0.8)
            self.press(Direction.DOWN,0.05,0.8)
            #おまかせレポート
            self.press(Direction.RIGHT,0.05,0.3)
            self.press(Direction.DOWN,0.05,0.8)
            self.press(Direction.DOWN,0.05,0.8)
            #ムービースキップ
            self.press(Direction.RIGHT,0.05,0.3)
            self.press(Direction.DOWN,1.5,0.1)
            #お助け機能
            self.press(Direction.RIGHT,0.05,0.5)
            self.pressRep(Button.A, wait=0.1, repeat=11, duration=0.1, interval=0.5)
            while not self.isContainTemplate('SV/Auto_story/menu_1.png', 0.8, crop=[1158,198,1232,266],show_value=False):
                self.press(Button.A,0.1,1.5)
            self.pressRep(Button.B, wait=0.1, repeat=10, duration=0.1, interval=0.1)   
            #ママのところへ
            self.press(Direction(Stick.LEFT, 90), duration=2.5, wait=0.1)
            self.press(Direction(Stick.LEFT, 180), duration=4.0, wait=0.1)
            self.press(Direction(Stick.LEFT, 270), duration=2.5, wait=6.0)
            self.press(Direction(Stick.LEFT, 270), duration=2.5, wait=0.1)
            self.press(Direction(Stick.LEFT, 180), duration=7.5, wait=0.1)
            self.renda(Button.A, 18)
            self.press(Direction(Stick.LEFT, 270), duration=2.0, wait=0.1)
            self.press(Direction(Stick.LEFT, 0), duration=7.5, wait=0.1)
            self.renda(Button.A, 34)
            #カバンを取りに行く
            self.press(Direction(Stick.LEFT, 0), duration=2.1, wait=0.1)
            self.press(Direction(Stick.LEFT, 90), duration=4.5, wait=0.1)
            self.press(Direction(Stick.LEFT, 0), duration=5.4, wait=0.1)
            self.press(Direction(Stick.LEFT, 270), duration=4.5, wait=0.1)
            self.press(Direction(Stick.LEFT, 0), duration=1.6, wait=0.1)
            self.press(Direction(Stick.LEFT, 90), duration=0.95, wait=0.1)
            self.renda(Button.A, 17)
            #クラベルのところへ
            self.press(Direction(Stick.LEFT, 180), duration=2.4, wait=0.1)
            self.press(Direction(Stick.LEFT, 90), duration=2.6, wait=0.1)
            self.press(Direction(Stick.LEFT, 180), duration=4.0, wait=0.1)
            self.press(Direction(Stick.LEFT, 270), duration=4.0, wait=0.1)
            self.press(Direction(Stick.LEFT, 180), duration=2.4, wait=0.1)
            self.renda(Button.A, 19)
            self.press(Direction(Stick.LEFT, 315), duration=2.9, wait=0.1)
            self.renda(Button.A, 90)
            if not self.fieldCheck():
                self.resetmyhome()
                continue
            else:
                break
        print(f"かかった時間:{self.elapsed_time_str(time.time()-start)}", f"経過時間:{self.elapsed_time_str(time.time()-self.start_time)}\n")

    def resetmyhome(self):
        #ソフトリセット
        print("\nリセットします")
        self.neutral()
        while not (self.chkReturnHome()):
            self.press(Button.HOME,0.05,1.5)
        self.pressRep(Button.X, wait=0.1, repeat=3, duration=0.1, interval=0.1)
        while not self.isContainTemplate('SV/Auto_story/myhome.png', 0.8, crop=[100, 0, 840, 140],show_value=False):
            self.press(Button.A,0.1,1.5)

    def firstpokemon(self):
        start = time.time()
        print("ネモ家へ")
        self.returnTofield(Button.A, 0.1, yasei=False)
        self.press(Direction(Stick.LEFT, 90), duration=36, wait=0.1)
        self.press(Direction(Stick.LEFT, 0), duration=0.5, wait=0.5)
        self.openMap()
        self.wait(1.0)
        self.pressRep(Button.A, wait=0.6, repeat=4, duration=0.1, interval=0.5)
        self.press(Button.RCLICK,0.1,0.3)
        self.press(Direction(Stick.LEFT, 347), duration=0.7, wait=0.1)   
        self.pressRep(Button.A, wait=0.5, repeat=2, duration=0.1, interval=0.8)
        self.pressRep(Button.B, wait=1.5, repeat=2, duration=0.1, interval=0.1)
        self.press(Direction(Stick.LEFT, 90), duration=12, wait=0.1)
        self.returnTofield(button=Button.A)
        print("御三家選択")
        self.press(Direction(Stick.LEFT, 90), duration=0.5, wait=0.1)
        self.pressRep(Button.A, wait=4.0, repeat=7, duration=0.1, interval=0.1)
        self.pressRep(Button.A, wait=0.1, repeat=15, duration=0.1, interval=0.2)
        self.pressRep(Button.B, wait=0.1, repeat=15, duration=0.1, interval=0.2)
        self.returnTofield(button=Button.A)
        #技入れ替え
        self.pressRep(Button.X, wait=0.6, repeat=4, duration=0.1, interval=0.1)
        self.pressRep(Button.A, wait=0.8, repeat=2, duration=0.1, interval=0.5)
        self.press(Direction.LEFT,0.5,0.5)
        self.pressRep(Button.A, wait=0.8, repeat=2, duration=0.1, interval=0.5)
        self.press(Direction.RIGHT,0.1,0.5)
        self.press(Button.Y,0.1,0.5)
        self.press(Button.A,0.1,0.5)
        self.press(Direction.DOWN,0.1,0.5)
        self.press(Direction.DOWN,0.1,0.5)
        self.press(Button.A,0.1,0.1)
        self.returnTofield(button=Button.B)
        self.pressRep(Button.ZR, wait=0.1, repeat=3, duration=0.1, interval=0.1)
        print(f"かかった時間:{self.elapsed_time_str(time.time()-start)}", f"経過時間:{self.elapsed_time_str(time.time()-self.start_time)}\n")

    def firstbattle(self):
        start = time.time()
        #ネモのところへ     
        self.pinAndmove(deg=315, duration=0.3, duration_move=12)
        self.report()
        self.pressRep(Button.ZR, wait=0.1, repeat=3, duration=0.1, interval=0.1)
        while True:
            self.pinAndmove(deg=37, duration=0.8, duration_move=5)       
            self.openMap()
            self.press(Button.Y,0.1,1.5)       
            self.pressRep(Button.L, wait=0.3, repeat=3, duration=0.1, interval=0.1)       
            self.hold(Direction(Stick.LEFT, 90))
            self.pressRep(Button.A, wait=0.1, repeat=32, duration=0.1, interval=0.1)
            self.holdEnd(Direction(Stick.LEFT, 90))

            self.press(Direction(Stick.LEFT, 300), duration=0.3, wait=0.1)
            self.pressRep(Button.L, wait=0.3, repeat=3, duration=0.1, interval=0.1)
            self.hold(Direction(Stick.LEFT, 90))
            self.pressRep(Button.A, wait=0.1, repeat=10, duration=0.1, interval=0.1)
            self.holdEnd(Direction(Stick.LEFT, 90))
            self.wait(4.5)
            if not self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],show_value=True):
                self.reset() 
                continue
            else:
                break
        #ネモとバトル
        self.returnTofield(Button.A ,0.1, yasei=False)
        self.press(Direction(Stick.LEFT, 90), duration=3.0, wait=0.1)
        self.report()
        self.pressRep(Button.ZR, wait=0.1, repeat=3, duration=0.1, interval=0.1)
        #ママのところへ
        while True:
            self.press(Direction(Stick.LEFT, 90), duration=9.0, wait=0.1) 
            self.press(Direction(Stick.LEFT, 0), duration=0.3, wait=0.1) 
            self.pressRep(Button.L, wait=0.3, repeat=3, duration=0.1, interval=0.1)
            self.press(Direction(Stick.LEFT, 90), duration=4.6, wait=0.5)
            self.press(Direction(Stick.LEFT, 157), duration=0.3, wait=0.1)
            self.pressRep(Button.L, wait=0.3, repeat=3, duration=0.1, interval=0.1)
            self.press(Direction(Stick.LEFT, 90), duration=3.0, wait=0.1)
            self.press(Direction(Stick.LEFT, 80), duration=2.0, wait=3.0)
            if not self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],use_gray=False):
                self.reset()
                continue
            else:
                break
        self.returnTofield(button=Button.A)
        #ネモのところへ
        self.press(Direction(Stick.LEFT, 90), duration=5.5, wait=0.1)
        self.press(Direction(Stick.LEFT, 25), duration=0.3, wait=0.1)
        self.pressRep(Button.L, wait=0.3, repeat=3, duration=0.1, interval=0.1)
        self.hold(Direction(Stick.LEFT, 90))
        while not self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],use_gray=False):
            self.wait(0.1)
        self.holdEnd(Direction(Stick.LEFT, 90))        
        #グルトンを倒す
        self.returnTofield(Button.A, 0.5, yasei=False)       
        #ピンを刺す
        self.returnTofield(button=Button.B)
        self.pressRep(Button.ZR, wait=0.1, repeat=3, duration=0.1, interval=0.1)
        self.setDestination('入り江のほら穴')
        self.GoStraight(False)
        self.press(Direction(Stick.LEFT, 100), duration=8.0, wait=0.1) 
        #会話発生
        while not self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],show_value=True):
            self.yasei()
            self.press(Direction(Stick.LEFT, 100), duration=3.0, wait=0.1)
        print("ネモと会話")       
        self.returnTofield(button=Button.A)
        self.press(Direction(Stick.LEFT, 90), duration=0.2, wait=0.1)
        self.pressRep(Button.L, wait=0.3, repeat=3, duration=0.1, interval=0.1)
        self.report()
        self.pressRep(Button.ZR, wait=0.1, repeat=3, duration=0.1, interval=0.1)
        print(f"かかった時間:{self.elapsed_time_str(time.time()-start)}", f"経過時間:{self.elapsed_time_str(time.time()-self.start_time)}\n")
    
    def irienohoraana(self):
        start = time.time()
        while True:
            start_time = time.time()
            flag = True
            self.press(Direction(Stick.LEFT, 90), duration=6.0, wait=0.1)
            print("ムービー中")
            self.renda(Button.A, 55)
            self.press(Direction(Stick.LEFT, 90), duration=6.0, wait=0.1)
            #サンドウィッチをあげる
            self.pressRep(Button.A, wait=0.8, repeat=2, duration=0.1, interval=0.5)
            while not self.isContainTemplate('SV/Auto_story/bag.png', 0.9):
                self.press(Button.B,0.1,1.0)
                if time.time() - start_time > 100:
                    flag = False
                    break
            if not flag:
                self.reset()
                continue
            self.wait(1.0)
            self.press(Direction.DOWN,0.1,0.5)
            self.press(Direction.DOWN,0.1,0.5)
            self.renda(Button.A, 68)
            #洞穴へ向かう        
            self.press(Direction(Stick.LEFT, 90), duration=8.0, wait=0.5)
            self.press(Direction(Stick.RIGHT, 0), duration=0.2, wait=0.5)
            self.hold(Direction(Stick.LEFT, 90))
            while not self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],use_gray=False):
                self.wait(0.1)
                if time.time() - start_time > 210:
                    flag = False
                    break
            self.holdEnd(Direction(Stick.LEFT, 90))
            if not flag:
                self.reset()
                continue
            start_time = time.time()
            self.renda(Button.A, 18)
            #会話終了後まっすぐ       
            self.press(Direction(Stick.LEFT, 90), duration=2.0, wait=0.5)
            self.press(Direction(Stick.LEFT, 35), duration=0.1, wait=0.5)
            self.pressRep(Button.L, wait=0.3, repeat=3, duration=0.1, interval=0.1)
            #岩を壊す
            self.press(Direction(Stick.LEFT, 90), duration=3.0, wait=6.0)
            self.press(Direction(Stick.LEFT, 80), duration=0.1, wait=0.5)
            self.pressRep(Button.L, wait=0.3, repeat=3, duration=0.1, interval=0.1)
            self.press(Direction(Stick.LEFT, 90), duration=5.0, wait=0.5)
            self.press(Direction(Stick.LEFT, 75), duration=0.1, wait=0.5)
            self.pressRep(Button.L, wait=0.3, repeat=3, duration=0.1, interval=0.1)
            self.press(Direction(Stick.LEFT, 90), duration=4.7, wait=0.5)
            self.press(Direction(Stick.LEFT, 53), duration=0.1, wait=0.5)
            self.pressRep(Button.L, wait=0.3, repeat=3, duration=0.1, interval=0.1)
            self.press(Direction(Stick.LEFT, 90), duration=13.5, wait=0.5)
            self.press(Direction(Stick.LEFT, 40), duration=0.1, wait=0.5)
            self.pressRep(Button.L, wait=0.3, repeat=3, duration=0.1, interval=0.1)
            #デルビルが出てくる
            self.press(Direction(Stick.LEFT, 90), duration=19.0, wait=0.1)
            self.wait(5.0)
            self.press(Direction(Stick.LEFT, 90), duration=2.8, wait=0.5)
            self.press(Direction(Stick.LEFT, 0), duration=0.1, wait=0.5)
            self.pressRep(Button.L, wait=0.3, repeat=3, duration=0.1, interval=0.1)
            #イベントが始まるまでまっすぐ       
            self.hold(Direction(Stick.LEFT, 90))
            while not self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],use_gray=False):
                self.yasei()
                if time.time() - start_time > 120:
                    self.holdEnd(Direction(Stick.LEFT, 90))
                    for i in range (2):
                        self.press(Direction(Stick.LEFT, 50), duration=2.0, wait=0.1)
                        self.press(Direction(Stick.LEFT, 130), duration=2.0, wait=0.1)
                    self.hold(Direction(Stick.LEFT, 90))
                    self.wait(1.0)
                    if not self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],use_gray=False):
                        flag = False
                        break
                    else:
                        break
                self.wait(0.1)
            self.holdEnd(Direction(Stick.LEFT, 90))
            if flag:
                break
            else:
                self.reset()
        self.returnTofield(Button.A, 0.1, yasei=False)
        print(f"かかった時間:{self.elapsed_time_str(time.time()-start)}", f"経過時間:{self.elapsed_time_str(time.time()-self.start_time)}\n")
    
    def todai(self):
        start = time.time()
        #ペパーのところへ
        print("ペパー戦へ")
        self.hold(Direction(Stick.LEFT, 90))
        while not self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],use_gray=False):
            self.yasei()
        self.holdEnd(Direction(Stick.LEFT, 90))      
        #self.press(Direction(Stick.LEFT, 90), duration=13.0, wait=0.1)
        self.returnTofield(Button.A, 0.1, yasei=False) 
        #レッツゴーで安全確認
        self.pressRep(Button.R, wait=2.0, repeat=2, duration=0.1, interval=0.1)       
        #灯台を登る
        self.press(Direction(Stick.LEFT, 90), duration=4.0, wait=0.1)
        self.press(Direction(Stick.LEFT, 0), duration=0.5, wait=0.1)
        self.press(Direction(Stick.LEFT, 90), duration=1.0, wait=2.0)
        self.returnTofield(wait=0.1, yasei=False)
        self.press(Direction(Stick.LEFT, 0), duration=3.0, wait=0.1)        
        self.pressRep(Button.A, wait=0.1, repeat=8, duration=0.1, interval=0.1)
        self.returnTofield(button=Button.A)        
        self.press(Direction(Stick.LEFT, 90), duration=1.0, wait=0.1)
        self.press(Direction(Stick.LEFT, 110), duration=1.0, wait=0.1)
        self.press(Direction(Stick.LEFT, 180), duration=1.0, wait=5.0)
        print(f"かかった時間:{self.elapsed_time_str(time.time()-start)}", f"経過時間:{self.elapsed_time_str(time.time()-self.start_time)}\n")
     
    def goToteburu_1(self):
        start = time.time()
        #ピンを刺す
        self.returnTofield(wait=0.15)
        self.pressRep(Button.R, wait=2.0, repeat=2, duration=0.1, interval=0.1) 
        self.press(Direction(Stick.LEFT, 90), duration=1.0, wait=0.1)
        self.setDestination('プラトタウン')
        self.pressRep(Button.ZR, wait=0.1, repeat=3, duration=0.1, interval=0.1)
        while not self.GoStraight(False, True, encount_time=0) == "kaiwa":
            self.press(Direction(Stick.LEFT, 200), duration=1.3, wait=0.1)
            self.press(Direction(Stick.LEFT, 90), duration=2.0, wait=5.0)
            if not self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],use_gray=False):
                self.fly('灯台')
                if not self.isContainTemplate('SV/Auto_story/flag.png',0.85):
                    self.setDestination('プラトタウン')
                else:
                    self.openMap()
                    self.returnTofield(button=Button.B)
                    self.pressRep(Button.ZR, wait=0.1, repeat=3, duration=0.1, interval=0.1)
            else:
                break
        #ネモと会話
        self.returnTofield(button=Button.A, wait=0.5) 
        print(f"かかった時間:{self.elapsed_time_str(time.time()-start)}", f"経過時間:{self.elapsed_time_str(time.time()-self.start_time)}\n")
    
    def goToteburu_2(self):
        start = time.time()      
        """self.pressRep(Button.B, wait=0.1, repeat=10, duration=0.1, interval=0.1)
        self.pressRep(Button.ZR, wait=0.1, repeat=3, duration=0.1, interval=0.1)
        #少し横へ              
        self.pressRep(Button.L, wait=0.5, repeat=3, duration=0.1, interval=0.1)
        self.press(Direction(Stick.LEFT, 250), duration=0.3, wait=0.1)
        self.pressRep(Button.L, wait=0.5, repeat=3, duration=0.1, interval=0.1)
        self.press(Direction(Stick.LEFT, 90), duration=2.5, wait=0.1)"""
        self.fly('プラトタウン')
        self.openMenu()
        self.returnTofield(Button.B)
        self.pressRep(Button.ZR, wait=0.1, repeat=3, duration=0.1, interval=0.1)
        self.pressRep(Button.L, wait=0.5, repeat=3, duration=0.1, interval=0.1)
        self.press(Direction(Stick.LEFT, 0), duration=0.1, wait=0.5)        
        self.pressRep(Button.L, wait=0.5, repeat=3, duration=0.1, interval=0.1)
        self.press(Direction(Stick.LEFT, 90), duration=2.6, wait=0.5)
        self.press(Direction(Stick.LEFT, 0), duration=0.1, wait=0.5)        
        self.pressRep(Button.L, wait=0.5, repeat=3, duration=0.1, interval=0.1)   
        #ピンを刺す     
        self.setDestination('テーブルシティ道中_1')
        self.pressRep(Button.ZR, wait=0.1, repeat=3, duration=0.1, interval=0.1)
        self.GoStraight(False, encount_time=0)
        self.setDestination('テーブルシティ道中_2')
        self.pressRep(Button.ZR, wait=0.1, repeat=3, duration=0.1, interval=0.1)
        self.GoStraight(False, encount_time=0)
        self.press(Direction(Stick.LEFT, 90), duration=3.0, wait=0.1)
        self.press(Direction(Stick.LEFT, 20), duration=0.3, wait=0.1)
        self.pressRep(Button.L, wait=0.5, repeat=3, duration=0.1, interval=0.1)
        self.pressRep(Button.R, wait=2.0, repeat=2, duration=0.1, interval=0.1)
        #会話が始まるまで横へ
        self.hold(Direction(Stick.LEFT, 90))
        while not self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],use_gray=False):
            self.yasei()
            self.wait(0.1)
        self.holdEnd(Direction(Stick.LEFT, 90))
        #ネモ戦
        self.returnTofield(Button.A ,0.1, yasei=False)
        print(f"かかった時間:{self.elapsed_time_str(time.time()-start)}", f"経過時間:{self.elapsed_time_str(time.time()-self.start_time)}\n")

    def teburucity(self):
        start = time.time()       
        self.press(Direction(Stick.LEFT, 180), duration=0.3, wait=0.1)
        self.openMap()
        self.press(Direction(Stick.LEFT, 90), duration=1, wait=0.1)
        self.pressRep(Button.A, wait=0.5, repeat=2, duration=0.1, interval=0.8)
        self.pressRep(Button.B, wait=1.5, repeat=2, duration=0.1, interval=0.1)
        self.pressRep(Button.ZR, wait=0.1, repeat=3, duration=0.1, interval=0.1)
        self.GoStraight(False, True)
        #下っ端とバトル  
        self.returnTofield(Button.A, 0.1, yasei=False)        
        #学校へ
        #self.press(Direction(Stick.LEFT, 0), duration=0.2, wait=0.1)
        self.GoStraight(kabe_flag=False, kaiwa_flag=True)
        self.returnTofield(button=Button.A)    
        #居室を出る
        self.press(Direction(Stick.LEFT, 0), duration=0.8, wait=0.1)
        self.press(Direction(Stick.LEFT, 270), duration=1.8, wait=0.1)
        self.returnTofield(button=Button.A)       
        #ペパーに話しかける
        self.press(Direction(Stick.LEFT, 90), duration=2.0, wait=0.1)
        self.press(Direction(Stick.LEFT, 180), duration=0.2, wait=0.1)
        self.pressRep(Button.A, wait=0.1, repeat=5, duration=0.1, interval=0.1)
        self.returnTofield(button=Button.A)
        #カシオペアと電話
        self.press(Direction(Stick.LEFT, 270), duration=2.0, wait=0.1)
        self.returnTofield(button=Button.A)        
        self.press(Direction(Stick.LEFT, 90), duration=3.5, wait=0.1)
        self.press(Direction(Stick.LEFT, 0), duration=0.8, wait=0.1)       
        #機械に話しかける
        self.pressRep(Button.A, wait=1.9, repeat=2, duration=0.1, interval=0.1)
        self.press(Direction.DOWN,0.1,0.5)
        self.renda(Button.A, 100)
        self.returnTofield(button=Button.B)
        #校長室へ
        self.press(Direction(Stick.LEFT, 230), duration=4.5, wait=0.1)      
        self.returnTofield(button=Button.A, wait=0.4)
        self.pressRep(Button.B, wait=0.1, repeat=10, duration=0.1, interval=0.1)
        self.press(Direction(Stick.LEFT, 290), duration=3.5, wait=0.1)
        self.press(Direction(Stick.LEFT, 270), duration=2.0, wait=0.1)      
        #ベッドへ
        self.returnTofield(button=Button.A)
        self.press(Direction(Stick.LEFT, 90), duration=1.0, wait=0.1)
        self.press(Direction(Stick.LEFT, 180), duration=1.0, wait=0.1)
        self.pressRep(Button.A, wait=0.1, repeat=6, duration=0.1, interval=0.1)
        self.returnTofield(button=Button.A)        
        #部屋から出る
        self.press(Direction(Stick.LEFT, 0), duration=3.0, wait=0.1)
        self.returnTofield(button=Button.A)
        #階段へ
        self.hold(Direction(Stick.LEFT, 90))
        while not self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],use_gray=False):
            self.wait(0.1)
        self.holdEnd(Direction(Stick.LEFT, 90))
        while not self.isContainTemplate('SV/Auto_story/plus.png', 0.92,use_gray=False):
            self.press(Button.A,0.1,0.1)
        self.press(Button.PLUS,0.1,0.1)
        self.returnTofield(button=Button.A)
        print(f"かかった時間:{self.elapsed_time_str(time.time()-start)}", f"経過時間:{self.elapsed_time_str(time.time()-self.start_time)}\n")

    def goToTaikunonushi(self):
        start = time.time()
        print("セルクルシティへ")
        while True:
            flag = True
            self.fly('テーブルシティ西')
            self.raidonCheck()
            self.setDestination('テーブルシティ_1')
            self.GoStraight()
            self.press(Direction(Stick.LEFT, 350), duration=1.0, wait=0.1)
            self.setDestination('テーブルシティ_2')
            start_time = time.time()
            if not self.GoStraight(kaiwa_flag=True) == "denwa":
                self.hold(Direction(Stick.LEFT, 90))
                while not self.isContainTemplate('SV/Auto_story/call.png',0.9,crop=[835,582,1000,670]):
                    self.wait(0.1)
                    if time.time() - start_time > 20:
                        flag = False
                        break
                self.holdEnd(Direction(Stick.LEFT, 90))
                if flag:
                    break
            else:
                break
        self.returnTofield(Button.A)
        self.press(Direction(Stick.LEFT, 90), duration=6.0, wait=0.1)
        self.report()
        while True:
            self.raidonCheck()
            self.setDestination('セルクルタウン道中_1')
            self.GoStraight()
            self.setDestination('セルクルタウン東')
            self.GoStraight()
            if self.fly('セルクルタウン西', repeat=5) is False:
                self.reset()
                continue
            else:
                break
        print("大空のヌシのところへ")
        self.raidonCheck()       
        self.setDestination('大空のヌシ道中_1')
        self.GoStraight()
        self.setDestination('大空のヌシ道中_2')
        self.GoStraight()
        self.setDestination('大空のヌシ道中_3')
        self.GoStraight()           
        self.setDestination('大空のヌシ道中_4')
        self.GoStraight()
        self.report()                    
        while True:
            self.raidonCheck()
            self.setDestination('大空のヌシ道中_5')    
            self.GoStraight()
            self.setDestination('大空のヌシ道中_6')
            if self.GoStraight(under_water_max=3)  == "water":
                self.reset()                  
                continue
            else:
                break
        self.report()
        while True:
            self.raidonCheck(check=True)
            self.setDestination('大空のヌシ道中_7')    
            self.GoStraight()
            #ポケセンで位置リセット
            if self.fly('大空のヌシ道中_7', repeat=5) is False:
                self.reset()
                continue
            else:
                break
        self.raidonCheck()
        self.press(Direction(Stick.LEFT, 160), duration=2.0, wait=0.1)
        self.setDestination('大空のヌシ道中_8')    
        self.GoStraight()
        self.setDestination('大空のヌシ道中_9')    
        self.GoStraight(kaiwa_flag=True)
        self.report()
        while True:
            self.raidonCheck()
            self.setDestination('大空のヌシ道中_10')        
            self.GoStraight()
            self.setDestination('大空のヌシ道中_11')
            if self.GoStraight(time_limit=120) == "timeover":
                self.reset()
                continue
            self.setDestination('大空のヌシ道中_12')
            if self.GoStraight(kaiwa_flag=True, nushi_battle=True, time_limit=90) == "timeover":
                self.reset()
                continue
            break
        #ヌシバトル
        print("大空のヌシとバトル")
        self.returnTofield(Button.A, 0.1, yasei=False)
        print("大空のヌシ撃破")
        print(f"かかった時間:{self.elapsed_time_str(time.time()-start)}", f"経過時間:{self.elapsed_time_str(time.time()-self.start_time)}\n")
        
    def goToDoshinnonushi(self):
        start = time.time()
        self.report()
        print("土震のヌシのところへ")       
        self.raidonCheck()
        self.setDestination("土震のヌシ道中_1")
        self.GoStraight()           
        self.setDestination("土震のヌシ道中_2",event_flag=True)
        self.GoStraight(kaiwa_flag=True)
        self.report()
        flag = False
        while not flag:
            self.raidonCheck()         
            if self.GoStraight(kaiwa_flag=True,) == "kaiwa":
                break
            #self.press(Direction(Stick.LEFT, 90), duration=6.0, wait=0.1)
            self.press(Direction(Stick.LEFT, 110), duration=0.3, wait=0.3)
            self.pressRep(Button.L, wait=0.1, repeat=3, duration=0.1, interval=0.1)
            self.press(Direction.UP, 5.4, 0.5)          
            self.hold(Direction(Stick.LEFT, 90))
            self.hold(Direction(Stick.RIGHT, 180))
            start_1 = time.time()
            while True:
                if (time.time() - start_1) > 60:
                    print("ヌシとエンカウントできなかったのでリセット")
                    self.holdEnd(Direction(Stick.LEFT, 90))
                    self.holdEnd(Direction(Stick.RIGHT, 180))
                    self.reset()
                    break
                if self.isContainTemplate('SV/Auto_story/call.png',0.9):
                    flag = True               
                    self.holdEnd(Direction(Stick.LEFT, 90))
                    self.holdEnd(Direction(Stick.RIGHT, 180))
                    break
        print("ヌシとエンカウント成功")
        self.returnTofield(Button.A, 0.1, yasei=False)          
        self.raidonCheck()
        self.setDestination("土震のヌシ道中_3",event_flag=True)
        self.GoStraight(kaiwa_flag=True)
        print("ペパーと共闘")
        self.returnTofield(Button.A, 0.1, yasei=False)
        print("土震のヌシ撃破")
        print(f"かかった時間:{self.elapsed_time_str(time.time()-start)}", f"経過時間:{self.elapsed_time_str(time.time()-self.start_time)}\n")
    
    def goToGIryunonushi(self):
        start = time.time()
        self.report()
        print("偽竜のヌシのところへ")
        while True:
            self.raidonCheck()
            self.setDestination("偽竜のヌシ道中_1")
            self.GoStraight()
            self.setDestination("偽竜のヌシ道中_2")
            self.GoStraight()
            self.setDestination('マリナードタウン')
            self.GoStraight()
            if self.fly('マリナードタウン', repeat=5) is False:
                self.reset()
                continue
            else:
                break
        #技の一番目と二番目を入れ替える 1:アクロバット, 2:アクアブレイク       
        self.wazaIrekae(1, 2)
        self.raidonCheck()
        self.setDestination('偽竜のヌシ道中_3')
        self.GoStraight()
        self.setDestination('偽竜のヌシ道中_4')
        self.GoStraight(kabe_flag=False)
        self.setDestination('偽竜のヌシ道中_5')
        self.GoStraight(kabe_flag=False, kaiwa_flag=True, mawarikomu=False) #encount_time=15      
        self.GoStraight(kabe_flag=False, mawarikomu=False) #encount_time=15
        self.setDestination('偽竜のヌシ道中_6', event_flag=True)
        self.report()  
        while True:        
            if self.GoStraight(kabe_flag=False, mawarikomu=False, time_limit=180) == "timeover":#encount_time=15
                self.reset()
                self.openMap()
                self.returnTofield(button=Button.B,wait=0.5)
                continue
            self.setDestination('偽竜のヌシ道中_7')
            self.GoStraight()    
            #ヌシを探す
            self.pressRep(Button.L, wait=0.5, repeat=3, duration=0.1, interval=0.1)
            #しゃがむ
            self.raidonCheck(False)
            self.press(Button.B,0.1,0.5)
            count = 0
            while count < 10:
                if self.sushi_check() > 0.9:
                    break
                else:
                    count += 1
                    self.press(Direction.UP, 0.2, 0.5)
            if count >= 10:
                self.reset()
                self.openMap()
                self.returnTofield(button=Button.B,wait=0.5)
                continue
            print("スシを発見")
            if self.sushi_battle():
                break
            else:
                self.reset()
                self.openMap()
                self.returnTofield(button=Button.B,wait=0.5)
                continue
        print("ヌシとバトル")
        self.returnTofield(Button.A, 0.1, yasei=False)        
        self.raidonCheck()
        self.setDestination('偽竜のヌシ道中_8')
        self.GoStraight(kabe_flag=False, mawarikomu=False)#encount_time=11
        self.setDestination('偽竜のヌシ道中_9', event_flag=True)
        if not self.GoStraight(kabe_flag=False, kaiwa_flag=True, mawarikomu=False) == "kaiwa":
            self.hold(Direction(Stick.LEFT, 90))
            while not self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],use_gray=False):
                self.wait(0.1)
                self.yasei(False)
            self.holdEnd(Direction(Stick.LEFT, 90))
        print("ペパーと共闘")
        self.returnTofield(Button.A, 0.1, yasei=False)
        print("偽竜のヌシ撃破")
        print(f"かかった時間:{self.elapsed_time_str(time.time()-start)}", f"経過時間:{self.elapsed_time_str(time.time()-self.start_time)}\n")

    def sushi_check(self):
        src = self.camera.readFrame()
        src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        ret, src_1 = cv2.threshold(src, 220, 255, cv2.THRESH_BINARY)
        cv2.imwrite('./Template/SV/Auto_story/test_screen.png', src_1)
        template = cv2.imread('./Template/SV/Auto_story/nushinushi.png', cv2.IMREAD_GRAYSCALE)
        ret, template_1 = cv2.threshold(template, 220, 255, cv2.THRESH_BINARY)
        res = cv2.matchTemplate(src_1, template_1, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, self.max_loc = cv2.minMaxLoc(res)
        print("ヌシチェック", max_val)
        return max_val
    
    def sushi_battle(self):
        while True:
            print(self.max_loc)
            x, y = self.max_loc
            x, y = x + 67, y + 21
            print(f'({x}, {y})')
            (638, 691) #主人公の位置
            if not (638 - x) == 0:
                rad = math.atan((691 - y)/(638 - x))
                deg = math.degrees(rad)
                if x >= 638:
                    deg = - deg
                else:
                    deg = 180-deg
            else:
                if (691 - y) >= 0:
                    deg = 90
                else:
                    deg = -90   
            print(deg)
            self.press(Direction(Stick.LEFT, deg),duration=0.2, wait=0.5)
            self.pressRep(Button.L, wait=0.5, repeat=3, duration=0.1, interval=0.1)
            self.pressRep(Button.A, wait=0.5, repeat=3, duration=0.1, interval=0.1)
            if self.sushi_check() < 0.9:            
                break
            else:
                continue
        start = time.time()
        while not self.isContainTemplate('SV/Auto_story/battle.png', 0.8):
            self.press(Button.B,0.1,0.1)
            if time.time() - start > 20:
                print("ヌシを見つけられませんでした")
                return False
        if self.isContainTemplate('SV/Auto_story/nushi_encount.png', 0.86, use_gray=False, crop=[440,10,832,113]):
            print("ヌシとエンカウントしました")
            return True
        else:
            print("スシとエンカウントしました")
            return False
    
    def pinAndmove(self,deg, duration, duration_move):
        self.openMap()
        self.press(Direction(Stick.LEFT, deg), duration=duration, wait=0.1)
        self.pressRep(Button.A, wait=0.5, repeat=2, duration=0.1, interval=0.8)
        self.pressRep(Button.B, wait=1.5, repeat=2, duration=0.1, interval=0.1)
        self.press(Direction(Stick.LEFT, 90), duration=duration_move, wait=0.1)

    def renda(self,button, x):
        y = time.time()
        while x > (time.time() - y):
            self.press(button, 0.05, 0.03)
    
    def report(self):
        print("\nセーブします")
        self.openMenu()           
        self.pressRep(Button.R, wait=1.0, repeat=3, duration=0.1, interval=0.1)
        self.pressRep(Button.A, wait=0.1, repeat=5, duration=0.1, interval=0.1)
        self.returnTofield(button=Button.B)
    
    def reset(self):
        #ソフトリセット
        print("\nリセットします")
        while not (self.chkReturnHome()):
            self.press(Button.HOME,0.05,1.5)
        self.pressRep(Button.X, wait=0.1, repeat=3, duration=0.1, interval=0.1)
        self.returnTofield(button=Button.A,wait=0.1)

    def fieldCheck(self):
        img = 'SV/Auto_story/maru.png' if self.maru_mode != 1 else (self.marufile + ".png")
        if self.maru_mode == 2:
            threshold = self.initmaruTh
            show_value = True
        else:
            threshold = 0.82
            show_value = False

        ret = self.isContainTemplate(img, threshold,
                                     crop=[1135,570,1185,625], show_value=show_value)

        if ret and self.maru_mode == 2:
            savefile = os.path.join(os.getcwd(), "Template", self.marufile)
            self.camera.saveCapture(filename=savefile, crop=1,
                                    crop_ax=[1153, 594, 1167, 607])
            threshold = 0.82
            show_value = True
            _ = self.isContainTemplate(self.marufile + ".png", threshold,
                                       crop=[1135,570,1185,625], show_value=show_value)
            self.maru_mode = 1
        return ret

    def returnTofield(self, button=False, wait=0.2, yasei=True):
        if yasei:
            while not self.fieldCheck():
                if button:
                    self.press(button,0.1,wait)
                else:
                    self.wait(wait)
                self.yasei()
        else:
            while not self.fieldCheck():
                if button:
                    self.press(button,0.1,wait)
                else:
                    self.wait(wait)
    
    def openMenu(self, wait=0.7):
        self.returnTofield(button=Button.B,wait=0.5)
        while not self.isContainTemplate('SV/Auto_story/menu.png', 0.8, crop=[1120,660,1280,720],show_value=False):
            self.press(Button.X,0.1,wait)
            self.yasei()
        self.press(Direction.RIGHT,0.6,0.1)

    def openMap(self):
        count = 0
        while True:
            if self.fieldCheck():#1040,480,1280,720
                self.press(Button.Y,0.05,0.1)
            if self.isContainTemplate('SV/Auto_story/openMap.png', 0.8):
                break
            count += 1
            if count % 50 == 0:
                print("マップが開けません")
                self.hold(Direction(Stick.LEFT, -90))
                self.pressRep(Button.B, wait=0.1, repeat=6, duration=0.05, interval=0.2)
                self.holdEnd(Direction(Stick.LEFT, -90))
            self.yasei()
        self.wait(0.3)
    
    def openBox(self):
        flag = False
        while True:
            self.openMenu()
            while not self.isContainTemplate('SV/Auto_story/selectBox.png', 0.9):
                self.press(Direction.DOWN,0.05,0.5)
            self.press(Button.A,0.05,1.7)
            start = time.time()
            while not self.isContainTemplate('SV/Auto_story/openBox.png', 0.8):
                self.wait(0.1)
                if time.time()-start > 10:
                    print(time.time()-start)
                    flag = True
                    break
            if flag:
                flag = False
                continue
            break
        self.wait(0.8)
    
    def raidonCheck(self, ride=True, check=False):
        flag = None  #0で降りている状態、1でライド状態
        while True:
            self.openMenu()
            if not self.isContainTemplate('SV/Auto_story/' + self.language+'/oriru.png', 0.86,use_gray=False):
                print("ライドしていません")
                if ride:
                    self.press(Button.PLUS,0.1,0.1)
                    flag = 1
                else:
                    self.press(Button.B,0.1,1.8)
                    flag = 0
            else:
                print("ライドしています")
                if ride:
                    flag = 1
                else:
                    self.press(Button.PLUS,0.1,1.8)
                    flag = 0
            if check:
                self.openMenu()
                if not self.isContainTemplate('SV/Auto_story/' + self.language+'/oriru.png', 0.86,use_gray=False):
                    print("ライドできませんでした")
                    self.returnTofield(button=Button.B, wait=0.7)
                    self.press(Direction.DOWN,0.5,0.5)
                    continue
                else:
                    break
            else:
                break
        self.returnTofield(button=Button.B, wait=0.7)
        return flag
    
    def wazaIrekae(self,x=1, y=1):
        print("技の入れ替え", x, "⇔", y)
        while not self.isContainTemplate('SV/Auto_story/waza_irekae.png', 0.85):
            self.openMenu()
            self.press(Direction.LEFT,0.5,0.5)
            self.pressRep(Button.A, wait=0.8, repeat=2, duration=0.1, interval=0.5)
            self.press(Direction.RIGHT,0.1,0.5)
        self.press(Button.Y,0.1,0.5)
        self.press(Button.A,0.1,0.5)  
        self.pressRep(Direction.DOWN, wait=0.1, repeat=abs(x-y), duration=0.1, interval=0.1)
        self.press(Button.A,0.1,0.1)
        self.returnTofield(button=Button.B)
    
    def temochiCheck(self):
        self.openBox()
        if self.isContainTemplate('SV/Auto_story/temochiBlank.png', 0.89,crop=[8,126,290,658]):
            return 1
        if self.isContainTemplate('SV/Auto_story/temochiBlank1.png', 0.89,crop=[8,126,290,658]):
            return 2
        if self.isContainTemplate('SV/Auto_story/temochiBlank2.png', 0.89,crop=[8,126,290,658]):
            return 3
        if self.isContainTemplate('SV/Auto_story/temochiBlank3.png', 0.89,crop=[8,126,290,658]):
            return 4
        if self.isContainTemplate('SV/Auto_story/temochiBlank4.png', 0.89,crop=[8,126,290,658]):
            return 5
        else:
            return 6
    
    def temochiIrekae(self,x=1):
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
                self.press(Direction.UP, 0.1, 0.5)
                self.press(Button.A,0.1,0.5)
                continue

    def danrush(self, time_limit=100):
        print("団ラッシュ")
        t = time.time()
        start = time.time()
        i = 0
        j = 0
        self.pressRep(Button.L, wait=0.5, repeat=3, duration=0.1, interval=0.1)
        self.hold(Direction(Stick.LEFT, 90))
        src = self.camera.readFrame()
        src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        while (t - start) < time_limit:
            self.pressRep(Button.R, wait=1.0, repeat=5, duration=0.1, interval=0.5)
            #while count == 0 and (t - start) < time_limit:
            src_1 = self.camera.readFrame()
            src_1 = cv2.cvtColor(src_1, cv2.COLOR_BGR2GRAY)
            src_1 = src_1[554: 668, 1086: 1224]#1086, 554 1224, 668
            res = cv2.matchTemplate(src, src_1, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(res)
            if max_val > 0.92:
                print(str(round(max_val, 3)))
                self.holdEnd(Direction(Stick.LEFT, 90))
                self.press(Direction(Stick.LEFT, j), duration=0.1, wait=0.5)
                self.pressRep(Button.L, wait=0.5, repeat=3, duration=0.1, interval=0.1)
                self.press(Direction.UP, 1.5, 0.5)
                self.hold(Direction(Stick.LEFT, 90))
                i += 1
                if i % 3 == 0:
                    j += 180               
            src = self.camera.readFrame()
            src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            if self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],use_gray=False):
                self.holdEnd(Direction(Stick.LEFT, 90))
                print("会話発生")
                return True
            t = time.time()
        self.holdEnd(Direction(Stick.LEFT, 90))
        print("時間切れです")
        return False
    
    def battle_irekae(self):
        while not self.fieldCheck():
            self.press(Button.A,0.1,0.1)
            if self.isContainTemplate('SV/Auto_story/pokemon_irekae.png', 0.85):
                print("ポケモン入れ替え画面")
                self.pressRep(Button.B, wait=0.5, repeat=10, duration=0.1, interval=0.1)

    def battle(self, kaiwa_flag=True):
        print("戦闘開始")
        i = 0
        while True:
            if self.isContainTemplate('SV/Auto_story/battle.png', 0.8):
                self.pressRep(Button.A, wait=0.1, repeat=8, duration=0.05, interval=0.1)
                self.pressRep(Button.B, wait=1.0, repeat=30, duration=0.1, interval=0.1)
                if self.isContainTemplate('SV/Auto_story/battle.png', 0.8):
                    i += 1
                    print("技が使えない？")
                    self.pressRep(Button.A, wait=0.8, repeat=1, duration=0.05, interval=0.1)
                    self.pressRep(Direction.DOWN, wait=0.6, repeat=i, duration=0.05, interval=0.3)
                    self.pressRep(Button.A, wait=0.1, repeat=8, duration=0.05, interval=0.1)
                    self.pressRep(Button.B, wait=2.0, repeat=20, duration=0.1, interval=0.1)
            if kaiwa_flag:
                if self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],use_gray=False)\
                or self.isContainTemplate('SV/Auto_story/messagewindow_1.png', 0.9,crop=[270,470,370,600],use_gray=False):
                    print("会話発生")
                    return "kaiwa"
            if self.fieldCheck():
                print("戦闘終了")
                break
            else:
                self.press(Button.B,0.1,0.1)           
    
    def yasei(self, a=True, nushi_battle=False, encount_time=2.5):
        if self.isContainTemplate('SV/Auto_story/battle.png', 0.8):
            print("野生エンカウント")
            if a == False:
                self.holdEnd(Direction(Stick.LEFT, 90))
            if nushi_battle:
                if self.isContainTemplate('SV/Auto_story/nushi_encount.png', 0.86, use_gray=False, crop=[440,10,832,113]):
                    print("ヌシと遭遇")
                    self.press(Direction.UP, 1.0, 0.5) 
                    return "nushi"
            if self.encount_timer_end - self.encount_timer_start < encount_time :
                self.yasei_count += 1
                print("*")
                if self.yasei_count >= 2:
                    print("敵を攻撃")              
                    self.press(Direction.UP, 1.0, 0.5)
                    self.press(Button.A,0.1,0.5)
            else:
                self.yasei_count = 0
            self.press(Direction.DOWN, 1.0, 0.5)
            self.pressRep(Button.A, wait=0.1, repeat=8, duration=0.05, interval=0.1)
            self.pressRep(Button.B, wait=2.7, repeat=5, duration=0.05, interval=0.1)
            if self.yasei_count >= 2:
                self.wait(4.8) #技使用分
            i = 0
            while True:
                if self.isContainTemplate('SV/Auto_story/battle.png', 0.8):
                    print("逃げられない？")
                    #self.yasei_count += 1
                    print("敵を攻撃")
                    self.press(Direction.UP, 1.0, 0.5)
                    self.press(Button.A,0.1,0.5)
                    self.press(Direction.DOWN, 0.8, 0.3)
                    self.pressRep(Direction.DOWN, wait=0.1, repeat=i, duration=0.05, interval=0.1)
                    self.pressRep(Button.A, wait=0.1, repeat=8, duration=0.05, interval=0.1)
                    self.pressRep(Button.B, wait=2.0, repeat=5, duration=0.05, interval=0.1)
                    i += 1
                else:
                    break
            self.encount_timer_start = time.time()
            if a == False:
                self.hold(Direction(Stick.LEFT, 90))
            return True

    def setDestination(self,name, event_flag=False, repeat_flag=True):
        count = 0
        while True:
            count += 1
            print(name, "にピンを刺す")
            self.openMap()
            self.move(name, event_flag, change_day=True)
            self.press(Button.A,0.1,0.7)
            self.pressRep(Direction.UP, wait=0.5, repeat=2, duration=0.1, interval=0.3)
            self.press(Button.A,0.1,0.5)
            self.returnTofield(button=Button.B,wait=0.5)
            if not self.isContainTemplate('SV/Auto_story/flag.png', 0.8):
                if repeat_flag:
                    continue
                else:
                    break
            else:
                break
    
    def fly(self,name, repeat=999, event_flag=False):
        print(name, "へ空を飛ぶ")
        i = 0
        count = 1
        while True:
            flag = False
            self.returnTofield(button=Button.B,wait=0.5)
            if count > repeat:
                print("目的地まで飛べませんでした")
                return False
            count += 1
            self.openMap()
            self.move(name, event_flag)
            if i > 0:
                self.press(Direction(Stick.LEFT, -90*i),duration=0.08, wait=0.12)
            self.press(Button.ZL,0.05,0.6)
            i += 1
            for j in range (0, 5):
                self.press(Button.A,0.05,0.6)
                if self.isContainTemplate('SV/Auto_story/fly.png', 0.9, use_gray=False, show_value=False, crop=[634,360,1080,586]):
                    if self.isContainTemplate('SV/Auto_story/eventflag.png',0.87):
                        flag = True
                        break
                    else:
                        self.pressRep(Button.A, wait=0.1, repeat=10, duration=0.05, interval=0.1)
                        break
                if self.isContainTemplate('SV/Auto_story/pin.png', 0.9, use_gray=False, show_value=False, crop=[634,360,1080,586]):
                    flag = True
                    break
            else:
                continue
            if flag:
                continue         
            break
        self.returnTofield(wait=0.1)
        self.wait(0.5)
    
    def elapsed_time_str(self,seconds, flag=True):
        seconds = int(seconds + 0.5)    
        h = seconds // 3600            
        m = (seconds - h * 3600) // 60  
        s = seconds - h * 3600 - m * 60
        if flag: 
            return f"{h}時間{m}分{s}秒"
        else:
            return f"{m}分{s}秒"
 
    def GoStraight(self, kabe_flag=True, kaiwa_flag=False, mawarikomu=True, under_water_max=999, nushi_battle=False, kabe=False, time_limit=False, encount_time=2.5):
        d = 5
        count = 1
        under_water = 1
        self.pressRep(Button.L, wait=0.5, repeat=3, duration=0.1, interval=0.1)
        self.hold(Direction(Stick.LEFT, 90))
        t = time.time()
        start_1 = time.time()
        src = self.camera.readFrame()
        src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        while True:
            result, x_pos, _ = self.getCoordinate("SV/Auto_story/flag.png", range_x=16, range_y=9)
            if result:
                if (1162 + d) < x_pos:#1162
                    self.press(Direction(Stick.RIGHT, 0),duration=0.06, wait=0.2)
                elif (1162 - d) > x_pos:
                    self.press(Direction(Stick.RIGHT, 180),duration=0.06, wait=0.2)
            if not self.isContainTemplate('SV/Auto_story/flag.png',0.8,crop=[1024,450,1280,720]):
                self.encount_timer_end = time.time()
                self.wait(self.move_time)
                self.holdEnd(Direction(Stick.LEFT, 90))
                while True:
                    if nushi_battle:
                        result = self.yasei(nushi_battle=nushi_battle, encount_time=encount_time)
                        if result == "nushi":
                            return "nushi"
                        if result == True:
                            t = time.time()
                            break
                    else:
                        if self.yasei(encount_time=encount_time):
                            t = time.time()
                            break
                    if not self.fieldCheck():
                        if self.isContainTemplate('SV/Auto_story/blackout.png',0.92):
                            print("水の中？")
                            under_water += 1
                            self.returnTofield(button=Button.A)
                            if under_water > under_water_max:
                                print("橋の前")
                                return "water"
                            self.openMap()
                            self.pressRep(Button.B, wait=1.0, repeat=1, duration=0.1, interval=0.1)
                            self.pressRep(Button.L, wait=0.5, repeat=3, duration=0.1, interval=0.1)
                            self.press(Direction(Stick.LEFT, 330),duration=1.0, wait=0.2)
                            self.returnTofield(button=Button.B)
                        if kaiwa_flag:
                            if self.isContainTemplate('SV/Auto_story/messagewindow.png', 0.9,crop=[270,480,370,570],use_gray=False)\
                            or self.isContainTemplate('SV/Auto_story/messagewindow_1.png', 0.9,crop=[270,470,370,600],use_gray=False):
                                print("会話発生")
                                return "kaiwa"
                            if self.isContainTemplate('SV/Auto_story/call.png',0.9,crop=[835,582,1000,670]):
                                print("電話")
                                self.returnTofield(button=Button.A)
                                return "denwa"
                        if self.isContainTemplate('SV/Auto_story/yasei_terastal.png',0.9):
                            print("テラスタルポケモンと遭遇")
                            self.press(Button.A,0.1,1.2)
                        continue             
                    else:
                        if self.isContainTemplate('SV/Auto_story/flag.png',0.8,crop=[1024,450,1280,720]):
                            break
                        else:
                            i = 0
                            while i < 2:
                                if self.fieldCheck() and (not self.isContainTemplate('SV/Auto_story/flag.png',0.8,crop=[1024,450,1280,720])):
                                    i += 1
                                else:
                                    break
                            if i == 2:
                                return
                            else:
                                break
                self.hold(Direction(Stick.LEFT, 90))        
            if time.time() - t > 5:
                src_1 = self.camera.readFrame()
                src_1 = cv2.cvtColor(src_1, cv2.COLOR_BGR2GRAY)
                src_1 = src_1[554: 668, 1086: 1224]#480: 720, 1040: 1280
                res = cv2.matchTemplate(src, src_1, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, _ = cv2.minMaxLoc(res)
                #print(str(round(max_val, 3)))
                if max_val > 0.92:
                    if kabe_flag:
                        print("壁をジャンプ")
                        self.holdEnd(Direction(Stick.LEFT, 90))
                        if kabe:
                            return "kabe"
                        self.wait(1.5)
                        self.hold(Direction(Stick.LEFT, 90))
                        self.press(Button.B,0.6,0.5)#0.3
                else:
                    count = 1
                t = time.time()
                count += 1
                src = self.camera.readFrame()
                src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            if mawarikomu:
                if count % 5 == 0:
                    print("詰まっているので位置修正")
                    self.holdEnd(Direction(Stick.LEFT, 90))
                    self.press(Direction(Stick.LEFT, 315),duration=2.0, wait=0.2)
                    self.openMap()
                    self.pressRep(Button.B, wait=1.0, repeat=1, duration=0.1, interval=0.1)
                    self.pressRep(Button.L, wait=0.5, repeat=3, duration=0.1, interval=0.1)
                    self.hold(Direction(Stick.LEFT, 90))
                    count = 1
            if time_limit is not False:
                if time.time() - start_1 > time_limit:
                    self.holdEnd(Direction(Stick.LEFT, 90))
                    print("時間内に到着しませんでした")
                    return "timeover"
    
    def changeDay(self):
        print("日付変更")
        while not (self.chkReturnHome()):
            self.press(Button.HOME,0.05,1.5)
        self.press(Direction.LEFT, 0.05, 0.3)
        self.press(Direction.DOWN, 0.05, 0.3)
        self.press(Direction.LEFT, 0.05, 0.3)
        self.press(Button.A, 0.05, 1.2)
        self.press(Direction.DOWN, 2.0, 0.3)
        self.press(Button.A, 0.05, 0.8)
        self.pressRep(Direction.DOWN, wait=0.5, repeat=3, duration=0.1, interval=0.3)
        self.press(Direction.DOWN, 0.2, 0.5)
        self.pressRep(Direction.DOWN, wait=0.3, repeat=2, duration=0.1, interval=0.3)
        self.press(Button.A, 0.05, 0.8)
        self.press(Direction.DOWN, 0.8, 0.8)
        self.press(Button.A, 0.05, 0.8)
        self.press(Direction.RIGHT, 1.2, 0.3)
        self.press(Button.A, 0.05, 0.8)
        self.returnTofield(Button.HOME, 2.0)
    
    def move(self, name, event_flag=False, change_day=False):
        d = 10
        count = 0
        x, y = self.getLocation(name)
        while True:
            if self.map == 0:
                _, x_pos, y_pos = self.getCoordinate("SV/Auto_story/map_3.png", range_x=295, range_y=210, search_range=[150, 570, 345, 935])
            elif self.map == 1:
                _, x_pos, y_pos = self.getCoordinate("SV/Auto_story/map_kitakami.png", range_x=295, range_y=210, search_range=[150, 570, 345, 935])
            if (x - d) <= x_pos <= (x + d) and (y - d) <= y_pos <= (y + d):
                break
            else:
                count += 1
                if self.isContainTemplate('SV/Auto_story/eventflag.png',0.87):
                    if event_flag:
                        return
                    else:
                        self.returnTofield(button=Button.B)
                        self.openMap()                        
                        continue
                if count % 6 == 0:
                    self.returnTofield(button=Button.B)
                    if change_day:
                        if count % 18 == 0:
                            self.changeDay()
                    self.openMap()
                    continue
                if not (x_pos - x) == 0:
                    rad = math.atan((y_pos - y)/(x_pos - x))
                    deg = math.degrees(rad)
                    if x >= x_pos:
                        deg = - deg
                    else:
                        deg = 180-deg
                else:
                    if (y_pos - y) >= 0:
                        deg = 90
                    else:
                        deg = -90
                l = ((y_pos - y)**2 + (x_pos - x)**2)**0.5
                duration_time = l * 1.61 / 1000
                #print(round(deg, 1), round(l, 1), round(duration_time, 2))
                if count == 1:
                    self.press(Direction(Stick.LEFT, deg),duration=duration_time, wait=0.5)
                else:
                    if duration_time < 0.2:
                        self.press(Button.ZR,0.1,0.6)
                    self.press(Direction(Stick.LEFT, deg),duration=duration_time, wait=0.5)
                    if duration_time < 0.2:
                        self.press(Button.ZL,0.1,1.1)
                continue

    def getCoordinate(self, template_path, range_x, range_y, search_range=[0, 720, 0, 1280], threshold=0.8, use_gray=True):
        TEMPLATE_PATH = "./Template/"
        src = self.camera.readFrame()
        src = src[search_range[0]:search_range[1], search_range[2]:search_range[3]]#[150:570, 345:935]
        src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) if use_gray else src
        if "map_3" in template_path:
            template = self.map_3
        elif "map_kitakami" in template_path:
            template = self.map_kitakami
        else:
            template = cv2.imread(TEMPLATE_PATH + template_path, cv2.IMREAD_GRAYSCALE if use_gray else cv2.IMREAD_COLOR)
        res = cv2.matchTemplate(src, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        x, y = max_loc
        #print(max_val, int(x+range_x+1), int(y+range_y+1))
        if max_val > threshold:
            return True, int(x+range_x+1), int(y+range_y+1)
        else:
            return False, int(x+range_x+1), int(y+range_y+1)
        
    def getLocation(self, name):
        self.location = {'ネモの家':[2577, 6462],
                         '入り江のほら穴':[2597, 6363],
                         '灯台':[2678, 6286],
                         'プラトタウン':[2568, 6097],
                         'テーブルシティ道中_1':[2377, 6057],
                         'テーブルシティ道中_2':[2470, 5840],
                         'アカデミー':[2501, 5280], 
                         'アカデミー_1':[2501, 5439],
                         'テーブルシティ西':[2440, 5551],
                         'テーブルシティ_1':[2382, 5557],
                         'テーブルシティ_2':[2288, 5595],                 

                         'セルクルタウン道中_1':[2050, 5696],                       
                         'セルクルタウン東':[1687, 5595],
                         'セルクルタウン西':[1518, 5578],
                         '大空のヌシ道中_1':[1453, 5423],
                         '大空のヌシ道中_2':[1454, 5309],
                         '大空のヌシ道中_3':[1357, 5528],
                         '大空のヌシ道中_4':[1324, 5317],
                         '大空のヌシ道中_5':[1225, 5195],
                         '大空のヌシ道中_6':[1132, 5241],
                         '大空のヌシ道中_7':[1016, 5283],
                         '大空のヌシ道中_8':[964, 5356],
                         '大空のヌシ道中_9':[899, 5292],
                         '大空のヌシ道中_10':[878, 5184],#5189
                         '大空のヌシ道中_11':[741, 5066],
                         '大空のヌシ道中_12':[766, 4912],
                       
                         '土震のヌシ道中_1':[803, 4958],
                         '土震のヌシ道中_2':[897, 4500],
                         '土震のヌシ道中_3':[786, 4594],

                         '偽竜のヌシ道中_1':[1094, 4357],
                         '偽竜のヌシ道中_2':[946, 4200],
                         'マリナードタウン':[853, 4207],
                         '偽竜のヌシ道中_3':[709, 3955],
                         '偽竜のヌシ道中_4':[781, 3740],
                         '偽竜のヌシ道中_5':[1658, 3476],
                         '偽竜のヌシ道中_6':[1807, 3369],
                         '偽竜のヌシ道中_7':[1786, 3414],
                         '偽竜のヌシ道中_8':[1581, 3269],
                         '偽竜のヌシ道中_9':[1537, 3350],

                         '湖の孤島':[1503, 3384],
                         'チャンプルタウン西':[2049, 4187],
                         'チャンプルタウン東':[2197, 4133],
                         'チャンプルジム道中':[2083, 4088],
                         'チャンプルジム':[2115, 4129],
                         '食堂':[2190, 4167],

                         'カラフシティ西':[1569, 4542],
                         'カラフシティ北':[1595, 4387],
                         'マリナードタウン道中':[818, 4278],
                         '市場':[691, 4288],
                         'カラフジム':[1686, 4543],

                         'ベイクタウン道中_1':[964, 5352],
                         'ベイクタウン道中_2':[625, 6207],#1066, 5616   665, 6141
                         'ベイクタウン':[989, 6124],
                         'ベイクジム':[1117, 6114],
                         'エクササイズ会場':[1133, 6114],

                         'テーブルシティ東':[2713, 5574],
                         '岩壁のヌシ道中_1':[2913, 5653],
                         '岩壁のヌシ道中_2':[2994, 5513],
                         '岩壁のヌシ道中_3':[3064, 5521],
                         '岩壁のヌシ道中_4':[3160, 5445],#3147, 5448
                         '岩壁のヌシ道中_5':[3232, 5400],
                         '岩壁のヌシ道中_6':[3353, 5424],
                         '岩壁のヌシ道中_7':[3407, 5343],
                         '岩壁のヌシ道中_8':[3425, 5320],
                         '岩壁のヌシ道中_9':[3064, 5681],

                         'ボウルタウン東':[3862, 5470],
                         'ボウルタウン西':[3647, 5505],
                         'ボウルジム道中_1':[3783, 5486],#3780, 5486
                         'ボウルジム道中_2':[3753, 5785],
                         'ボウルジム':[3753, 5550],
                         'キマワリ集め会場':[3780, 5548],
                         'ハッコウシティ道中':[3885, 4848],
                         'ハッコウシティ南':[4044, 4861],
                         'ハッコウシティ北':[4105, 4543],
                         'ハッコウジム':[4072, 4774],

                         'ナッペ山':[2344, 3305],
                         #'フリッジタウン道中_1':[2617, 3118],
                         'フリッジタウン道中_1':[2630, 3110],
                         #'フリッジタウン道中_2':[2701, 3102],
                         'フリッジタウン道中_2':[2735, 3077],
                         #'フリッジタウン道中_3':[2810, 3131],
                         'フリッジタウン道中_3':[2810, 3120],
                         #'フリッジタウン道中_4':[2914, 3167],
                         'フリッジタウン道中_4':[2921, 3186],
                         'フリッジタウン道中_5':[2796, 3208],                        
                         'フリッジタウン':[2806, 3315],
                         'フリッジジム':[2864, 3374],

                         'ナッペ山ジム':[2964, 3614],
                         'ナッペ山ジム_1':[2918, 3658],
                         '雪山滑り':[2937, 3637],

                         'スター団あく組道中_1':[1503, 4632],
                         'スター団あく組道中_2':[1654, 4774],
                        
                         'スター団ほのお組道中_':[3707, 5264],

                         'スター団どく組道中_1':[3238, 4109],
                         'スター団どく組道中_2':[3118, 4161],

                         'スター団かくとう組道中':[4168, 3655],
                         'スター団かくとう組道中_1':[4074, 3601],
                         'スター団かくとう組':[4265, 3823],

                         'スター団フェアリー組道中':[2378, 2832],

                         'vsボタン':[2500, 5248],
                         'ボタン待ち合わせ場所':[2500, 5503],

                         '自分の家':[2420, 6449],

                         'ポケモンリーグ':[2136, 5184],
                         'テーブルシティ西門':[2193, 5594],

                         'vsネモ':[2484, 5581],

                         '潜鋼のヌシ道中_1':[3915, 4463],
                         '潜鋼のヌシ道中_2':[3902, 4415],
                         '潜鋼のヌシ道中_3':[3847, 4401],
                         '潜鋼のヌシ道中_4':[3992, 4457],
                         '潜鋼のヌシ道中_5':[3967, 4299],

                         'セルクルジム':[1594, 5618],
                         'オリーブころがし':[1533, 5487],

                         'ゼロゲート':[2293, 4385],
                         #'ゼロゲート':[2270, 4361],

                         'スイリョクタウン道中_1':[1901, 2575],
                         'スイリョクタウン道中_2':[1975, 2490],
                         'スイリョクタウン道中_3':[1975, 2270],
                         'スイリョクタウン':[1989, 2367],
                         '看板1道中_1':[1499, 2386],
                         '看板1道中_2':[1514, 2214],
                         '歴史の看板_1':[1555, 2218],
                         'キタカミセンター':[2417, 2032],
                         '看板2道中_1':[2429, 1876],
                         '看板2道中_2':[2352, 1872],
                         '歴史の看板_2':[2303, 1929],
                         '恐れ穴_道中':[2061, 1823],
                         '恐れ穴':[1980, 1828],
                         'ゼイユとスグリの家_道中':[1904, 2378],
                         'ゼイユとスグリの家':[1919, 2256],
                         '鬼退治フェス会場':[2359, 1849],
                         'キタカミセンター入口':[2423, 1976],
                         'ゼイユとスグリの家_道中_2':[1910, 2294],
                         '桃沢商店':[2023, 2366],
                         '看板3道中_1':[1265, 2508],
                         '看板3道中_2':[809, 1621],
                         '歴史の看板_3':[946, 942],
                         'てらす池道中_1':[1436, 1962],
                         'てらす池道中_2':[1166, 1544],
                         'てらす池道中_3':[1663, 1219],
                         'てらす池_ゼイユ':[1740, 1594],
                         '祠':[1672, 2239],
                         '管理人':[2334, 1849],
                         '情報三人目_1':[1914, 2385],
                         '情報三人目_2':[1905, 2288],
                         'マシマシラ':[865, 2496],
                         'イイネイヌ':[913, 702],
                         'キチキギス_1':[2153, 1535],
                         'てらす池':[1720, 1564],
                         'キチキギス_道中':[2425, 1458],
                         'キチキギス_2':[2315, 1485],
                         }
        return self.location[name][0], self.location[name][1]

    
