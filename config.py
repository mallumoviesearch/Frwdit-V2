#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "14623143"))
    API_HASH = os.environ.get("API_HASH", "51ee2679d47d66aed5795876afc67622")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5905715077:AAHoxsnqZvpW3monZ5uoRjDbw_5e283V1HE")
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "@MALLU_MOVIE_SEARCH")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", "1963316264")
    SESSION = os.environ.get("SESSION", "") 
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
