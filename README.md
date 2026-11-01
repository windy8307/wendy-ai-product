# WENDY 國外連線系統 — 第一階段

此專案是可部署的 LINE Webhook 基礎版。尚未實作 AI 命名、訂單統計或 LINE 訊息回覆。

## Render 部署
1. 建立 **Private** GitHub repository，將本資料夾中的檔案上傳至 repository 根目錄。
2. Render → New → Web Service → 連接 GitHub repository。
3. Runtime 選 Python；Build Command: `pip install -r requirements.txt`。
4. Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`。
5. Environment 設 `LINE_CHANNEL_SECRET` 為重新核發的 Channel secret。不要放入程式碼或 GitHub。
6. 部署完成後先開啟 `https://你的網域/health`，應顯示 `{"status":"ok"}`。
7. LINE Official Account Manager → Messaging API → Webhook 網址填 `https://你的網域/callback`，再於 LINE Developers 啟用 webhook 並驗證。

## 安全
LINE_CHANNEL_SECRET 必須是伺服器環境變數。截圖若曾暴露 secret，請先重新核發。
Webhook 會驗證 LINE 簽章，避免任意偽造事件。

## 限制
LINE OpenChat 社群訊息無法透過一般 Messaging API 直接收取。本階段只驗證 LINE Webhook 連線，不會自動讀取社群 +1。後續會另建網頁下單。
