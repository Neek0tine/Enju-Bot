import os
import random
import asyncio
import dialogflow
from discord.ext import commands


class DialogCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['hey', 'hello', 'whatsup?', 'whatsup', 'busy?', 'can we talk?'])
    async def enju(self, ctx):
        ans = ["whats up?",
               "hey",
               "hello",
               "yes?",
               "how can I help u?"]
        busy = random.choice(ans)
        await ctx.send(busy)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'
        DIALOGFLOW_PROJECT_ID = 'enju-kbckgm'
        DIALOGFLOW_LANGUAGE_CODE = 'en'
        SESSION_ID = 'me'
        bye = 'bye'
        print('[+] Talk command initiated')
        processed_input = ''
        while processed_input != bye:
            try:
                try:
                    user_input = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30,)
                    processed_input = str(user_input.content)
                    processed_input = processed_input.lower()
                except:
                    print('[!] No message detected or understood, is it string?')
                    pass
            except asyncio.TimeoutError:
                await ctx.send('geez go talk to someone else')
                print('[!] Bot ignored, ignoring you :<')

            session_client = dialogflow.SessionsClient()
            session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
            text_input = dialogflow.types.TextInput(text=processed_input, language_code=DIALOGFLOW_LANGUAGE_CODE)
            query_input = dialogflow.types.QueryInput(text=text_input)
            response = session_client.detect_intent(session=session, query_input=query_input)
            reply = response.query_result.fulfillment_text
            print("\n[+] Query text:", response.query_result.query_text)
            print("[+] Detected intent:", response.query_result.intent.display_name)
            print("[+] Detected intent confidence:", response.query_result.intent_detection_confidence)
            print("[+] Fulfillment text:", response.query_result.fulfillment_text, "\n")
            await ctx.trigger_typing()
            await asyncio.sleep(2)
            await ctx.send(reply)
        print('[+] Talk command stopped')

def setup(bot):
    bot.add_cog(DialogCog(bot))
