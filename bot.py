import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ChatAction
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
    MessageHandler, 
    Filters)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT = range(8)
# Callback data
ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN,ELEVEN, TWELVE = range(12)



def start(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    print(update)
    keyboard = [
        [InlineKeyboardButton(text='1. Leer un cuento', callback_data=str(ONE)),InlineKeyboardButton(text='2. Ver videos', callback_data=str(TWO))],
        [InlineKeyboardButton(text='Sobre Atenas Education', url='https://atenas.education')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("\U0001F680 Hola "+user.first_name+", qué deseas hacer:", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now

    return FIRST

def start_over(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [InlineKeyboardButton(text='1. Leer un cuento', callback_data=str(ONE)),InlineKeyboardButton(text='2. Ver videos', callback_data=str(TWO))],
        [InlineKeyboardButton(text='Sobre Atenas Education', url='https://atenas.education')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(text="\U0001F680 Hola, qué deseas hacer:", reply_markup=reply_markup)
    return FIRST

def cuentos(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Científicas", callback_data=str(THREE)),
            InlineKeyboardButton("Ingenieras", callback_data=str(FOUR)),
            InlineKeyboardButton("Astronautas", callback_data=str(FIVE)),
        ],
        [
            InlineKeyboardButton("Profesoras", callback_data=str(SIX)),
            InlineKeyboardButton("Físicas", callback_data=str(SEVEN)),
            InlineKeyboardButton("Matemáticas", callback_data=str(EIGHT)),
        ]
        ,
        [
            InlineKeyboardButton("Sugerir cuento \U0001F4DA", callback_data=str(ELEVEN)),
        ]
        ,
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(NINE)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(TEN)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Elige una categoría \U00002705", reply_markup=reply_markup
    )
    return FIRST

def sugerir(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
                [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(NINE)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(TEN)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="\U0001F91A Sugerir cuentos:\n\n Responde este mensaje para sugerir un personaje o para realizar el aporte de un cuento\n", reply_markup=reply_markup
    )
    return NINE


def videos(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("También quiero ser ingeniera", callback_data=str(ONE))],
        [   InlineKeyboardButton("Mensaje a niñas que quieren ser científicas", callback_data=str(TWO))],
        [   InlineKeyboardButton("Día de la Mujer en la Ciencia", callback_data=str(THREE))],
        [   InlineKeyboardButton("Mensaje a niñas que quieren ser científicas 2", callback_data=str(FOUR))],
        [   InlineKeyboardButton("¿Qué piensan las niñas en la ciencia?", callback_data=str(FIVE)),
        ],
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(NINE)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(TEN)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="\U0001F3A5 Escoge uno de los siguientes videos", reply_markup=reply_markup
    )
    return SECOND

def video1(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(SEVEN)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(EIGHT)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=" También quiero ser ingeniera https://youtu.be/5sk51Onnl5M",reply_markup=reply_markup)
    # Transfer to conversation state `SECOND`
    return SECOND

def video2(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(SEVEN)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(EIGHT)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=" Mensaje a niñas que quieren ser científicas https://youtu.be/Hc6kK168SM8",reply_markup=reply_markup)
    # Transfer to conversation state `SECOND`
    return SECOND

def video3(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(SEVEN)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(EIGHT)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Día de la Mujer en la Ciencia https://youtu.be/N45tehAL7jw",reply_markup=reply_markup)
    # Transfer to conversation state `SECOND`
    return SECOND

def video4(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(SEVEN)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(EIGHT)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=" También quiero ser ingeniera https://youtu.be/5sk51Onnl5M",reply_markup=reply_markup)
    # Transfer to conversation state `SECOND`
    return SECOND

def video5(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(SEVEN)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(EIGHT)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="¿Qué piensan las niñas en la ciencia https://youtu.be/s9uEobyqdr8",reply_markup=reply_markup)
    # Transfer to conversation state `SECOND`
    return SECOND

def cat1(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Matilde Hidalgo", callback_data=str(ONE))],
        [InlineKeyboardButton("Margaret Hamilton", callback_data=str(TWO))],
        [InlineKeyboardButton("Marie Curie", callback_data=str(THREE))],
        [InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Elige una científica \U0001F469\u200d\U0001F52C", reply_markup=reply_markup
    )
    return THREE

def cat2(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Margaret Hamilton", callback_data=str(ONE))],
        [InlineKeyboardButton("Marie Curie", callback_data=str(TWO))],
        [InlineKeyboardButton("Matilde Hidalgo", callback_data=str(THREE))],
        [InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Elige una ingeniera \U0001F469\u200d\U0001F4BB", reply_markup=reply_markup
    )
    return FOUR

def cat3(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Margaret Hamilton", callback_data=str(ONE))],
        [InlineKeyboardButton("Marie Curie", callback_data=str(TWO))],
        [InlineKeyboardButton("Matilde Hidalgo", callback_data=str(THREE))],
        [InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Elige una astronauta \U0001F469\u200d\U0001F680", reply_markup=reply_markup
    )
    return FIVE

def cat4(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Margaret Hamilton", callback_data=str(ONE))],
        [InlineKeyboardButton("Marie Curie", callback_data=str(TWO))],
        [InlineKeyboardButton("Matilde Hidalgo", callback_data=str(THREE))],
        [InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Elige una profesora \U0001F469\u200d\U0001F3EB", reply_markup=reply_markup
    )
    return SIX

def cat5(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Margaret Hamilton", callback_data=str(ONE))],
        [InlineKeyboardButton("Marie Curie", callback_data=str(TWO))],
        [InlineKeyboardButton("Matilde Hidalgo", callback_data=str(THREE))],
        [InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Elige una física \U0001F469\U0001F3FD\u200d\U0001F52C", reply_markup=reply_markup
    )
    return SEVEN

def cat6(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Margaret Hamilton", callback_data=str(ONE))],
        [InlineKeyboardButton("Marie Curie", callback_data=str(TWO))],
        [InlineKeyboardButton("Matilde Hidalgo", callback_data=str(THREE))],
        [InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Elige una matemática \U0001F469\U0001F3FD\u200d\U0001F3EB", reply_markup=reply_markup
    )
    return EIGHT

def cuento1(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La primera mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return THREE

def cuento2(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La segunda mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return THREE

def cuento3(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La tercera mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return THREE

def cuento4(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La cuarta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FOUR

def cuento5(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La quinta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FOUR

def cuento6(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La sexta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FOUR

def cuento7(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La sexta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIVE

def cuento8(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La sexta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIVE

def cuento9(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La sexta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIVE

def cuento10(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La sexta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return SIX

def cuento11(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La sexta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return SIX

def cuento12(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La sexta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return SIX

def cuento13(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La sexta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return SEVEN

def cuento14(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La sexta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return SEVEN

def cuento15(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La sexta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return SEVEN

def cuento16(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La sexta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return EIGHT

def cuento17(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La sexta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return EIGHT

def cuento18(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(FOUR)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="La sexta mujer que viajó al espacio https://telegra.ph/Ejemplo-de-cuento-03-19",reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return EIGHT


def cuento_over(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Científicas", callback_data=str(THREE)),
            InlineKeyboardButton("Ingenieras", callback_data=str(FOUR)),
            InlineKeyboardButton("Astronautas", callback_data=str(FIVE)),
        ],
        [
            InlineKeyboardButton("Profesoras", callback_data=str(SIX)),
            InlineKeyboardButton("Físicas", callback_data=str(SEVEN)),
            InlineKeyboardButton("Matemáticas", callback_data=str(EIGHT)),
        ],
        [
            InlineKeyboardButton("\U0001F519 Volver", callback_data=str(NINE)),
            InlineKeyboardButton("\U0001F44B Salir", callback_data=str(TEN)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Elige una categoría  \U00002705", reply_markup=reply_markup
    )
    return FIRST


def end(update: Update, _: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over"""
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="\U0001F44B Gracias por visitarnos")
    return ConversationHandler.END

def input_text(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    user = update.message.from_user
    chat_id=str(update.message.chat_id)
    print(update.message.chat_id)
    keyboard = [
        [InlineKeyboardButton(text='\U0001F519 Volver', callback_data=str(FOUR)),InlineKeyboardButton(text='\U0001F44B Salir', callback_data=str(FIVE))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("\U0001F44C Gracias "+user.first_name+" por tu aporte, lo atenderé en la brevedad posible. \n\n\U0001F913 Mientras tanto te invito a seguir disfrutando de más recursos", reply_markup=reply_markup)

    context.bot.send_message(
        chat_id='1688282470',
        text=user.first_name+" "+user.last_name+" acabó de enviar el siguiente mensaje: \n\n"+text
    )
    return THREE



def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("1718982456:AAHS0vQruzh3TB5U1NOcd-CuYiqbDWm8zmY")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

 
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(cuentos, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(videos, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(cat1, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(cat2, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(cat3, pattern='^' + str(FIVE) + '$'),
                CallbackQueryHandler(cat4, pattern='^' + str(SIX) + '$'),
                CallbackQueryHandler(cat5, pattern='^' + str(SEVEN) + '$'),
                CallbackQueryHandler(cat6, pattern='^' + str(EIGHT) + '$'),
                CallbackQueryHandler(start_over, pattern='^' + str(NINE) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(TEN) + '$'),
                CallbackQueryHandler(sugerir, pattern='^' + str(ELEVEN) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(video1, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(video2, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(video3, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(video4, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(video5, pattern='^' + str(FIVE) + '$'),
                CallbackQueryHandler(start_over, pattern='^' + str(SEVEN) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(EIGHT) + '$'),
            ],
            THREE: [
                CallbackQueryHandler(cuento1, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(cuento2, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(cuento3, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(cuento_over, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(FIVE) + '$'),
            ],
            FOUR: [
                CallbackQueryHandler(cuento4, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(cuento5, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(cuento6, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(cuento_over, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(FIVE) + '$'),
            ],
            FIVE: [
                CallbackQueryHandler(cuento7, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(cuento8, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(cuento9, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(cuento_over, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(FIVE) + '$'),
            ],
            SIX: [
                CallbackQueryHandler(cuento10, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(cuento11, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(cuento12, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(cuento_over, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(FIVE) + '$'),
            ],
            SEVEN: [
                CallbackQueryHandler(cuento13, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(cuento14, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(cuento15, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(cuento_over, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(FIVE) + '$'),
            ],
            EIGHT: [
                CallbackQueryHandler(cuento16, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(cuento17, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(cuento18, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(cuento_over, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(FIVE) + '$'),
            ],
            NINE: [
                MessageHandler(Filters.text, input_text)
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to dispatcher that will be used for handling
    # updates
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
