from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class WorkerKeyboards:
    @staticmethod
    def take_on_job(task_id: int) -> InlineKeyboardMarkup:
        kb = InlineKeyboardBuilder()
        kb.button(text='Принять в работу', callback_data=f'take_on_job:{task_id}')
        return kb.as_markup()

    @staticmethod
    def done_task(task_id: int) -> InlineKeyboardMarkup:
        kb = InlineKeyboardBuilder()
        kb.button(text='Заказ выполнен', callback_data=f'done_task:{task_id}')
        return kb.as_markup()
