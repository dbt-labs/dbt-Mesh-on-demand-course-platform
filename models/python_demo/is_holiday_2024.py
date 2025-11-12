import holidays
import pandas

def model(dbt, session):
    dbt.config(
        materialized="table",
        packages=['pandas', 'holidays']
    )

    us_holidays = holidays.US()

    df = dbt.ref('stg_orders').to_pandas()
    df['IS_HOLIDAY'] = df['ordered_at'].apply(lambda date: date in us_holidays)

    return df