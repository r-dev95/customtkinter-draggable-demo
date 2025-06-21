"""This is the module that defines event base component class.
"""

from abc import ABC, abstractmethod
from collections.abc import Callable
from logging import getLogger

import customtkinter as ctk

from lib.common.types import ParamLog

PARAM_LOG = ParamLog()
LOGGER = getLogger(PARAM_LOG.NAME)


class EventBus:
    """Subscribe and run events.
    """
    def __init__(self) -> None:
        self.listeners: dict[str, list[Callable]] = {}

    def subscribe(self, event_name: str, callback: Callable) -> None:
        """Subscribe an event.

        Args:
            event_name (str): event name.
            callback (Callable): callback function.
        """
        LOGGER.debug(f'{event_name=}, {callback=}')
        self.listeners.setdefault(event_name, []).append(callback)

    def emit(self, event_name: str, *args, **kwargs) -> None:  # noqa: D417
        """Run an event.

        Args:
            event_name (str): event name.
        """
        LOGGER.debug(f'{event_name=}, {args=}, {kwargs=}')
        for callback in self.listeners.get(event_name, []):
            callback(*args, **kwargs)


class BaseComponent(ABC):
    """Defines the base of the class that receives the :class:`EventBus` class.

    Args:
        event_bus (EventBus): :class:`EventBus` class.
    """
    def __init__(self, event_bus: EventBus) -> None:
        self.event_bus = event_bus
        items = self.register_events()

        if items:
            for event_name, callback in items.items():
                LOGGER.debug(f'{event_name=}, {callback=}')
                self.event_bus.subscribe(event_name=event_name, callback=callback)

    @abstractmethod
    def register_events(self) -> dict[str, Callable]:
        """Returns a list of events to subscribe to.

            *   Define it in the child class.

        Returns:
            dict[str, Callable]: events list to register. (key: event name, val: func)
        """
        ...


class BasePage(ctk.CTkScrollableFrame, BaseComponent):
    """Defines the base page.

    Args:
        master (ctk.CTk): parent widget class.
        event_bus (EventBus): :class:`EventBus` class.
        page_name (str): page name.
    """
    def __init__(
            self,
            master: ctk.CTk,
            event_bus: EventBus,
            page_name: str,
            **kwargs,
        ) -> None:
        ctk.CTkScrollableFrame.__init__(self=self, master=master, **kwargs)
        BaseComponent.__init__(self=self, event_bus=event_bus)

        self.configure(fg_color='transparent', label_text=page_name)
