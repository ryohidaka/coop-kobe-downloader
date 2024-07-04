import calendar
from datetime import date, timedelta
from enum import Enum


class Weekday(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7


def get_weekday_str(weekday: Weekday, offset: int = 0) -> str:
    """
    指定された曜日とオフセットに基づいて特定の週の文字列を生成します。

    Parameters:
    * param weekday: 対象の曜日（`Weekday`列挙型）
    * param offset: 過去の週数（デフォルトは`0`、現在の週）

    Return: 年、月、週を表す文字列
    """
    # 今日の日付を取得
    today = date.today()

    # 今日の曜日を取得
    today_weekday = today.isoweekday()

    # 対象の曜日を計算
    target_weekday = weekday.value

    # 今日から対象の曜日までの日数を計算
    days_until_target = (today_weekday - target_weekday) % 7

    # 対象の日付を計算（オフセットに基づいて調整）
    target_day = today - timedelta(days=days_until_target) - timedelta(weeks=offset - 1)

    # 年、月、日を取得
    year = target_day.year
    month = target_day.month
    day = target_day.day

    # get_nth_week関数を呼び出して結果を取得
    res = get_nth_week(year, month, day)

    # 年、月、結果を文字列として結合して返す
    return f"{year}{str(month).zfill(2)}{res}"


def get_nth_week(year: int, month: int, day: int, first_weekday: int = 0) -> int:
    """
    指定された日付が月の第何週目に当たるかを計算します。

    Parameters:
    * year: 年
    * month: 月
    * day: 日
    * first_weekday: 週の最初の曜日（デフォルトは`0`: 月曜日）

    Return: 第何週目かを示す整数
    """
    # 月の最初の日の曜日を取得
    first_dow = calendar.monthrange(year, month)[0]

    # 週の開始曜日に基づいてオフセットを計算
    offset = (first_dow - first_weekday) % 7

    # 指定された日が第何週目かを計算
    return (day + offset - 1) // 7 + 1
