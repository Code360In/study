# 1
from datetime import datetime, timedelta
ex = datetime.now().strftime('%Y-%m-%d')
ex
# 2
date_template = '%Y-%m-%d'
(datetime.strptime(exe_date, date_template) - timedelta(days=1)).strftime(date_template)
# 3
from dateutil.relativedelta import relativedelta
datetime.strftime(datetime.strptime(exe_date, '%Y-%m-%d') - relativedelta(day=1), '%Y-%m-%d')
std_dt = datetime.strftime(datetime.strptime(get_day_ago_date(exe_date, 1), '%Y-%m-%d'), "%Y%m%d")
std_day = int(std_dt[-2:])
get_day_ago_date(exe_date, std_day)
# 4
import calendar
def get_last_day(exe_date):
date_array = exe_date.split('-')
return calendar.monthrange(int(date_array[0]),int(date_array[1]))[1]
print(f'{exe_date[:-2]}{get_last_day(exe_date)} 00:00:00')
