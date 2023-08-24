import time
from utils import logger
from multiprocessing.dummy import Pool
from reger import Reger
from config import REF_CODE, SLEEP_MEJDU_AKKAMI


def main(mail: str):
    reger = Reger(mail=mail)
    session = reger.get_session()
    add_to_waitlist: bool = reger.add_to_waitlist(session=session, ref_code=REF_CODE)

    if add_to_waitlist:
        with open('registered.txt', 'a') as file:
            file.write(f'{mail}\n')

        logger.success(f'Успешно зарегистрировал почту {mail} в вэйтлист')
    else:

        logger.error('еррор, перехожу к следующей почте')

    time.sleep(SLEEP_MEJDU_AKKAMI)


if __name__ == '__main__':
    with open('mails.txt', 'r') as file:
        mails: list = file.read().split('\n')

    logger.info(f'Загружено {len(mails)} аккаунтов')

    threads: int = int(input('Threads: '))
    print('')

    with Pool(processes=threads) as executor:
        executor.map(main, mails)