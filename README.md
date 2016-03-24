# Ishibashi

IshibashiはHardwareのユニットテストを行う為のライブラリです。
Raspberry pi などにインストールして、
標準ライブラリである unittest と併用して利用してください。

# Usage

```
  Ishibashi() # gpio modeで起動
  Ishibashi("bcm") # gpio modeで起動
  Ishibashi("pin") # pin modeで起動
```
