from aiogram_dialog import DialogManager


def list_to_select_format(items: list, custom_index: list | None = None) -> list[tuple]:
    return [(index, elem) for index, elem in zip(range(len(items)) if custom_index is None else custom_index, items)]


def get_dialog_data_dto(dialog_manager: DialogManager, custom_name: str = 'dialog_data_dto'):
    return dialog_manager.dialog_data.get(custom_name)


# class CloseAndSwitchTo(SwitchTo):
#     def __init__(self, text: Format, state: State, start_data_contains: list[str]):
#         super().__init__(
#             text=text,
#             id=f'back_and_switch_{state.state[:10]}',
#             state=state
#         )
#         self.state = state
#         self.start_data_contains = start_data_contains
#
#     async def _on_click(
#             self, callback: CallbackQuery, button: Button,
#             manager: DialogManager,
#     ):
#         await manager.done()
#
#         if self.start_data_contains:
#             dd: dict = get_dialog_data_dto(manager).model_dump()
#             await manager.start(self.state, data={data: dd[data] for data in self.start_data_contains})
#         else:
#             await manager.start(self.state)
#
