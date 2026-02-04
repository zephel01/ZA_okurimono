#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand
from Commands.Keys import Button, Hat, Direction
# 文字入力用のライブラリをインポート（Modified/Extension版に標準搭載）
from Commands.PythonCommands.Samples.InputSwitchKeyboard import SwitchKeyboard

class SerialCodeMacro(PythonCommand):
    # Poke-Controllerの画面に表示される名前
    NAME = 'シリアルコード入力マクロ'

    def __init__(self):
        super().__init__()

    def do(self):
        # --------------------------------------------------
        # ここにシリアルコード（英数字）を入力してください
        # --------------------------------------------------
        SERIAL_CODE = "PREPAR1NG" 

        # 1. Xボタン（メニューを開く）
        self.press(Button.X, wait=1.0)

        # 2. 上ボタン（Direction.UP または Hat.TOP）
        self.press(Direction.UP, wait=0.5)

        # 3. Aボタン
        self.press(Button.A, wait=1.0)

        # 4. 十字キー左
        self.press(Hat.LEFT, wait=0.5)

        # 5. 十字キー下
        self.press(Hat.BTM, wait=0.5)

        # 6. Aボタン
        self.press(Button.A, wait=1.0)

        # 7. 十字キー下
        self.press(Hat.BTM, wait=0.5)

        # 8. Aボタン
        self.press(Button.A, wait=1.5)

        # 9. Aボタン（入力フォームを開くため少し長めに待機）
        self.press(Button.A, wait=3.0)

        # 10. シリアルコード文字入力
        # キーボード操作クラスの初期化
        keyboard = SwitchKeyboard(self)
        # 指定したコードを入力
        keyboard.input(SERIAL_CODE)
        
        # 入力完了後の確定操作が必要な場合は以下を追加
        # self.press(Button.PLUS, wait=2.0) 

        self.finish()
