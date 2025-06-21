"""This is the module that defines draggable card.
"""

from collections.abc import Callable
from logging import getLogger
from tkinter import Event

import customtkinter as ctk

from lib.common.types import EventName as E
from lib.common.types import ParamLog
from lib.components.base import BaseComponent, BasePage, EventBus

PARAM_LOG = ParamLog()
LOGGER = getLogger(PARAM_LOG.NAME)

MIN_CARD_LENGTH = 2


class DraggableCard(ctk.CTkFrame, BaseComponent):
    """Defines the draggable card.

    Args:
        master (ctk.CTkBaseClass): The parent widget of this widget.
        event_bus (EventBus): :class:`EventBus` class.
        index (int): The order index of the :class:`DraggableCard`.
    """
    def __init__(
            self,
            master: ctk.CTkBaseClass,
            event_bus: EventBus,
            index: int,
        ) -> None:
        ctk.CTkFrame.__init__(self=self, master=master)
        BaseComponent.__init__(self=self, event_bus=event_bus)
        self.index = index

        self.configure(fg_color=('gray80', 'gray20'), corner_radius=10)
        self.default_fg_color = self.cget('fg_color')
        self.drop_item_y: int = self.winfo_y()
        self.columnconfigure(index=0, weight=1)

        self.label = ctk.CTkLabel(self, text=f'カード {index + 1}')
        self.label.grid(row=0, column=0, pady=10)

        self.bind_all_children(
            widget=self,
            sequence='<Button-1>',
            command=self.on_click,
        )
        self.bind_all_children(
            widget=self,
            sequence='<B1-Motion>',
            command=self.on_drag,
        )
        self.bind_all_children(
            widget=self,
            sequence='<ButtonRelease-1>',
            command=self.on_release,
        )
        # self.bind(sequence='<Button-1>', command=self.on_click)
        # self.bind(sequence='<B1-Motion>', command=self.on_drag)
        # self.bind(sequence='<ButtonRelease-1>', command=self.on_release)

        self.set_cursor_all_children(widget=self, cursor='hand2')

    def register_events(self) -> dict[str, Callable]:  # noqa: PLR6301
        """Returns a list of events to subscribe to.

        Returns:
            dict[str, Callable]: events list to register. (key: event name, val: func)
        """
        return {}

    def bind_all_children(
            self,
            widget: ctk.CTkBaseClass,
            sequence: str,
            command: Callable,
        ) -> None:
        """Binds recursively to all child widgets.

        Args:
            widget (ctk.CTkBaseClass): The widget.
            sequence (str): The sequence of actions.
            command (Callable): The function that binds to a sequence of actions.
        """
        widget.bind(sequence, command)
        for child in widget.winfo_children():
            self.bind_all_children(widget=child, sequence=sequence, command=command)

    def set_cursor_all_children(
            self,
            widget: ctk.CTkBaseClass,
            cursor: str,
        ) -> None:
        """Sets recursively the cursor type for all child widgets.

        Args:
            widget (ctk.CTkBaseClass): The widget.
            cursor (str): The cursor type.
        """
        widget.configure(cursor=cursor)
        for child in widget.winfo_children():
            self.set_cursor_all_children(widget=child, cursor=cursor)

    def on_click(self, _: Event) -> None:
        """Updates the UI.

        Args:
            _ (Event): The properties of an tkinter event.
        """
        self.configure(fg_color=('white', 'black'))
        self.set_cursor_all_children(widget=self, cursor='double_arrow')

    def on_drag(self, event: Event) -> None:
        """Updates the UI.

        Args:
            event (Event): The properties of an tkinter event.
        """
        self.drop_item_y = event.y
        self.event_bus.emit(
            event_name=E.REORDER,
            drag_idx=self.index,
            drop_item_y=self.drop_item_y,
        )

    def on_release(self, event: Event) -> None:
        """Updates the UI.

        Args:
            event (Event): The properties of an tkinter event.
        """
        self.drop_item_y = event.y
        self.event_bus.emit(
            event_name=E.REORDER,
            drag_idx=self.index,
            drop_item_y=self.drop_item_y,
        )
        self.configure(fg_color=self.default_fg_color)
        self.set_cursor_all_children(widget=self, cursor='hand2')


class DraggableCardParentFrame(BasePage):
    """Defines the parent frame of the :class:`DraggableCard`.

    Args:
        master (ctk.CTkBaseClass): The parent widget of this widget.
        event_bus (EventBus): :class:`EventBus` class.
    """
    page_name = 'Draggable Card Panrent Frame'

    def __init__(self, master: ctk.CTk, event_bus: EventBus) -> None:
        super().__init__(master=master, event_bus=event_bus, page_name=self.page_name)

        self.cards: list[DraggableCard] = []

        self.columnconfigure(index=0, weight=1)

    def register_events(self) -> dict[str, Callable]:
        """Returns a list of events to subscribe to.

        Returns:
            dict[str, Callable]: events list to register. (key: event name, val: func)
        """
        return {
            E.ADD_CARD: self.on_add_card,
            E.REORDER: self.on_reorder,
        }

    def on_add_card(self) -> None:
        """Add :class:`DraggableCard`.
        """
        index = len(self.cards)
        card = DraggableCard(master=self, event_bus=self.event_bus, index=index)
        card.grid(row=index, column=0, pady=10, sticky=ctk.EW)
        self.cards.append(card)

    def render(self) -> None:
        """Render :class:`DraggableCard`.
        """
        for i, card in enumerate(self.cards):
            card.grid_forget()
            card.index = i
            card.grid(row=i, column=0, pady=10, sticky=ctk.EW)
        LOGGER.debug(f'{self.cards=}')

    def on_reorder(self, drag_idx: int, drop_item_y: int) -> None:
        """Reorder :class:`DraggableCard`.

        Args:
            drag_idx (int): Index of :class:`DraggableCard` after dragging.
            drop_item_y (int): The y coordinate of the mouse at the time of the drop.
        """
        if len(self.cards) < MIN_CARD_LENGTH:
            return
        space_width = int(self.cards[1].winfo_y() - self.cards[0].winfo_y())
        drop_idx = drag_idx + drop_item_y // space_width
        if 0 <= drop_idx < len(self.cards) and drop_idx != drag_idx:
            LOGGER.debug(f'{drag_idx=}, {self.cards[drag_idx].index=}')
            LOGGER.debug(f'{drop_idx=}, {self.cards[drop_idx].index=}')
            self.cards[drag_idx], self.cards[drop_idx] = (
                self.cards[drop_idx], self.cards[drag_idx],
            )
            self.render()
