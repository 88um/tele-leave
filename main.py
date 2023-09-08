from telethon.sync import TelegramClient

# Your API ID and API hash from https://my.telegram.org
api_id = 1370903  
api_hash = '23c73e7bb6075cd2c909ca51decd7460'

# Your phone number
phone_number = '6281396578255'

# Initialize the Telegram client
client = TelegramClient(phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
            client.send_code_request(phone_number)
            client.sign_in(phone_number, input('[+] Enter the code: '))


async def leave_all_channels():
    # Connect to the Telegram server
    await client.start()

    try:
        # Get a list of all the channels you are a member of
        dialogs = await client.get_dialogs()

        # Iterate through the dialogs and leave each channel
        for dialog in dialogs:
            if dialog.is_channel:
                await client.delete_dialog(dialog.entity)
                print(f'Left channel: {dialog.name}')

    finally:
        # Disconnect the client
        await client.disconnect()

# Run the leave_all_channels function
with client:
    client.loop.run_until_complete(leave_all_channels())
