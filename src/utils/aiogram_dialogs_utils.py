from aiogram_dialog import DialogManager


def list_to_select_format(items: list, custom_index: list | None = None) -> list[tuple]:
    return [(index, elem) for index, elem in zip(range(len(items)) if custom_index is None else custom_index, items)]


def get_dialog_data_dto(dialog_manager: DialogManager, custom_name: str = 'dialog_data_dto'):
    return dialog_manager.dialog_data.get(custom_name)
