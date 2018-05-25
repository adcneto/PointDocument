from opsdroid.matchers import match_regex
import random

@match_regex(r'registry novo|novo registry|registry|new registry|faq do registry|docs do registry', case_sensitive=False)
async def newregistry(opsdroid, config, message):
    await message.respond('https://confluence.intranet.uol.com.br/confluence/display/PagSeguro/FAQ+-+Docker+Registry')

@match_regex(r'exit 34|exit status 34|erro 34')
async def erro34 (opsdroid, config, message):
    if match_regex(r'exit 34|exit status 34|erro 34') == "exit 34":
        message.respond("Tudo bem, meu bacano? \n")
    await message.respond('https://confluence.intranet.uol.com.br/confluence/pages/viewpage.action?pageId=176849282')

@match_regex(r'amazon web services|aws', case_sensitive=False)
async def faq_aws (opsdroid, config, message):
    await message.respond('https://confluence.intranet.uol.com.br/confluence/display/PagSeguro/FAQ')


@match_regex(r'(?:aws|amazon web services) (?:erro 34|exit status 34)|(?:erro 34|exit status 34) (?:aws|amazon web services)', case_sensitive=False)
async def too_many_requisitions (opsdroid, config, message):
    await message.respond("Relate apenas um problema por vez. Meu neocórtex positrônico é de 32 bit!")
