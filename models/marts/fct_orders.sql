with orders as (
    select * from {{ ref('int_orders') }}
    where ordered_at<= current_date
),

final as (
    select 
        orders.*,
        date_part(month, ordered_at) as ordered_month,
        date_part(day, ordered_at) as ordered_day, 
        date_part(year, ordered_at) as ordered_year
    from orders
)

select * 
from final