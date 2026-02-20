<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Private Space</title>
    <style>
        body { background: #000; color: #fff; font-family: -apple-system, sans-serif; margin: 0; display: flex; flex-direction: column; height: 100vh; }
        #chat { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; }
        .msg { margin-bottom: 15px; max-width: 85%; padding: 10px 15px; border-radius: 18px; line-height: 1.5; word-wrap: break-word; }
        .user { align-self: flex-end; background: #007aff; color: white; }
        .bot { align-self: flex-start; background: #262626; color: #ff79c6; }
        .img-content { width: 100%; max-width: 250px; border-radius: 10px; margin-top: 10px; cursor: pointer; border: 1px solid #444; }
        #input-area { background: #121212; padding: 15px; display: flex; border-top: 1px solid #333; }
        input { flex: 1; background: #222; border: none; color: white; padding: 12px 18px; border-radius: 25px; outline: none; }
        button { background: none; border: none; color: #ff79c6; font-weight: bold; margin-left: 10px; padding: 0 10px; }
    </style>
</head>
<body>
    <div id="chat"></div>
    <div id="input-area">
        <input type="text" id="msg" placeholder="跟我說點私密的事..." onkeypress="if(event.keyCode==13) send()">
        <button onclick="send()">傳送</button>
    </div>

    <script>
        async function send() {
            const input = document.getElementById('msg');
            const chat = document.getElementById('chat');
            const text = input.value.trim();
            if (!text) return;

            input.value = '';
            chat.innerHTML += `<div class="msg user">${text}</div>`;
            chat.scrollTop = chat.scrollHeight;

            try {
                const res = await fetch('/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: text})
                });
                const data = await res.json();
                
                // 圖片解析邏輯
                let formattedReply = data.reply.replace(/\[IMAGE:(.*?)\]/g, (match, url) => {
                    return `<br><img src="${url}" class="img-content" onclick="window.open('${url}')">`;
                });

                chat.innerHTML += `<div class="msg bot">${formattedReply}</div>`;
                chat.scrollTop = chat.scrollHeight;
            } catch (e) {
                chat.innerHTML += `<div class="msg bot">連線失敗...</div>`;
            }
        }
    </script>
</body>
</html>
