from datetime import datetime


class Date:
    @staticmethod
    async def convert_to_timestamp(date):
        return int(datetime.timestamp(datetime.strptime(date, '%d.%m.%Y')))
