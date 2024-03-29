# smart-remocon-on-raspbeerypi

## 要件
スマートフォンから、シーリングライト、エアコンなど、赤外線通信を行う家電を操作できるようにする。

## 使用機器
IoT機器として、raspberrypi zero を用いる。また、raspberry pi zero 上に赤外線受信回路、赤外線送信回路を実装する。

## 使用方法
まず、raspberrypi側に送信する赤外線信号を登録しておく。  
また、スマートフォンからメッセージを受け取るためのdiscord bot serverを立てておく。  

iosではショートカットのアプリなどからdiscord webhookを使ってdiscordにメッセージを送信する。  
メッセージに対応した赤外線信号がraspberrpiから発信される。

※discord bot serverを用いるのは簡単に外部のネットワークからでもアクセスできるようにするためであるので、ネットワーク機器の設定を適切に行えば適当なサーバーでも問題ない。
## アーキテクチャ/技術仕様

インターネットを介しての接続はDiscordを通して行う。raspberrypi zero上にサーバーを構築してインターネット上からアクセスできるようにしてもいいが、セキュリティ面の問題が多い(FWの設定や認証機構など)のでDiscord Botを作成し、Botコマンドを介して機器を操作するようにすることで、セキュリティ面を考慮した実装の普段を減らす。

しかし、いちいちDiscordでコマンドを実行するのは面倒である。たとえば、シーリングライトをつけたり消したりするだけでも

1. スマホのロックを解除
2. SNSのフォルダに移動
3. Discordを起動
4. 専用のサーバーに移動
5. テキスト欄に’ \ ‘を打ち込む
6. Bot コマンドを選択
7. Bot コマンドを実行

と最大で7つのステップが必要になる。
そこで、簡単な操作の手間を削減するために、LAN内にのみ公開するサーバーをraspberrypi zero上に構築し、ブラウザから直接エンドポイントを叩くことで、機器の操作を行えるようにする。
エンドポイントをお気に入り登録すれば、簡単な操作に限れば

1. スマホのロックを解除
2. エンドポイントをまとめたフォルダに移動
3. 行いたい操作に応じたエンドポイントにアクセス

の3ステップだけで操作を行えるようになる。
エンドポイントを直接叩くことによって行える操作は以下の6つを考えている。

1. シーリングライトの点灯
2. シーリングライトライトの消灯
3. エアコンの起動
4. エアコンの停止
5. エアコンが二時間後に止まるタイマーをセット
6. エアコンが午前7時に起動するタイマーをセット

この6つを選んだのは、普段行う操作の9割以上がこの操作だからである。
エアコンに関して、

5月〜10月は冷房27℃
11月から4月は暖房21℃

に設定する。
温度を変更したい場合はDiscord Botのコマンドから操作を行う。
また、エンドポイントにアクセスして操作を行う場合Discordを経由しない。これはもしDiscordのサーバーがダウンしても最低限の操作は行えるように、という措置である。