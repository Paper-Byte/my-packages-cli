#!/usr/bin/env python3

from models.language import Language
from models.package import Package
from rich.progress import track
import time
import ipdb


def reset_database():
    Package.drop_table()
    Language.drop_table()
    Language.create_table()
    Package.create_table()

    vainilla_js = Language.create("Vanilla JS")
    react = Language.create(
        "React")
    Package.create(
        "Chakra UI", "npm install @chakra-ui/react @emotion/react @emotion/styled framer-motion", react.id)
    Package.create(
        "Tailwind CSS", "npm install -D tailwindcss", vainilla_js.id)
    Package.create("react-icons", "npm install react-icons --save", react.id)
    Package.create("Redux", "npm install @reduxjs/toolkit", react.id)
    Package.create("React-Redux", "npm install react-redux", react.id)
    Package.create("HowlerJS", "npm install howler", vainilla_js.id)
    Package.create("HowlerJS", "npm install howler", vainilla_js.id)
    Package.create("PushJS", "npm install push.js --save", vainilla_js.id)


reset_database()
for i in track(range(1), description='Starting up clean debug...'):
    time.sleep(.20)
ipdb.set_trace()
