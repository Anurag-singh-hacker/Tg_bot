from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import asyncio

BOT_TOKEN = "8534778362:AAFRBJs6IEtOtsuoFBqQnbAfPVAiQcKC8ck"

# ---------- START ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome\n\nCommands:\n"
        "/like 12345678\n"
        "/info 12345678\n"
        "\n☠️ Developer Anurag Singh\n"
            "☠️ Insta @anuragkumarsinghofficial 💙\n"
            "😍 Follow For More 🥰"
    )

# ---------- LIKE COMMAND ----------
async def like(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Use like this:\n/like 12345678")
        return

    uid = context.args[0]

    # 🔄 instant waiting message
    msg = await update.message.reply_text(
        "wait..... 😊\n🤩 By Anurag Singh ...."
    )

    await asyncio.sleep(2)

    try:
        url = f"https://mukesh-ult-like.vercel.app/like?uid={uid}&region=ind&key=UDIT"
        r = requests.get(url, timeout=20)
        data = r.json()

        text = (
            f"🥰 Likes Given By API : {data.get('LikesGivenByAPI', 'N/A')}\n"
            f"🤗 Likes After Command : {data.get('LikesafterCommand', 'N/A')}\n"
            f"😍 Likes Before Command : {data.get('LikesbeforeCommand', 'N/A')}\n"
            f"😎 Player Nickname : {data.get('PlayerNickname', 'N/A')}\n"
            f"☠️ Level : {data.get('Level', 'N/A')}\n"
            f"💀 Region : {data.get('Region', 'N/A')}\n"
            f"👽 UID : {data.get('UID', uid)}\n"
            f"status : {data.get('status', 'N/A')}\n"
            f"daily_limit : 20 Like 1 uid\n\n"
            f"☠️ Developer Anurag Singh\n"
            "☠️ Insta @anuragkumarsinghofficial 💙\n"
            "😍 Follow For More 🥰"
            
        )

        await msg.edit_text(text)

    except Exception as e:
        await msg.edit_text("❌ Like API error / network issue")

# ---------- INFO COMMAND ----------
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Use info like this:\n/info 12345678")
        return

    uid = context.args[0]

    # 🔄 instant waiting message
    msg = await update.message.reply_text(
        "wait..... 😊\n🤩 By Anurag Singh ...."
    )

    await asyncio.sleep(2)

    try:
        url = f"http://danger-info-alpha.vercel.app/accinfo?uid={uid}&key=DANGERxINFO"
        r = requests.get(url, timeout=20)

        if r.status_code != 200:
            await msg.edit_text("❌ Info API response error")
            return

        data = r.json()

        text = ""
        for k, v in data.items():
            text += f"{k} : {v}\n"

        text += (
            "\n☠️ Developer Anurag Singh\n"
            "☠️ Insta @anuragkumarsinghofficial 💙\n"
            "😍 Follow For More 🥰"
        )

        await msg.edit_text(text)

    except Exception as e:
        await msg.edit_text("❌ Info API / network issue")

# ---------- MAIN ----------
def main():
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .connect_timeout(30)
        .read_timeout(30)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("like", like))
    app.add_handler(CommandHandler("info", info))

    print("🤖 Bot running...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
