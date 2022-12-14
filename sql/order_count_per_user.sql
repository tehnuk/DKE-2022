SELECT users.*, orders.order_count
    from
    (
        SELECT "Код клиента", count(distinct "Код заказа") as order_count
        from "Заказ клиента" group by "Код клиента"
    ) as orders
    join Клиент as users on orders."Код клиента" == users."Код клиента"