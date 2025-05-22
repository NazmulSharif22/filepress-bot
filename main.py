import logging
from pyrogram import Client, filters
from config import API_ID, API_HASH, SESSION, BOT_USERNAME
from uploader import upload_to_filepress

logging.basicConfig(level=logging.INFO)

app = Client(
    name="filepress_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
)

@app.on_message(filters.private & filters.document)
async def handle_file(client, message):
    downloading_msg = await message.reply("⬇️ Downloading file...")
    file_path = await message.download()
    await downloading_msg.edit("⬆️ Uploading to FilePress...")

    try:
        link = upload_to_filepress(file_path)
        await downloading_msg.edit(f"✅ Uploaded:\n{link}")
    except Exception as e:
        await downloading_msg.edit(f"❌ Upload failed:\n`{e}`")

app.run()
