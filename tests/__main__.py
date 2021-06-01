# alfareza

import os

from alphaz import alphaz


async def _worker() -> None:
    chat_id = int(os.environ.get("CHAT_ID") or 0)
    type_ = 'unofficial' if os.path.exists("../alphaz/plugins/unofficial") else 'main'
    await alphaz.send_message(chat_id, f'`{type_} build completed !`')

if __name__ == "__main__":
    alphaz.begin(_worker())
    print('alphaz test has been finished!')
