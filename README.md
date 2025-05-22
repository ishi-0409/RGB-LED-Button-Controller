# RGB LED Button Controller

このプロジェクトは、Raspberry Pi と RGB LED を用いて  
**赤・緑・青の各色に異なる動作を割り当てたLED制御システム**です。  
ChatGPTと一緒に回路・プログラムを構築しました。

---

## 概要

3つのボタンを用いて、それぞれのLEDに以下の機能を割り当てています：

| 色 | 操作 | 動作 |
|----|------|------|
| 赤 | ボタン（プッシュ式） | ON/OFFのトグル制御 |
| 緑 | ボタン長押し | 長押ししている間だけ点滅 |
| 青 | ボタン（トグル式） | ボタンを押すたびに明るさを段階的に切り替え（PWM制御） |

---
## 参考資料

この装置のアイデアと回路構成は、以下の動画を参考にしました：

- [Raspberry Pi LESSON 12: Pushbutton Control of RGB LED](https://www.youtube.com/watch?v=hkdqWVx-HhM&t=2738s)

##  デモ動画

この作品の動作デモを以下のYouTube動画にアップロードしました：

- [RGB LED ボタン制御デモ | Raspberry Pi × Python × ChatGPT](https://www.youtube.com/watch?v=uFYHbG6Avpg)

動画では、以下の3つのLED動作を順番に紹介しています：

1. **赤LED**：ボタンを押すたびにON/OFFが切り替わるトグル動作  
2. **緑LED**：ボタンを長押ししている間だけ点滅  
3. **青LED**：トグルスイッチで押すたびに明るさが変化（PWM）


##  改善点

- プログラムを `Ctrl+C` で終了した際に、以下のようなエラーが表示されます

TypeError: unsupported operand type(s) for &: 'NoneType' and 'int'


→ `RPi.GPIO` ライブラリの終了処理に起因するもので、現時点では解決できていません。動作には支障ありません。

- プログラム再起動時、青色LEDが一瞬だけ点灯することがあります。  
→現在のところ確実な解決方法は見つかっていません。




