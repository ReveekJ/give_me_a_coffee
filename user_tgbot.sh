#!/bin/sh
alembic upgrade head
exec python3 -m src.user_tgbot.bot
