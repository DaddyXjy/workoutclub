import os
import datetime
from optparse import OptionParser  

'''
for x in range(10, 31):
    with open(f"写作打卡/5.{x}日写作打卡.md", 'w') as f:
        f.write(f"# 5.{x}日写作打卡")
'''


def list_all_days(year,startMonth = 1):
    beginDay = datetime.date(year,startMonth or 1,1)
    endDay = datetime.date(year,12,31)
    allDaysCount = (endDay - beginDay).days + 1
    allDays = []
    for i in range(allDaysCount):
        day = beginDay + datetime.timedelta(days=i)
        allDays.append(day)
    return allDays
    
def gen_file(day):
    filename = f"{day.year}.{day.month}.{day.day}workout"
    linkname = f"{day.year}.{day.month}.{day.day}-健身打卡"
    dirpath = f'workout/{day.year}y-workout/{day.year}y-{day.month}m-workout'
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    filepath = f'{dirpath}/{filename}.md'
    with open(filepath, 'w') as f:
        f.write(f"# {linkname}\n")
        f.write(f"## 训练内容\n")
        f.write(f"## 饮食\n")
    print(filepath)

def gen_summary(day):
    filename = f"{day.year}.{day.month}.{day.day}workout"
    linkname = f"{day.year}.{day.month}.{day.day}-健身打卡"
    dirpath = f'workout/{day.year}y-workout/{day.year}y-{day.month}m-workout'
    text = f' - [ ] [{linkname}](/{dirpath}/{filename}.md)\n'
    return text
def gen_year_file(year,startMonth = 1):
    days = list_all_days(year , startMonth= startMonth)
    for day in days:
        gen_file(day)

def gen_summary_readme_file(year,month,text):
    filename = f"{year}y-{month}m-workout"
    linkname = f"{year}年{month}月-健身打卡汇总"
    dirpath = f'workout/{year}y-workout/{year}y-{month}m-workout'
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    filepath = f'{dirpath}/{filename}.md'    
    with open(filepath, 'w') as f:
        f.write(f"# {linkname}\n")
        f.write(text)
def gen_year_summary(year,startMonth = 1):
    days = list_all_days(year , startMonth= startMonth)
    iterMonth = days[0].month - 1
    monthText = ''
    for day in days:
        if iterMonth != day.month:
            if monthText != '':
                gen_summary_readme_file(day.year, iterMonth,monthText)
            monthText = ''
            iterMonth = day.month
        monthText = monthText + gen_summary(day)  
    else:
        gen_summary_readme_file(day.year, iterMonth,monthText)
if __name__ == '__main__':
    parser = OptionParser()  
    parser.add_option("-y", "--year",  
                action = "store",  
                type = 'int',  
                dest = "year",  
                default = None,  
                help="generate year files"  
                )
    parser.add_option("-m", "--month",  
            action = "store",  
            type = 'int',  
            dest = "month",  
            default = None,  
            help="generate from start month"  
            )  
    (options, args) = parser.parse_args() 
    gen_year_file(options.year , startMonth= options.month)
    print(gen_year_summary(options.year , startMonth= options.month))


